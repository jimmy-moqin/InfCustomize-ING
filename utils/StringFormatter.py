class StringFormatter:
    def __call__(self):
        return self.string2listwidget

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

# 实例化
StringFormatter = StringFormatter()
