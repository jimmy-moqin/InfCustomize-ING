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
