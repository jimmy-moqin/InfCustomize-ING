from PyQt5.QtWidgets import QApplication

from Bin.modifyMain import ModifyMain

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Ui_ModifyMain=ModifyMain()
    Ui_ModifyMain.show()#调用主窗口
    sys.exit(app.exec_())

