from PyQt5.QtGui import QFont


class UniqueFont(QFont):
    '''字体管理类'''

    def __init__(self):
        super(UniqueFont, self).__init__()

    def Bold(self, size=10):
        boldFont = QFont()
        boldFont.setBold(True)
        boldFont.setPointSize(size)
        return boldFont

