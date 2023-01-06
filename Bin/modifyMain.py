import json
import os

from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QItemDelegate,
                             QMainWindow, QMessageBox, QTableWidgetItem)
from ui.modify import Ui_ModifyWindow
from utils.ListWidgetManager import ListWidgetManager
from utils.Logger import logger
from utils.TableWidgetManager import TableWidgetManager
from utils.UniqueFont import UniqueFont


class EmptyDelegate(QItemDelegate):
    '''代理类，用于禁用表格编辑'''

    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class ModifyMain(QMainWindow, Ui_ModifyWindow):

    def __init__(self):
        super(ModifyMain, self).__init__()
        self.setupUi(self)

        # 实例化日志对象
        self.logger = logger('modifyMain')
        # 实例化ListWidget管理类
        self.listWidgetManager = ListWidgetManager(self.basicTab_modifyRecordListWidget)
        # 实例化TableWidget管理类
        self.tableWidgetManager = TableWidgetManager(self.basicTab_tableWidget)
        # 实例化字体管理类
        self.uniqueFont = UniqueFont()

        # 获取当前路径
        self.currentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.cachePath = os.path.join(self.currentPath, 'cache')
        # 默认文件路径
        self.defaultFilePath = os.path.join(self.currentPath, 'default')
        self.defaultGameValueFile = os.path.join(self.defaultFilePath, 'game-values.json')
        self.defaultTowerStatFile = os.path.join(self.defaultFilePath, 'tower-stats.json')

        self.initMenu()

        self.initUI()

    def initMenu(self):
        '''初始化及绑定菜单栏动作'''
        # 退出
        self.actionExit.triggered.connect(self.close)
        # 载入游戏路径
        self.actionLoad_game_path.triggered.connect(self.loadGamePath)
        # 载入资源文件
        self.actionLoad_resource.triggered.connect(self.loadResourceFile)

    def initUI(self):
        '''初始化UI'''
        # 在未载入游戏路径时禁用TabWidget
        for i in range(1, 6):
            self.tabWidget.setTabEnabled(i, False)

        ############################## basicTab UI ##############################

        # 绑定按钮动作
        self.basicTab_searchBtn.clicked.connect(self.searchBasicVar)
        self.basicTab_selectBtn.clicked.connect(self.selectBasicVar)
        self.basicTab_recallRecordBtn.clicked.connect(self.recallRecord)
        self.basicTab_resetModifyBtn.clicked.connect(self.resetRecord)
        self.basicTab_exportRecordBtn.clicked.connect(self.exportRecord)
        self.basicTab_outputBtn.clicked.connect(self.outputFile)
        self.basicTab_applyBtn.clicked.connect(self.applyFile)
        self.basicTab_infoBtn.clicked.connect(lambda: self.showRecordInfo(self.basicTab_modifyRecordWidget))

        # 绑定ComboBox动作
        self.basicTab_selectComboBox_1.activated.connect(self.selectChange)

        # 绑定TableWidget动作
        self.basicTab_tableWidget.cellChanged.connect(self.valueModify)

        # 设置表格头部自适应缩放
        self.basicTab_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.basicTab_tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.basicTab_tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)
        # 隐藏列表头
        self.basicTab_tableWidget.verticalHeader().setHidden(True)
        # 设置表格自动换行
        self.basicTab_tableWidget.setWordWrap(True)
        # 设置表格前四列不可编辑
        for i in range(0, 4):
            self.basicTab_tableWidget.setItemDelegateForColumn(i, EmptyDelegate(self))

        # 设置修改记录widget隐藏
        self.basicTab_modifyRecordWidget.hide()
        # 设置修改记录widget隐藏
        self.towerTab_modifyRecordGroupBox.hide()

        ############################## towerTab UI ##############################

        # 绑定左侧Tag
        self.towerTab_basicTag.clicked.connect(lambda: self.tagChange('basic'))
        self.towerTab_sniperTag.clicked.connect(lambda: self.tagChange('sniper'))
        self.towerTab_cannonTag.clicked.connect(lambda: self.tagChange('cannon'))
        self.towerTab_freezingTag.clicked.connect(lambda: self.tagChange('freezing'))
        self.towerTab_airTag.clicked.connect(lambda: self.tagChange('air'))
        self.towerTab_splashTag.clicked.connect(lambda: self.tagChange('splash'))
        self.towerTab_blastTag.clicked.connect(lambda: self.tagChange('blast'))
        self.towerTab_multishotTag.clicked.connect(lambda: self.tagChange('multishot'))
        self.towerTab_minigunTag.clicked.connect(lambda: self.tagChange('minigun'))
        self.towerTab_venomTag.clicked.connect(lambda: self.tagChange('venom'))
        self.towerTab_teslaTag.clicked.connect(lambda: self.tagChange('tesla'))
        self.towerTab_missileTag.clicked.connect(lambda: self.tagChange('missile'))
        self.towerTab_flamethrowerTag.clicked.connect(lambda: self.tagChange('flamethrower'))
        self.towerTab_laserTag.clicked.connect(lambda: self.tagChange('laser'))
        self.towerTab_gaussTag.clicked.connect(lambda: self.tagChange('gauss'))
        self.towerTab_crusherTag.clicked.connect(lambda: self.tagChange('crusher'))

        # 绑定按钮动作
        self.towerTab_infoBtn.clicked.connect(lambda: self.showRecordInfo(self.towerTab_modifyRecordGroupBox))

        # 设置表格自动换行
        self.towerTab_basicAttributeTableWidget.setWordWrap(True)

    ################## Methods of Menu ##################

    def loadGamePath(self):
        '''载入游戏路径'''
        print('载入游戏路径')
        self.gamePath = QFileDialog.getExistingDirectory(self, "选取文件夹",
                                                         "G:/SteamLibrary/steamapps/common/Infinitode 2") + '/'

        # 获取路径下的文件夹
        gamePathList = os.listdir(self.gamePath)
        # 判断是否存在res文件夹
        if 'res' in gamePathList:
            self.logger.info('找到res文件夹')
            self.resource = os.path.join(self.gamePath, 'res/')
            # res文件夹下的目标文件
            resourceFileList = [
                "achievements.json",
                "game-values.json",
                "tower-enemy-attack-matrix.json",
                "tower-enemy-damage-matrix.json",
                "tower-stats.json",
            ]
            # 判断是否存在目标文件
            for file in resourceFileList:
                if os.path.exists(os.path.join(self.resource, file)):
                    continue
                # 如果有不存在的目标文件，则弹出警告框
                else:
                    self.logger.error('未找到文件 {}'.format(file))
                    QMessageBox.warning(
                        self, '警告', "在当前游戏路径的 res 文件夹下未找到 {} 文件\n请重新选择游戏安装路径，或使用 '载入资源文件' 手动选择 res 文件夹".format(file),
                        QMessageBox.StandardButton.Yes)
                    break
            # 如果目标文件都存在，则载入文件路径
            else:
                self.achievementsFile = os.path.join(self.resource, resourceFileList[0])
                self.gameValueFile = os.path.join(self.resource, resourceFileList[1])
                self.towerEnemyAttackMatrixFile = os.path.join(self.resource, resourceFileList[2])
                self.towerEnemyDamageMatrixFile = os.path.join(self.resource, resourceFileList[3])
                self.towerStatsFile = os.path.join(self.resource, resourceFileList[4])
                self.logger.info('载入文件路径成功')

                # 启用TabWidget
                self.tabWidget.setTabEnabled(0, True)
                self.tabWidget.setTabEnabled(1, True)
                # 将路径填充到文本框
                self.basicTab_initFileLineEdit.setText(self.gameValueFile)
                # 显示Tab1
                self.tabWidget.setCurrentIndex(0)

                # 解析基础变量文件
                self.gameValueFileParse()

                # 解析塔属性文件
                self.towerStatsFileParse()

        # 如果不存在res文件夹
        else:
            self.logger.error('未找到res文件夹')
            QMessageBox.warning(self, '警告',
                                "在当前游戏路径 {} 未找到 res 文件夹\n请重新选择游戏安装路径，或使用 '载入资源文件' 手动选择 res 文件夹".format(self.gamePath),
                                QMessageBox.StandardButton.Yes)
            return 0

    def loadResourceFile(self):
        '''载入资源文件'''
        print('载入资源文件')
        self.resource = QFileDialog.getExistingDirectory(self, "选取文件夹", "G:/SteamLibrary/steamapps/common/Infinitode 2")
        # res文件夹下的目标文件
        resourceFileList = [
            "achievements.json",
            "game-values.json",
            "tower-enemy-attack-matrix.json",
            "tower-enemy-damage-matrix.json",
            "tower-stats.json",
        ]
        # 判断是否存在目标文件
        for file in resourceFileList:
            if os.path.exists(os.path.join(self.resource, file)):
                continue
            # 如果有不存在的目标文件，则弹出警告框
            else:
                self.logger.error('未找到文件 {}'.format(file))
                QMessageBox.warning(self, '警告', "在当前资源路径的 res 文件夹下未找到 {} 文件\n请重新选择资源路径".format(file),
                                    QMessageBox.StandardButton.Yes)
                return 0
        # 如果目标文件都存在，则载入文件路径
        else:
            self.achievementsFile = os.path.join(self.resource, resourceFileList[0])
            self.gameValueFile = os.path.join(self.resource, resourceFileList[1])
            self.towerEnemyAttackMatrixFile = os.path.join(self.resource, resourceFileList[2])
            self.towerEnemyDamageMatrixFile = os.path.join(self.resource, resourceFileList[3])
            self.towerStatsFile = os.path.join(self.resource, resourceFileList[4])
            self.logger.info('载入文件路径成功')

            # 启用TabWidget
            self.tabWidget.setTabEnabled(0, True)
            self.tabWidget.setTabEnabled(1, True)
            # 将路径填充到文本框
            self.basicTab_initFileLineEdit.setText(self.gameValueFile)
            # 显示Tab1
            self.tabWidget.setCurrentIndex(0)
            # 解析基础变量文件
            self.gameValueFileParse()
            # 解析塔属性文件
            self.towerStatsFileParse()

    ################## Methods of Tab Basic ##################

    def gameValueFileParse(self):
        '''解析基础变量文件'''

        # 读取文件
        with open(self.gameValueFile, 'r', encoding='utf-8') as f:
            self.gameValueFileContent = json.load(f)

        with open(self.defaultGameValueFile, 'r', encoding='utf-8') as f:
            defaultGameValueFileContent = json.load(f)

        # 将变量的描述信息填充到变量字典中
        for var in self.gameValueFileContent:
            if defaultGameValueFileContent[var].get('desc'):
                self.gameValueFileContent[var]['desc'] = defaultGameValueFileContent[var]['desc']
            else:
                self.gameValueFileContent[var]['desc'] = '-'
        # 从字典将数据渲染到表格中
        self.tableWidgetManager.renderItemsFromDict(self.gameValueFileContent)

    def searchBasicVar(self):
        '''搜索基础变量'''
        # 获取搜索框内容
        searchContent = self.basicTab_searchLineEdit.text()
        # 如果搜索框内容为空，则不搜索
        if searchContent.strip() == '':
            return 0
        # 如果搜索框内容不为空，则搜索
        else:
            # 处理搜索内容
            searchContentList = searchContent.upper().split(" ")
            resDict = {}
            for searchKeyWord in searchContentList:
                for var in self.gameValueFileContent:
                    if (searchKeyWord in var) or (searchKeyWord in self.gameValueFileContent[var]['desc']):
                        resDict[var] = self.gameValueFileContent[var]
            # 清空表格
            self.basicTab_tableWidget.clearContents()
            # 将搜索结果渲染到表格中
            self.tableWidgetManager.renderItemsFromDict(resDict)
        return resDict

    def selectChange(self):
        select_1 = self.basicTab_selectComboBox_1.currentText()
        if select_1 == '塔属性':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.addItems([
                "基础塔",
                "狙击塔",
                "加农炮",
                "寒冰塔",
                "防空塔",
                "溅射塔",
                "爆破塔",
                "散射塔",
                "机枪塔",
                "毒液塔",
                "特斯拉",
                "导弹",
                "火焰塔",
                "激光塔",
                "电磁炮",
                "破碎机",
            ])
        elif select_1 == '技能':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.addItems([
                "火球",
                "暴风雪",
                "火焰风暴",
                "雷",
                "烟雾弹",
                "风暴",
                "磁铁",
                "子弹墙",
                "球状闪电",
                "LOIC",
                "核武器",
                "超载",
            ])
        elif select_1 == '杂项':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.addItems([
                "矿机",
                "积分",
            ])

    def selectBasicVar(self):
        select = self.basicTab_selectComboBox_2.currentText()
        selectKeywordDict = {
            "基础塔": "BASIC",
            "狙击塔": "SNIPER",
            "加农炮": "CANNON",
            "寒冰塔": "FREEZING",
            "防空塔": "AIR",
            "溅射塔": "SPLASH",
            "爆破塔": "BLAST",
            "散射塔": "MULTISHOT",
            "机枪塔": "MINIGUN",
            "毒液塔": "VENOM",
            "特斯拉": "TESLA",
            "导弹": "MISSILE",
            "火焰塔": "FLAME",
            "激光塔": "LASER",
            "电磁炮": "GAUSS",
            "破碎机": "CRUSHER",
            "火球": "ABILITY_FIREBALL",
            "暴风雪": "ABILITY_BLIZZARD",
            "火焰风暴": "ABILITY_FIRESTORM",
            "雷": "ABILITY_THUNDER",
            "烟雾弹": "ABILITY_SMOKE",
            "风暴": "ABILITY_WINDSTORM",
            "磁铁": "ABILITY_MAGNET",
            "子弹墙": "ABILITY_BULLET_WALL",
            "球状闪电": "ABILITY_BALL_LIGHTNING",
            "LOIC": "ABILITY_LOIC",
            "核武器": "ABILITY_NUKE",
            "超载": "ABILITY_OVERLOAD",
            "矿机": "MINER",
            "积分": "SCORE",
        }
        resDict = {}
        for var in self.gameValueFileContent:
            if selectKeywordDict[select] in var:
                resDict[var] = self.gameValueFileContent[var]

        # 将筛选结果渲染到表格中
        self.tableWidgetManager.renderItemsFromDict(resDict)

        return resDict

    def valueModify(self):
        row = self.basicTab_tableWidget.currentRow()
        col = self.basicTab_tableWidget.currentColumn()
        if col == 4:
            value = self.basicTab_tableWidget.item(row, col).text()
            if value != '':
                if self.basicTab_tableWidget.item(row, 2).text() == '布尔值':
                    if value in ["1", "0"]:
                        pass
                    else:
                        self.basicTab_tableWidget.item(row, col).setText('')
                        QMessageBox.warning(self, '错误', '布尔值只能为0或1')
                        self.logger.error('布尔值只能为0或1')
                        return 0

                var = self.basicTab_tableWidget.item(row, 0).text().replace(" ", "_")
                self.gameValueFileContent[var]['modify'] = value

                self.listWidgetManager.update(var, value)
                self.logger.info(f'修改变量{var}的值为{value}')

    def recallRecord(self):
        currentRow = self.basicTab_modifyRecordListWidget.currentRow()
        print(currentRow)
        if currentRow != -1:
            var = self.listWidgetManager.getvar(currentRow)  # 获取撤回的变量
            self.listWidgetManager.remove(currentRow)  # 删除撤回的变量
            print(var)
            # 获取当前表格中显示的所有变量
            currentTableVars = self.tableWidgetManager.getCurrentVars()
            if var in currentTableVars:
                # 如果撤回的变量在表格中，那么就刷新显示
                self.basicTab_tableWidget.item(currentTableVars.index(var), 4).setText('')
            else:
                # 如果撤回的变量不在表格中，那么就更新gameValueFileContent
                self.gameValueFileContent[var]['modify'] = ''
            self.logger.info(f'撤回修改变量{var}')

    def resetRecord(self):
        choose = QMessageBox.information(self, '提示', '重置修改记录后，所有修改将不可恢复', QMessageBox.StandardButton.Ok,
                                         QMessageBox.StandardButton.Cancel)
        if choose == QMessageBox.StandardButton.Ok:
            # 获取当前表格中显示的所有变量
            currentTableVars = self.tableWidgetManager.getCurrentVars()
            for var in self.listWidgetManager.varList:
                self.gameValueFileContent[var]['modify'] = ''
                if var in currentTableVars:
                    self.basicTab_tableWidget.item(currentTableVars.index(var), 4).setText('')

            self.listWidgetManager.clear()
            self.logger.info('重置修改记录')
        else:
            pass

    def exportRecord(self):
        if self.listWidgetManager.varList == []:
            QMessageBox.warning(self, '错误', '没有修改记录')
            self.logger.error('没有修改记录')
            return 0
        else:
            path = QFileDialog.getSaveFileName(self, '保存修改记录', './', '文本文件(*.txt)')[0]
            if path != '':
                self.listWidgetManager.output(path)
                self.logger.info(f'保存修改记录到{path}')
            else:
                pass

    def outputFile(self):
        path = QFileDialog.getSaveFileName(self, '保存修改后的文件', './', 'json源文件(*.json)')[0]
        if path != '':
            outputDict = self.gameValueFileContent.copy()
            modifyVars = self.listWidgetManager.varList
            for var in modifyVars:
                outputDict[var]['default'] = int(outputDict[var]['modify'])
                del outputDict[var]['modify']
            for var in outputDict:
                del outputDict[var]['desc']

            with open(path, 'w', encoding='utf-8') as f:
                json.dump(outputDict, f, indent=4, ensure_ascii=False)
            self.logger.info(f'保存修改后的文件到{path}')
        else:
            pass

    def applyFile(self):
        choose = QMessageBox.warning(self, '警告', '覆盖文件后，所有修改将不可恢复', QMessageBox.StandardButton.Ok,
                                     QMessageBox.StandardButton.Cancel)
        if choose == QMessageBox.StandardButton.Ok:
            path = os.path.join(self.gamePath, "res/"
                                'game-values.json')
            if path != '':
                outputDict = self.gameValueFileContent.copy()
                modifyVars = self.listWidgetManager.varList
                for var in modifyVars:
                    outputDict[var]['default'] = int(outputDict[var]['modify'])
                    del outputDict[var]['modify']
                for var in outputDict:
                    del outputDict[var]['desc']

                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(outputDict, f, indent=4, ensure_ascii=False)
                self.logger.info(f'覆盖修改后的文件到{path}')
            else:
                pass
        else:
            pass

    def showRecordInfo(self, widget):
        '''可能的公共方法，用于显示或隐藏widget'''
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()

    ################## Methods of Tab Tower ##################
    def tagChange(self, towerName):
        '''标签改变'''
        tags = []
        for tagObj in self.towerTab_tagWidget.children()[1:]:
            name = tagObj.objectName().split('_')[1].replace("Tag", "")
            if name != towerName:  # 将不被点击的标签对象加入列表，以便统一处理
                tags.append((name, tagObj))
            else:
                # 处理被点击的标签，置为亮色
                clickedTag = tagObj
                clickedTag.setStyleSheet("border-image: url(:/tower_c/tower_48_color/TOWER_{}.png)".format(
                    towerName.upper()))
                self.currentTower = towerName

        # 处理未被点击的标签,全部置灰
        for tup in tags:
            tagObj = tup[1]
            tagName = tup[0]
            tagObj.setStyleSheet(
                "QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_%s.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_%s_1.png);}"
                % (tagName.upper(), tagName.upper()))

        self.towerTabTowerStatTableShow(towerName)

    def towerStatsFileParse(self):
        '''解析tower_stats.json文件'''
        attributesZh = {
            'prices': '价格',
            'RANGE': '射程',
            'DAMAGE': '伤害',
            'ATTACK_SPEED': '攻击速度',
            'ROTATION_SPEED': '旋转速度',
            'PROJECTILE_SPEED': '子弹速度',
            'U_BURN_CHANCE': '燃烧机率',
            'U_BURNING_TIME': '燃烧时间',
            'U_DAMAGE_MULTIPLY': '伤害加成',
            'STUN_CHANCE': '眩晕机率',
            'U_STUN_DURATION': '眩晕时间',
            'U_EXPLOSION_RANGE': '爆炸范围',
            'FREEZE_PERCENT': '冰冻机率',
            'FREEZE_SPEED': '冰冻速度',
            'U_POISON_DURATION_BONUS': '中毒时间',
            'U_CHAIN_LIGHTNING_BONUS_LENGTH': '链电长度',
            'U_BATTERIES_CAPACITY': '电池容量',
            'U_ACCELERATION': '加速度',
            'U_PROJECTILE_COUNT': '子弹数量',
            'U_SHOOT_ANGLE': '射击角度',
            'AIM_SPEED': '瞄准速度',
            'U_CRIT_CHANCE': '暴击机率',
            'U_CRIT_MULTIPLIER': '暴击加成',
            'ACCURACY': '精准度',
            'CHAIN_LIGHTNING_DAMAGE': '链电伤害',
            'U_CHAIN_LIGHTNING_LENGTH': '链电长度',
            'U_POISON_DURATION': '中毒时间',
            'RESOURCE_CONSUMPTION': '资源消耗',
            'CHARGING_SPEED': '充能速度',
            'DURATION': '持续时间',
            'U_BONUS_EXPERIENCE': '经验加成',
            'U_LRM_AIM_SPEED': '瞄准速度',
        }
        with open(self.towerStatsFile, 'r', encoding='utf-8') as f:
            towerStats = json.load(f)

        self.towerTab_basicAttributeTableWidgetInfo = {}
        self.towerTab_basicAttributeTableWidgetHeader = {}
        self.towerTab_abilityTableWidgetInfo = {}
        self.towerTab_abilityTableWidgetHeader = {}

        for tower in towerStats:
            # 初始化字典
            self.towerTab_basicAttributeTableWidgetHeader[tower] = []
            self.towerTab_basicAttributeTableWidgetInfo[tower] = []
            self.towerTab_abilityTableWidgetHeader[tower] = []
            self.towerTab_abilityTableWidgetInfo[tower] = []

            # 获取价格属性
            priceList = towerStats[tower]['prices']
            self.towerTab_basicAttributeTableWidgetHeader[tower].append(attributesZh["prices"])
            self.towerTab_basicAttributeTableWidgetInfo[tower].append(priceList)

            # 获取其他基础属性
            for att in towerStats[tower]["stats"]:
                # 如果属性值里有value字段，说明是基础属性
                if towerStats[tower]["stats"][att].get("values", 0):
                    self.towerTab_basicAttributeTableWidgetHeader[tower].append(attributesZh[att])
                    self.towerTab_basicAttributeTableWidgetInfo[tower].append(towerStats[tower]["stats"][att]["values"])
                    # 如果同时含有max字段
                    if towerStats[tower]["stats"][att].get("max", 0):
                        # 这里的索引-1是因为上面已经append进去一个列表，这个max要加在上述列表的最后，所以要用-1来取得上述列表
                        self.towerTab_basicAttributeTableWidgetInfo[tower][-1].append(
                            towerStats[tower]["stats"][att]["max"])
                    else:
                        # 如果没有max字段，就在最后加一个空值
                        self.towerTab_basicAttributeTableWidgetInfo[tower][-1].append("-")
                # 如果属性值里没有value字段，说明是特殊属性
                else:
                    self.towerTab_abilityTableWidgetHeader[tower].append(attributesZh[att])
                    sublist = []
                    sublist.append(towerStats[tower]["stats"][att]['startValue'])
                    sublist.append(towerStats[tower]["stats"][att]['valueDelta'])
                    # 如果同时含有max字段
                    if towerStats[tower]["stats"][att].get("max", 0):
                        sublist.append(towerStats[tower]["stats"][att]['max'])
                    else:
                        # 如果没有max字段，就在最后加一个空值
                        sublist.append("-")
                    self.towerTab_abilityTableWidgetInfo[tower].append(sublist)

    def towerTabTowerStatTableShow(self, towerName):
        # 信号断开
        self.towerTab_basicAttributeTableWidget.disconnect()

        towerName = towerName.upper()
        basicAttInfo = self.towerTab_basicAttributeTableWidgetInfo[towerName]
        basicAttHeader = self.towerTab_basicAttributeTableWidgetHeader[towerName]
        abilityInfo = self.towerTab_abilityTableWidgetInfo[towerName]
        abilityHeader = self.towerTab_abilityTableWidgetHeader[towerName]

        # self.towerTab_basicAttributeTableWidget.clear()
        verticalHeader = ['L0', 'L1', 'L2', 'L3', 'L4', 'L5', 'L6', 'L7', 'L8', 'L9', 'L10', '最大值']
        self.towerTab_basicAttributeTableWidget.setColumnCount(len(basicAttHeader))
        self.towerTab_basicAttributeTableWidget.setHorizontalHeaderLabels(basicAttHeader)
        self.towerTab_basicAttributeTableWidget.setRowCount(12)
        self.towerTab_basicAttributeTableWidget.setVerticalHeaderLabels(verticalHeader)
        
        for i in range(len(basicAttInfo)):
            for j in range(len(basicAttInfo[i])):
                item = QTableWidgetItem(str(basicAttInfo[i][j]))
                self.towerTab_basicAttributeTableWidget.setItem(j, i, item)

        self.towerTab_abilityTableWidget.clear()
        verticalHeader = ['初始值', '增量', '最大值']
        self.towerTab_abilityTableWidget.setColumnCount(len(abilityHeader))
        self.towerTab_abilityTableWidget.setHorizontalHeaderLabels(abilityHeader)
        self.towerTab_abilityTableWidget.setRowCount(3)
        self.towerTab_abilityTableWidget.setVerticalHeaderLabels(verticalHeader)
        
        for i in range(len(abilityInfo)):
            for j in range(len(abilityInfo[i])):
                item = QTableWidgetItem(str(abilityInfo[i][j]))
                self.towerTab_abilityTableWidget.setItem(i, j, item)

        # 加载完后，信号连接-单元格内容改变
        self.towerTab_basicAttributeTableWidget.cellChanged.connect(self.towerStatChange)

    def towerStatChange(self):
        attributesEn = {
            "价格": "prices",
            "射程": "RANGE",
            "伤害": "DAMAGE",
            "攻击速度": "ATTACK_SPEED",
            "旋转速度": "ROTATION_SPEED",
            "子弹速度": "PROJECTILE_SPEED",
            "燃烧机率": "U_BURN_CHANCE",
            "燃烧时间": "U_BURNING_TIME",
            "伤害加成": "U_DAMAGE_MULTIPLY",
            "眩晕机率": "STUN_CHANCE",
            "眩晕时间": "U_STUN_DURATION",
            "爆炸范围": "U_EXPLOSION_RANGE",
            "冰冻机率": "FREEZE_PERCENT",
            "冰冻速度": "FREEZE_SPEED",
            "中毒时间": "U_POISON_DURATION_BONUS",
            "链电长度": "U_CHAIN_LIGHTNING_BONUS_LENGTH",
            "电池容量": "U_BATTERIES_CAPACITY",
            "加速度": "U_ACCELERATION",
            "子弹数量": "U_PROJECTILE_COUNT",
            "射击角度": "U_SHOOT_ANGLE",
            "瞄准速度": "AIM_SPEED",
            "暴击机率": "U_CRIT_CHANCE",
            "暴击加成": "U_CRIT_MULTIPLIER",
            "精准度": "ACCURACY",
            "链电伤害": "CHAIN_LIGHTNING_DAMAGE",
            "链电长度": "U_CHAIN_LIGHTNING_LENGTH",
            "中毒时间": "U_POISON_DURATION",
            "资源消耗": "RESOURCE_CONSUMPTION",
            "充能速度": "CHARGING_SPEED",
            "持续时间": "DURATION",
            "经验加成": "U_BONUS_EXPERIENCE",
            "瞄准速度": "U_LRM_AIM_SPEED",
        }

        row = self.towerTab_basicAttributeTableWidget.currentRow()
        col = self.towerTab_basicAttributeTableWidget.currentColumn()
        # 获取修改的单元格
        item = self.towerTab_basicAttributeTableWidget.item(row, col)
        # 获取行标题
        rowHeader = self.towerTab_basicAttributeTableWidget.verticalHeaderItem(row).text()
        # 获取列标题
        columnHeader = self.towerTab_basicAttributeTableWidget.horizontalHeaderItem(col).text()
        # 获取修改后的值
        value = item.text()
        # 获取塔的名称
        towerName = self.currentTower.upper()
        print(towerName, rowHeader.replace("L",""), attributesEn[columnHeader], value)
        # 修改数据
        

