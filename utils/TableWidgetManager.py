from PyQt5.QtWidgets import QTableWidgetItem


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
