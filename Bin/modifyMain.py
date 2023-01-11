import json
import os

from const.Constant import Const
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QItemDelegate,
                             QMainWindow, QMessageBox, QTableWidgetItem)
from ui.modify import Ui_ModifyWindow
from utils.Logger import logger
from utils.TableWidgetManager import TableWidgetManager
from utils.TreeViewManager import TreeViewItem, TreeViewManager
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
        # 实例化TreeView管理类
        self.treeViewManager = TreeViewManager(self.modifyRecordTreeView)
        # 实例化TableWidget管理类
        self.basicTab_tableWidgetManager = TableWidgetManager(self.basicTab_tableWidget)
        # 实例化字体管理类
        self.uniqueFont = UniqueFont()
        # 实例化常量类
        self.const = Const()

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
        self.basicTab_searchLineEdit.textChanged.connect(self.searchBasicVar)
        self.basicTab_selectComboBox_2.currentIndexChanged.connect(self.selectBasicVar)
        self.recallRecordBtn.clicked.connect(self.recallRecord)
        self.resetModifyBtn.clicked.connect(self.resetRecord)
        self.exportRecordBtn.clicked.connect(self.exportRecord)
        # self.outputBtn.clicked.connect(self.outputFile)
        # self.applyBtn.clicked.connect(self.applyFile)
        self.basicTab_infoBtn.clicked.connect(lambda: self.showRecordInfo(self.modifyRecordWidget))

        # 绑定ComboBox动作
        self.basicTab_selectComboBox_1.activated.connect(self.selectChange)

        # 绑定TableWidget动作
        self.basicTab_tableWidget.cellChanged.connect(self.valueModify)

        # 设置表格头部自适应缩放
        self.basicTab_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # 设置表格自动换行
        self.basicTab_tableWidget.setWordWrap(True)
        # 设置表格前2列不可编辑
        for i in range(0, 2):
            self.basicTab_tableWidget.setItemDelegateForColumn(i, EmptyDelegate(self))

        # 设置修改记录widget隐藏
        self.modifyRecordWidget.hide()

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
            # 显示Tab1
            self.tabWidget.setCurrentIndex(0)
            # 解析基础变量文件
            self.gameValueFileParse()
            # 解析塔属性文件
            self.towerStatsFileParse()

    ################## Methods of Tab Basic ##################
    # FIXED:
    def gameValueFileParse(self):
        '''解析基础变量文件'''
        # 读取文件
        with open(self.gameValueFile, 'r', encoding='utf-8') as f:
            self.gameValueFileContent = json.load(f)

        # 将变量的描述信息填充到变量字典中
        for var in self.const.game_values:
            self.gameValueFileContent[var]['desc'] = self.const.game_values[var]

        # 将字典转换成2d列表
        data = []
        for key in self.gameValueFileContent:
            data.append([
                self.gameValueFileContent[key]['desc'], self.gameValueFileContent[key]['units'],
                self.gameValueFileContent[key]['default']
            ])
        # 从字典将数据渲染到表格中
        self.basicTab_tableWidgetManager.render(horizonalHeader=['含义', '类型', '默认值'],
                                                verticalHeader=list(self.gameValueFileContent.keys()),
                                                data=data)

    # FIXED:
    def searchBasicVar(self):
        '''搜索基础变量'''
        self.basicTab_tableWidget.disconnect()  # 暂时断开tableWidget的信号槽
        # 获取搜索框内容
        searchContent = self.basicTab_searchLineEdit.text()
        # 如果搜索框内容为空，则不搜索
        if searchContent.strip() == '':
            # 重新连接tableWidget的信号槽
            self.basicTab_tableWidget.cellChanged.connect(self.valueModify)
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

            # 将resDict转换成2d列表
            data = []
            for key in resDict:
                data.append([resDict[key]['desc'], resDict[key]['units'], resDict[key]['default']])
            # 清空表格
            self.basicTab_tableWidget.clear()
            # 将搜索结果渲染到表格中
            self.basicTab_tableWidgetManager.render(horizonalHeader=['含义', '类型', '默认值'],
                                                    verticalHeader=list(resDict.keys()),
                                                    data=data)
            # 重新连接tableWidget的信号槽
            self.basicTab_tableWidget.cellChanged.connect(self.valueModify)

    # FIXED:
    def selectChange(self):
        # 暂时断开对 selectComboBox_2 的信号槽连接
        self.basicTab_selectComboBox_2.disconnect()
        select_1 = self.basicTab_selectComboBox_1.currentText()
        if select_1 == '塔属性':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.addItems(self.const.towerNameZh)
        elif select_1 == '技能':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.addItems(self.const.AbilityNameZh)
        elif select_1 == '杂项':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.addItems([
                "矿机",
                "积分",
            ])
        # 重新连接对 selectComboBox_2 的信号槽连接
        self.basicTab_selectComboBox_2.currentTextChanged.connect(self.selectBasicVar)

    # FIXED:
    def selectBasicVar(self):
        self.basicTab_tableWidget.disconnect()  # 暂时断开对tableWidget的信号槽连接
        select = self.basicTab_selectComboBox_2.currentText()
        selectKeywordDict = self.const.selectKeywordDict
        resDict = {}
        for var in self.gameValueFileContent:
            if selectKeywordDict[select] in var:
                resDict[var] = self.gameValueFileContent[var]

        # 将resDict转换成2d列表
        data = []
        for key in resDict:
            data.append([resDict[key]['desc'], resDict[key]['units'], resDict[key]['default']])
        # 将筛选结果渲染到表格中
        self.basicTab_tableWidgetManager.render(horizonalHeader=['含义', '类型', '默认值'],
                                                verticalHeader=list(resDict.keys()),
                                                data=data)
        # 重新连接对tableWidget的信号槽连接
        self.basicTab_tableWidget.cellChanged.connect(self.valueModify)

    # FIXED:
    def valueModify(self):
        row = self.basicTab_tableWidget.currentRow()
        col = self.basicTab_tableWidget.currentColumn()
        if col == 2:
            value = self.basicTab_tableWidget.item(row, col).text()
            if value != '':
                if self.basicTab_tableWidget.item(row, 1).text() == 'BOOLEAN':
                    if value in ["1", "0"]:
                        pass
                    else:
                        self.basicTab_tableWidget.item(row, col).setText('')
                        QMessageBox.warning(self, '错误', '布尔值只能为0或1')
                        self.logger.error('布尔值只能为0或1')
                        return 0
                # 获得本行的行头
                var = self.basicTab_tableWidget.verticalHeaderItem(row).text()

                item = TreeViewItem(modifyType="TCC",
                                    location=self.basicTab_tableWidget,
                                    mapto=self.gameValueFileContent,
                                    keys=(var, 'default'),
                                    col=int(col),
                                    row=int(row),
                                    colHeader=self.basicTab_tableWidget.horizontalHeaderItem(col).text(),
                                    rowHeader=var,
                                    oldValue=self.gameValueFileContent[var]['default'],
                                    newValue=value)
                self.treeViewManager.addTreeItem(item)

                self.gameValueFileContent[var]['default'] = value

    ################## Methods of Modify Record Widget ##################
    # FIXED:
    def recallRecord(self):
        '''撤回修改'''
        # 尝试获取当前行的子项：返回-1表示没有子项，当前项就是父项
        currentRow = self.modifyRecordTreeView.currentIndex().child(0, 0).row()
        if currentRow == -1:
            # 说明选的是子项
            currentSubRow = self.modifyRecordTreeView.currentIndex().row()
            parentRow = self.modifyRecordTreeView.currentIndex().parent().row()
            if parentRow == -1:
                # 说明选的是根节点，或者list里没有修改记录
                return 0
            else:
                res, locTable, mapto, keys, col, row, colHeader, rowHeader = self.treeViewManager.removeTreeItem(
                    parentRow, currentSubRow)
                # 更新表格
                temp = mapto
                for key in keys[:-1]:
                    temp = temp[key]
                temp[keys[-1]] = res

        else:
            # 说明选的是父项
            res, locTable, mapto, keys, col, row, colHeader, rowHeader = self.treeViewManager.removeTreeItem(
                currentRow, -1)
            # 更新表格
            temp = mapto
            for key in keys[:-1]:
                temp = temp[key]
            temp[keys[-1]] = res

        # 刷新显示
        verticalHeaders = []
        for i in range(locTable.rowCount()):
            verticalHeaders.append(locTable.verticalHeaderItem(i).text())
        if rowHeader in verticalHeaders:
            locTable.item(row, col).setText(str(res))
        else:
            pass
        # 恢复信号连接
        locTable.itemChanged.connect(self.valueModify)

    # FIXED:
    def resetRecord(self):
        '''重置修改'''
        choose = QMessageBox.information(self, '提示', '重置修改记录后，所有修改将不可恢复', QMessageBox.StandardButton.Ok,
                                         QMessageBox.StandardButton.Cancel)
        if choose == QMessageBox.StandardButton.Ok:
            for i in range(self.treeViewManager.itemsNum - 1, -1, -1):
                res, locTable, mapto, keys, col, row, colHeader, rowHeader = self.treeViewManager.removeTreeItem(i, -1)
                # 更新表格
                temp = mapto
                for key in keys[:-1]:
                    temp = temp[key]
                temp[keys[-1]] = res

                # 刷新显示
                verticalHeaders = []
                for i in range(locTable.rowCount()):
                    verticalHeaders.append(locTable.verticalHeaderItem(i).text())
                if rowHeader in verticalHeaders:
                    locTable.item(row, col).setText(str(res))
                else:
                    pass
                # 恢复信号连接
                locTable.itemChanged.connect(self.valueModify)
        else:
            pass

    # FIXED:
    def exportRecord(self):
        '''导出修改记录'''
        if self.treeViewManager.itemsNum == 0:
            QMessageBox.warning(self, '错误', '没有修改记录')
            self.logger.error('没有修改记录')
            return 0
        else:
            path = QFileDialog.getSaveFileName(self, '保存修改记录', './', '文本文件(*.txt)')[0]
            if path != '':
                self.treeViewManager.output(path)
                self.logger.info(f'保存修改记录到{path}')
            else:
                pass

    def showRecordInfo(self, widget):
        '''可能的公共方法，用于显示或隐藏widget'''
        if widget.isHidden():
            widget.show()
        else:
            widget.hide()

    # def outputFile(self):
    #     path = QFileDialog.getSaveFileName(self, '保存修改后的文件', './', 'json源文件(*.json)')[0]
    #     if path != '':
    #         outputDict = self.gameValueFileContent.copy()
    #         modifyVars = self.listWidgetManager.varList
    #         for var in modifyVars:
    #             outputDict[var]['default'] = int(outputDict[var]['modify'])
    #             del outputDict[var]['modify']
    #         for var in outputDict:
    #             del outputDict[var]['desc']

    #         with open(path, 'w', encoding='utf-8') as f:
    #             json.dump(outputDict, f, indent=4, ensure_ascii=False)
    #         self.logger.info(f'保存修改后的文件到{path}')
    #     else:
    #         pass

    # def applyFile(self):
    #     choose = QMessageBox.warning(self, '警告', '覆盖文件后，所有修改将不可恢复', QMessageBox.StandardButton.Ok,
    #                                  QMessageBox.StandardButton.Cancel)
    #     if choose == QMessageBox.StandardButton.Ok:
    #         path = os.path.join(self.gamePath, "res/"
    #                             'game-values.json')
    #         if path != '':
    #             outputDict = self.gameValueFileContent.copy()
    #             modifyVars = self.listWidgetManager.varList
    #             for var in modifyVars:
    #                 outputDict[var]['default'] = int(outputDict[var]['modify'])
    #                 del outputDict[var]['modify']
    #             for var in outputDict:
    #                 del outputDict[var]['desc']

    #             with open(path, 'w', encoding='utf-8') as f:
    #                 json.dump(outputDict, f, indent=4, ensure_ascii=False)
    #             self.logger.info(f'覆盖修改后的文件到{path}')
    #         else:
    #             pass
    #     else:
    #         pass

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
        attributesZh = self.const.attributesZh
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
        verticalHeader = [towerName + '-L0', towerName + '-L1', towerName + '-L2', towerName + '-L3', towerName + '-L4', towerName + '-L5', towerName + '-L6', towerName + '-L7', towerName + '-L8', towerName + '-L9', towerName + '-L10', towerName + '-最大值']
        self.towerTab_basicAttributeTableWidget.setColumnCount(len(basicAttHeader))
        self.towerTab_basicAttributeTableWidget.setHorizontalHeaderLabels(basicAttHeader)
        self.towerTab_basicAttributeTableWidget.setRowCount(12)
        self.towerTab_basicAttributeTableWidget.setVerticalHeaderLabels(verticalHeader)

        for i in range(len(basicAttInfo)):
            for j in range(len(basicAttInfo[i])):
                item = QTableWidgetItem(str(basicAttInfo[i][j]))
                self.towerTab_basicAttributeTableWidget.setItem(j, i, item)

        self.towerTab_abilityTableWidget.clear()
        verticalHeader = [towerName + '-初始值', towerName + '-增量', towerName + '-最大值']
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
        attributesEn = self.const.attributesEn
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
        print(towerName, rowHeader.replace("L", ""), attributesEn[columnHeader], value)
        item = TreeViewItem(
            modifyType="TCC",
            location=self.towerTab_basicAttributeTableWidget,
            mapto=self.towerTab_basicAttributeTableWidgetInfo,
            keys=(towerName, col, row),
            col = col,
            row = row,
            colHeader=columnHeader,
            rowHeader=rowHeader,
            oldValue=self.towerTab_basicAttributeTableWidgetInfo[towerName][col][row],
            newValue=value,
        )
        self.treeViewManager.addTreeItem(item)
        # 修改数据
        self.towerTab_basicAttributeTableWidgetInfo[towerName][col][row] = value
