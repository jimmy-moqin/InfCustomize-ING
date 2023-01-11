import random
from typing import Tuple

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableWidget, QTreeView


class TreeViewItem():

    def __init__(self, modifyType: str, location: QTableWidget, mapto: dict, keys: tuple, col: int, row: int, colHeader:str, rowHeader:str, oldValue: str, newValue: str):
        self.modifyType = modifyType
        self.location = location
        self.mapto = mapto
        self.keys = keys
        self.col = col
        self.row = row
        self.colHeader = colHeader
        self.rowHeader = rowHeader
        self.oldValue = oldValue
        self.newValue = newValue
        self.creatHeader()
        self.hash = hash(self.header)

    def creatHeader(self):
        self.header = "{}: {} pos[{},{}]".format(self.modifyType, self.location.objectName(), self.rowHeader, self.colHeader)


class TreeViewManager(object):

    def __init__(self, treeView: QTreeView) -> None:
        self.treeView = treeView
        self.itemsNum = 0
        self.itemsDict = {}
        self.itemsList = []
        self.itemsHashDict = {}

        # 绑定模型
        self.model = QStandardItemModel(0, 1, self.treeView)
        self.model.setHeaderData(0, Qt.Orientation.Horizontal, "修改记录")
        self.treeView.setModel(self.model)

    def addTreeItem(self, treeViewItem: TreeViewItem):
        '''添加树形视图中的item'''
        # 如果存在这个item，则添加子item
        if self.itemsDict.get(treeViewItem.hash, 0):
            row = self.itemsList.index(treeViewItem.header)
            item = self.model.item(row, 0)
            subItem = QStandardItem("{} -> {}".format(treeViewItem.oldValue, treeViewItem.newValue))
            item.appendRow(subItem)
            self.itemsDict[treeViewItem.hash].append((treeViewItem.oldValue, treeViewItem.newValue))

        else:
            # 如果不存在这个item,
            self.itemsDict[treeViewItem.hash] = []
            self.itemsList.append(treeViewItem.header)
            self.itemsHashDict[treeViewItem.hash] = treeViewItem

            self.model.insertRow(self.itemsNum)
            item = QStandardItem(treeViewItem.header)
            subItem = QStandardItem("{} -> {}".format(treeViewItem.oldValue, treeViewItem.newValue))
            item.appendRow(subItem)
            self.model.setItem(self.itemsNum, 0, item)

            self.itemsDict[treeViewItem.hash].append((treeViewItem.oldValue, treeViewItem.newValue))

        self.itemsNum = len(self.itemsDict)

    def removeTreeItem(self, parentRow: int, childRow: int) -> Tuple[str, QTableWidget, dict, tuple, int, int, str, str]:
        '''删除树形视图中的item'''
        itemHash = hash(self.itemsList[parentRow])
        loc: QTableWidget = self.itemsHashDict[itemHash].location
        col: int = self.itemsHashDict[itemHash].col
        row: int = self.itemsHashDict[itemHash].row
        colHeader = self.itemsHashDict[itemHash].colHeader
        rowHeader = self.itemsHashDict[itemHash].rowHeader
        mapto: dict = self.itemsHashDict[itemHash].mapto
        keys: tuple = self.itemsHashDict[itemHash].keys

        # 断开表格的信号连接
        loc.disconnect()  ###此处在管理器内断开了信号槽链接，一定要在调用后重连

        if childRow == -1:
            updateValue = self.itemsDict[itemHash][0][0]
            # 删除父item
            self.model.removeRow(parentRow)
            self.itemsDict.pop(itemHash)
            self.itemsHashDict.pop(itemHash)
            self.itemsList.remove(self.itemsList[parentRow])
            self.itemsNum = len(self.itemsDict)
            return updateValue, loc, mapto, keys, col, row, colHeader, rowHeader
        else:
            # 删除子item
            item = self.model.item(parentRow, 0)
            parentItem = self.itemsDict[itemHash]
            updateValue = parentItem[0][0]
            # 使用循环删除所选子项一下的所有项目，包括所选子项
            for i in range(len(parentItem) - 1, childRow - 1, -1):
                item.removeRow(i)
                parentItem.remove(parentItem[i])
                self.itemsNum = len(self.itemsDict)
            if len(parentItem) == 0:
                # 如果子item为空，则同时删除父item
                self.model.removeRow(parentRow)
                self.itemsDict.pop(itemHash)
                self.itemsList.remove(self.itemsList[parentRow])
                self.itemsNum = len(self.itemsDict)
                return updateValue, loc, mapto, keys, col, row, colHeader, rowHeader
            else:
                # 如果在删除子项后父项不为空，则返回最后一个子项的newvalue
                updateValue = parentItem[-1][-1]
                return updateValue, loc, mapto, keys, col, row, colHeader, rowHeader

    def output(self,path:str):
        '''导出修改记录'''
        with open(path, "w", encoding="utf-8") as f:
            for i in self.itemsList:
                f.write(i + "\n")
                for j in self.itemsDict[hash(i)]:
                    f.write("    {} -> {}\n".format(j[0], j[1]))
