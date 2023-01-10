from typing import Dict, List, Tuple

from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class TableWidgetManager():
    '''TableWidget管理类'''

    def __init__(self, tableWidget:QTableWidget):
        self.tableWidget = tableWidget
        self.horizontalHeaders = self.tableWidget.horizontalHeader()
        self.verticalHeaders = self.tableWidget.verticalHeader()
        self.cols = 0
        self.rows = 0

    def setHorizontalHeaders(self, labels:List):
        '''设置表头'''
        self.tableWidget.setColumnCount(len(labels))
        self.cols = len(labels)
        self.tableWidget.setHorizontalHeaderLabels(labels)
    
    def setVerticalHeaders(self, labels:List):
        '''设置行头'''
        self.tableWidget.setRowCount(len(labels))
        self.rows = len(labels)
        self.tableWidget.setVerticalHeaderLabels(labels)

    def render(self, data:List[List[str]]):
        '''渲染表格'''
        self.rows = len(data)
        if self.rows != 0:
            self.cols = len(data[0])
            self.tableWidget.setRowCount(self.rows)
            for row in range(self.rows):
                for col in range(self.cols):
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        else:
            self.tableWidget.setRowCount(0)
    
    def getFirstColunm(self) -> List[str]:
        '''获取第一列数据'''
        data = []
        for row in range(self.rows):
            data.append(self.tableWidget.item(row, 0).text())
        return data

    