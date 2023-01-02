import json
import logging
import os
import pickle as pkl
from typing import Any, Dict, List, Optional, Tuple, Union

from PyQt5 import QtCore
from PyQt5.QtWidgets import (QFileDialog, QHeaderView, QItemDelegate,
                             QMainWindow, QMessageBox, QTableWidgetItem)
from ui.modify import Ui_ModifyWindow


class logger(object):

    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        self.fh = logging.FileHandler('log.log', encoding='utf-8')
        self.fh.setLevel(logging.DEBUG)
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)


class EmptyDelegate(QItemDelegate):
    '''代理类，用于禁用表格编辑'''

    def __init__(self, parent):
        super(EmptyDelegate, self).__init__(parent)

    def createEditor(self, QWidget, QStyleOptionViewItem, QModelIndex):
        return None


class ListWidgetManager():
    '''ListWidget管理类'''

    def __init__(self, listWidget):
        self.listWidget = listWidget
        self.varList = []
        self.varValueDict = {}

    def add(self, var, value):
        '''添加变量名和变量值'''
        self.varList.append(var)
        self.varValueDict[var] = value
        item = self.string2listwidget(var, value, 25)
        self.listWidget.addItem(item)

    def clear(self):
        '''清空ListWidget'''
        self.listWidget.clear()
        self.varList = []
        self.varValueDict = {}
        print(self.varList)

    def remove(self, row):
        '''删除选中的变量'''
        var = self.varList[row]
        self.listWidget.takeItem(row)  # 删除原来的变量
        self.varList.remove(var)  # 在列表中删除
        self.varValueDict.pop(var)  # 在字典中删除
        print(self.varList)

    def string2listwidget(self, var, value, lenth=20):
        '''该格式化函数,用于将修改后的变量名和变量值格式化地显示在Listwidget中'''
        if var == '': return
        if value == '': return
        if len(var) >= lenth:
            per = lenth - 6
            pre_var = var[:per]
            suf_var = var[-3:]
            var = pre_var + '...' + suf_var
        else:
            var = var.rjust(lenth, ' ')

        return "{} -> {}".format(var, value)

    def update(self, var, value):
        '''更新变量'''
        if var not in self.varList:

            self.add(var, value)
        else:
            row = self.varList.index(var)
            self.listWidget.takeItem(row)  # 删除原来的变量
            self.varList.remove(var)  # 在列表中删除
            self.varValueDict.pop(var)  # 在字典中删除
            self.add(var, value)  # 添加新的变量
        print(self.varList)

    def getvar(self, row):
        '''获取变量名'''
        return self.varList[row]

    def output(self, path):
        '''输出变量值'''
        with open(path, 'w') as f:
            for var, value in self.varValueDict.items():
                f.write('{}\n'.format(self.string2listwidget(var, value, 25)))


class TableWidgetManager():
    '''TableWidget管理类'''

    def __init__(self, tableWidget):
        self.tableWidget = tableWidget

    def getCurrentVars(self):
        '''获取当前表格中的变量名'''
        varList = []
        for i in range(self.tableWidget.rowCount()):
            varList.append(self.tableWidget.item(i, 0).text().replace(" ", "_"))
        return varList

    def renderItemsFromDict(self, varValueDict):
        '''从字典中添加变量'''
        # 清空表格
        self.tableWidget.clearContents()
        # 设置表格行数
        self.tableWidget.setRowCount(len(varValueDict))

        i = 0
        for row in varValueDict:
            var = QTableWidgetItem(row.replace("_", " "))
            units = QTableWidgetItem(varValueDict[row]['units'])
            default = QTableWidgetItem(str(varValueDict[row]['default']))
            desc = QTableWidgetItem(varValueDict[row]['desc'])
            modify = QTableWidgetItem(str(varValueDict[row].get('modify', '')))

            self.tableWidget.setItem(i, 0, var)
            self.tableWidget.setItem(i, 1, desc)
            if units.text() == 'UNITS_PER_SECOND':
                units.setText('1单位/秒')
            elif units.text() == 'SECONDS':
                units.setText('秒')
            elif units.text() == 'PERCENTS':
                units.setText('百分比')
            elif units.text() == 'UNITS':
                units.setText('1单位')
            elif units.text() == 'BOOLEAN':
                units.setText('布尔值')
            self.tableWidget.setItem(i, 2, units)
            self.tableWidget.setItem(i, 3, default)
            self.tableWidget.setItem(i, 4, modify)
            i += 1


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

        # 获取当前路径
        self.currentPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.cachePath = os.path.join(self.currentPath, 'cache')
        # 默认文件路径
        self.defaultFilePath = os.path.join(self.currentPath, 'default')
        self.defaultGameValueFile = os.path.join(self.defaultFilePath, 'game-values.json')
        #

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

        # 绑定按钮动作
        self.basicTab_searchBtn.clicked.connect(self.searchBasicVar)
        self.basicTab_selectBtn.clicked.connect(self.selectBasicVar)
        self.basicTab_recallRecordBtn.clicked.connect(self.recallRecord)
        self.basicTab_resetModifyBtn.clicked.connect(self.resetRecord)
        self.basicTab_exportRecordBtn.clicked.connect(self.exportRecord)
        self.basicTab_outputBtn.clicked.connect(self.outputFile)
        self.basicTab_applyBtn.clicked.connect(self.applyFile)

        # 绑定ComboBox动作
        self.basicTab_selectComboBox_1.activated.connect(self.selectChange)

        # 绑定TableWidget动作
        self.basicTab_tableWidget.cellChanged.connect(self.valueModify)

        # 设置表格头部自适应缩放
        self.basicTab_tableWidget.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        self.basicTab_tableWidget.verticalHeader().setHidden(True)
        # 设置表格自动换行
        self.basicTab_tableWidget.setWordWrap(True)
        # 设置表格前四列不可编辑
        for i in range(0, 4):
            self.basicTab_tableWidget.setItemDelegateForColumn(i, EmptyDelegate(self))

    def loadGamePath(self):
        '''载入游戏路径'''
        print('载入游戏路径')
        self.gamePath = QFileDialog.getExistingDirectory(
            self, "选取文件夹", "G:\SteamLibrary\steamapps\common\Infinitode 2") + '/'

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
                        self, '警告',
                        "在当前游戏路径的 res 文件夹下未找到 {} 文件\n请重新选择游戏安装路径，或使用 '载入资源文件' 手动选择 res 文件夹"
                        .format(file), QMessageBox.Yes)
                    break
            # 如果目标文件都存在，则载入文件路径
            else:
                self.achievementsFile = os.path.join(self.resource, resourceFileList[0])
                self.gameValueFile = os.path.join(self.resource, resourceFileList[1])
                self.towerEnemyAttackMatrixFile = os.path.join(self.resource,
                                                               resourceFileList[2])
                self.towerEnemyDamageMatrixFile = os.path.join(self.resource,
                                                               resourceFileList[3])
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

        # 如果不存在res文件夹
        else:
            self.logger.error('未找到res文件夹')
            QMessageBox.warning(
                self, '警告',
                "在当前游戏路径 {} 未找到 res 文件夹\n请重新选择游戏安装路径，或使用 '载入资源文件' 手动选择 res 文件夹".format(
                    self.gamePath), QMessageBox.Yes)
            return 0

    def loadResourceFile(self):
        '''载入资源文件'''
        print('载入资源文件')
        self.resource = QFileDialog.getExistingDirectory(
            self, "选取文件夹", "G:\SteamLibrary\steamapps\common\Infinitode 2")
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
                QMessageBox.warning(self, '警告',
                                    "在当前资源路径的 res 文件夹下未找到 {} 文件\n请重新选择资源路径".format(file),
                                    QMessageBox.Yes)
                return 0
        # 如果目标文件都存在，则载入文件路径
        else:
            self.achievementsFile = os.path.join(self.resource, resourceFileList[0])
            self.gameValueFile = os.path.join(self.resource, resourceFileList[1])
            self.towerEnemyAttackMatrixFile = os.path.join(self.resource,
                                                           resourceFileList[2])
            self.towerEnemyDamageMatrixFile = os.path.join(self.resource,
                                                           resourceFileList[3])
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
                self.gameValueFileContent[var]['desc'] = defaultGameValueFileContent[var][
                    'desc']
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
                    if (searchKeyWord
                            in var) or (searchKeyWord
                                        in self.gameValueFileContent[var]['desc']):
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
        elif select_1 == '':
            self.basicTab_selectComboBox_2.clear()
            self.basicTab_selectComboBox_2.currentText = ''

    def selectBasicVar(self):
        select = self.basicTab_selectComboBox_2.currentText()
        selectKeywordDict = {
            '': '',
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
        choose = QMessageBox.information(self, '提示', '重置修改记录后，所有修改将不可恢复',
                                         QMessageBox.Ok | QMessageBox.Cancel)
        if choose == QMessageBox.Ok:
            # 获取当前表格中显示的所有变量
            currentTableVars = self.tableWidgetManager.getCurrentVars()
            for var in self.listWidgetManager.varList:
                self.gameValueFileContent[var]['modify'] = ''
                if var in currentTableVars:
                    self.basicTab_tableWidget.item(currentTableVars.index(var),
                                                   4).setText('')

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
        QMessageBox.warning(self, '警告', '覆盖文件后，所有修改将不可恢复', QMessageBox.Ok, QMessageBox.Cancel)
        if QMessageBox.Ok:
            path = os.path.join(self.gamePath,"res/" 'game-values.json')
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
