from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel


class Tag(QLabel):
    # 自定义信号, 注意信号必须为类属性
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(Tag, self).__init__(parent)

    def mouseReleaseEvent(self, QMouseEvent):
        self.clicked.emit()

