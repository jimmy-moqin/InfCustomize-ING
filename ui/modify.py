# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modify.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ModifyWindow(object):
    def setupUi(self, ModifyWindow):
        ModifyWindow.setObjectName("ModifyWindow")
        ModifyWindow.resize(1294, 765)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ModifyWindow.sizePolicy().hasHeightForWidth())
        ModifyWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        ModifyWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ModifyWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.basicTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.basicTab.sizePolicy().hasHeightForWidth())
        self.basicTab.setSizePolicy(sizePolicy)
        self.basicTab.setObjectName("basicTab")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.basicTab)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.basicTab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.basicTab_searchLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.basicTab_searchLineEdit.setObjectName("basicTab_searchLineEdit")
        self.horizontalLayout_3.addWidget(self.basicTab_searchLineEdit)
        self.basicTab_searchBtn = QtWidgets.QPushButton(self.groupBox)
        self.basicTab_searchBtn.setObjectName("basicTab_searchBtn")
        self.horizontalLayout_3.addWidget(self.basicTab_searchBtn)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout_3.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.basicTab_selectComboBox_1 = QtWidgets.QComboBox(self.groupBox)
        self.basicTab_selectComboBox_1.setObjectName("basicTab_selectComboBox_1")
        self.basicTab_selectComboBox_1.addItem("")
        self.basicTab_selectComboBox_1.addItem("")
        self.basicTab_selectComboBox_1.addItem("")
        self.horizontalLayout_2.addWidget(self.basicTab_selectComboBox_1)
        self.basicTab_selectComboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.basicTab_selectComboBox_2.setObjectName("basicTab_selectComboBox_2")
        self.horizontalLayout_2.addWidget(self.basicTab_selectComboBox_2)
        self.basicTab_selectBtn = QtWidgets.QPushButton(self.groupBox)
        self.basicTab_selectBtn.setObjectName("basicTab_selectBtn")
        self.horizontalLayout_2.addWidget(self.basicTab_selectBtn)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 4)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.basicTab_tableWidget = QtWidgets.QTableWidget(self.basicTab)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.basicTab_tableWidget.setFont(font)
        self.basicTab_tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.basicTab_tableWidget.setObjectName("basicTab_tableWidget")
        self.basicTab_tableWidget.setColumnCount(5)
        self.basicTab_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.basicTab_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.basicTab_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.basicTab_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.basicTab_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.basicTab_tableWidget.setHorizontalHeaderItem(4, item)
        self.basicTab_tableWidget.horizontalHeader().setVisible(True)
        self.basicTab_tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.basicTab_tableWidget.verticalHeader().setDefaultSectionSize(45)
        self.basicTab_tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.verticalLayout_3.addWidget(self.basicTab_tableWidget)
        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 8)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.basicTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.basicTab_initFileLineEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.basicTab_initFileLineEdit.setObjectName("basicTab_initFileLineEdit")
        self.horizontalLayout_6.addWidget(self.basicTab_initFileLineEdit)
        self.horizontalLayout_6.setStretch(0, 8)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.basicTab)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.basicTab_modifyRecordListWidget = QtWidgets.QListWidget(self.groupBox_4)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.basicTab_modifyRecordListWidget.setFont(font)
        self.basicTab_modifyRecordListWidget.setObjectName("basicTab_modifyRecordListWidget")
        self.verticalLayout_6.addWidget(self.basicTab_modifyRecordListWidget)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.basicTab_recallRecordBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.basicTab_recallRecordBtn.setObjectName("basicTab_recallRecordBtn")
        self.horizontalLayout_7.addWidget(self.basicTab_recallRecordBtn)
        self.basicTab_resetModifyBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.basicTab_resetModifyBtn.setObjectName("basicTab_resetModifyBtn")
        self.horizontalLayout_7.addWidget(self.basicTab_resetModifyBtn)
        self.basicTab_exportRecordBtn = QtWidgets.QPushButton(self.groupBox_4)
        self.basicTab_exportRecordBtn.setObjectName("basicTab_exportRecordBtn")
        self.horizontalLayout_7.addWidget(self.basicTab_exportRecordBtn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_3 = QtWidgets.QGroupBox(self.basicTab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.basicTab_applyBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.basicTab_applyBtn.setObjectName("basicTab_applyBtn")
        self.horizontalLayout_5.addWidget(self.basicTab_applyBtn)
        self.basicTab_outputBtn = QtWidgets.QPushButton(self.groupBox_3)
        self.basicTab_outputBtn.setObjectName("basicTab_outputBtn")
        self.horizontalLayout_5.addWidget(self.basicTab_outputBtn)
        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 7)
        self.verticalLayout_2.setStretch(2, 2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 3)
        self.tabWidget.addTab(self.basicTab, "")
        self.towerTab = QtWidgets.QWidget()
        self.towerTab.setObjectName("towerTab")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.towerTab)
        self.horizontalLayout_8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_8.setContentsMargins(11, -1, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.leftTagsScrollArea = QtWidgets.QScrollArea(self.towerTab)
        self.leftTagsScrollArea.setStyleSheet("QScrollBar {height:0px;}\n"
"QScrollBar {width:0px;}\n"
"")
        self.leftTagsScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.leftTagsScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.leftTagsScrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.leftTagsScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.leftTagsScrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.leftTagsScrollArea.setWidgetResizable(True)
        self.leftTagsScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.leftTagsScrollArea.setObjectName("leftTagsScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -206, 52, 894))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.towerTab_tagWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.towerTab_tagWidget.setObjectName("towerTab_tagWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.towerTab_tagWidget)
        self.verticalLayout_7.setContentsMargins(3, 5, 0, 5)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.towerTab_basicTag = Tag(self.towerTab_tagWidget)
        self.towerTab_basicTag.setMinimumSize(QtCore.QSize(49, 49))
        self.towerTab_basicTag.setMaximumSize(QtCore.QSize(49, 49))
        self.towerTab_basicTag.setStyleSheet("QLabel:hover{\n"
"    border-image:url(:/tower_c/tower_48_color/TOWER_BASIC.png)\n"
"}\n"
"QLabel{\n"
"    border-image: url(:/tower_g/tower_48_grey/TOWER_BASIC_1.png);\n"
"}")
        self.towerTab_basicTag.setText("")
        self.towerTab_basicTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_basicTag.setObjectName("towerTab_basicTag")
        self.verticalLayout_7.addWidget(self.towerTab_basicTag)
        self.towerTab_sniperTag = Tag(self.towerTab_tagWidget)
        self.towerTab_sniperTag.setMinimumSize(QtCore.QSize(49, 43))
        self.towerTab_sniperTag.setMaximumSize(QtCore.QSize(49, 43))
        self.towerTab_sniperTag.setStyleSheet("QLabel:hover{\n"
"    border-image:url(:/tower_c/tower_48_color/TOWER_SNIPER.png)\n"
"}\n"
"QLabel{\n"
"    border-image: url(:/tower_g/tower_48_grey/TOWER_SNIPER_1.png);\n"
"}")
        self.towerTab_sniperTag.setText("")
        self.towerTab_sniperTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_sniperTag.setObjectName("towerTab_sniperTag")
        self.verticalLayout_7.addWidget(self.towerTab_sniperTag)
        self.towerTab_cannonTag = Tag(self.towerTab_tagWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(49)
        sizePolicy.setVerticalStretch(49)
        sizePolicy.setHeightForWidth(self.towerTab_cannonTag.sizePolicy().hasHeightForWidth())
        self.towerTab_cannonTag.setSizePolicy(sizePolicy)
        self.towerTab_cannonTag.setMinimumSize(QtCore.QSize(49, 47))
        self.towerTab_cannonTag.setMaximumSize(QtCore.QSize(49, 47))
        self.towerTab_cannonTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_CANNON.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_CANNON_1.png);}")
        self.towerTab_cannonTag.setText("")
        self.towerTab_cannonTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_cannonTag.setObjectName("towerTab_cannonTag")
        self.verticalLayout_7.addWidget(self.towerTab_cannonTag)
        self.towerTab_freezingTag = Tag(self.towerTab_tagWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.towerTab_freezingTag.sizePolicy().hasHeightForWidth())
        self.towerTab_freezingTag.setSizePolicy(sizePolicy)
        self.towerTab_freezingTag.setMinimumSize(QtCore.QSize(49, 49))
        self.towerTab_freezingTag.setMaximumSize(QtCore.QSize(49, 49))
        self.towerTab_freezingTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_FREEZING.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_FREEZING_1.png);}")
        self.towerTab_freezingTag.setText("")
        self.towerTab_freezingTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_freezingTag.setObjectName("towerTab_freezingTag")
        self.verticalLayout_7.addWidget(self.towerTab_freezingTag)
        self.towerTab_airTag = Tag(self.towerTab_tagWidget)
        self.towerTab_airTag.setMinimumSize(QtCore.QSize(49, 43))
        self.towerTab_airTag.setMaximumSize(QtCore.QSize(49, 43))
        self.towerTab_airTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_AIR.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_AIR_1.png);}")
        self.towerTab_airTag.setText("")
        self.towerTab_airTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_airTag.setObjectName("towerTab_airTag")
        self.verticalLayout_7.addWidget(self.towerTab_airTag)
        self.towerTab_splashTag = Tag(self.towerTab_tagWidget)
        self.towerTab_splashTag.setMinimumSize(QtCore.QSize(49, 52))
        self.towerTab_splashTag.setMaximumSize(QtCore.QSize(49, 52))
        self.towerTab_splashTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_SPLASH.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_SPLASH_1.png);}")
        self.towerTab_splashTag.setText("")
        self.towerTab_splashTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_splashTag.setObjectName("towerTab_splashTag")
        self.verticalLayout_7.addWidget(self.towerTab_splashTag)
        self.towerTab_blastTag = Tag(self.towerTab_tagWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.towerTab_blastTag.sizePolicy().hasHeightForWidth())
        self.towerTab_blastTag.setSizePolicy(sizePolicy)
        self.towerTab_blastTag.setMinimumSize(QtCore.QSize(49, 47))
        self.towerTab_blastTag.setMaximumSize(QtCore.QSize(49, 47))
        self.towerTab_blastTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_BLAST.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_BLAST_1.png);}")
        self.towerTab_blastTag.setText("")
        self.towerTab_blastTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_blastTag.setObjectName("towerTab_blastTag")
        self.verticalLayout_7.addWidget(self.towerTab_blastTag)
        self.towerTab_multishotTag = Tag(self.towerTab_tagWidget)
        self.towerTab_multishotTag.setMinimumSize(QtCore.QSize(49, 43))
        self.towerTab_multishotTag.setMaximumSize(QtCore.QSize(49, 43))
        self.towerTab_multishotTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_MULTISHOT.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_MULTISHOT_1.png);}")
        self.towerTab_multishotTag.setText("")
        self.towerTab_multishotTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_multishotTag.setObjectName("towerTab_multishotTag")
        self.verticalLayout_7.addWidget(self.towerTab_multishotTag)
        self.towerTab_minigunTag = Tag(self.towerTab_tagWidget)
        self.towerTab_minigunTag.setMinimumSize(QtCore.QSize(49, 49))
        self.towerTab_minigunTag.setMaximumSize(QtCore.QSize(49, 49))
        self.towerTab_minigunTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_MINIGUN.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_MINIGUN_1.png);}")
        self.towerTab_minigunTag.setText("")
        self.towerTab_minigunTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_minigunTag.setObjectName("towerTab_minigunTag")
        self.verticalLayout_7.addWidget(self.towerTab_minigunTag)
        self.towerTab_venomTag = Tag(self.towerTab_tagWidget)
        self.towerTab_venomTag.setMinimumSize(QtCore.QSize(49, 42))
        self.towerTab_venomTag.setMaximumSize(QtCore.QSize(49, 42))
        self.towerTab_venomTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_VENOM.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_VENOM_1.png);}")
        self.towerTab_venomTag.setText("")
        self.towerTab_venomTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_venomTag.setObjectName("towerTab_venomTag")
        self.verticalLayout_7.addWidget(self.towerTab_venomTag)
        self.towerTab_teslaTag = Tag(self.towerTab_tagWidget)
        self.towerTab_teslaTag.setMinimumSize(QtCore.QSize(49, 47))
        self.towerTab_teslaTag.setMaximumSize(QtCore.QSize(49, 47))
        self.towerTab_teslaTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_TESLA.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_TESLA_1.png);}")
        self.towerTab_teslaTag.setText("")
        self.towerTab_teslaTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_teslaTag.setObjectName("towerTab_teslaTag")
        self.verticalLayout_7.addWidget(self.towerTab_teslaTag)
        self.towerTab_missileTag = Tag(self.towerTab_tagWidget)
        self.towerTab_missileTag.setMinimumSize(QtCore.QSize(49, 29))
        self.towerTab_missileTag.setMaximumSize(QtCore.QSize(49, 29))
        self.towerTab_missileTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_MISSILE.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_MISSILE_1.png);}")
        self.towerTab_missileTag.setText("")
        self.towerTab_missileTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_missileTag.setObjectName("towerTab_missileTag")
        self.verticalLayout_7.addWidget(self.towerTab_missileTag)
        self.towerTab_flameTag = Tag(self.towerTab_tagWidget)
        self.towerTab_flameTag.setMinimumSize(QtCore.QSize(49, 47))
        self.towerTab_flameTag.setMaximumSize(QtCore.QSize(49, 47))
        self.towerTab_flameTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_FLAME.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_FLAME_1.png);}")
        self.towerTab_flameTag.setText("")
        self.towerTab_flameTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_flameTag.setObjectName("towerTab_flameTag")
        self.verticalLayout_7.addWidget(self.towerTab_flameTag)
        self.towerTab_laserTag = Tag(self.towerTab_tagWidget)
        self.towerTab_laserTag.setMinimumSize(QtCore.QSize(49, 49))
        self.towerTab_laserTag.setMaximumSize(QtCore.QSize(49, 49))
        self.towerTab_laserTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_LASER.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_LASER_1.png);}")
        self.towerTab_laserTag.setText("")
        self.towerTab_laserTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_laserTag.setObjectName("towerTab_laserTag")
        self.verticalLayout_7.addWidget(self.towerTab_laserTag)
        self.towerTab_gaussTag = Tag(self.towerTab_tagWidget)
        self.towerTab_gaussTag.setMinimumSize(QtCore.QSize(49, 49))
        self.towerTab_gaussTag.setMaximumSize(QtCore.QSize(49, 49))
        self.towerTab_gaussTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_GAUSS.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_GAUSS_1.png);}")
        self.towerTab_gaussTag.setText("")
        self.towerTab_gaussTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_gaussTag.setObjectName("towerTab_gaussTag")
        self.verticalLayout_7.addWidget(self.towerTab_gaussTag)
        self.towerTab_crusherTag = Tag(self.towerTab_tagWidget)
        self.towerTab_crusherTag.setMinimumSize(QtCore.QSize(49, 49))
        self.towerTab_crusherTag.setMaximumSize(QtCore.QSize(49, 49))
        self.towerTab_crusherTag.setStyleSheet("QLabel:hover{border-image:url(:/tower_c/tower_48_color/TOWER_CRUSHER.png)}QLabel{border-image: url(:/tower_g/tower_48_grey/TOWER_CRUSHER_1.png);}")
        self.towerTab_crusherTag.setText("")
        self.towerTab_crusherTag.setAlignment(QtCore.Qt.AlignCenter)
        self.towerTab_crusherTag.setObjectName("towerTab_crusherTag")
        self.verticalLayout_7.addWidget(self.towerTab_crusherTag)
        self.horizontalLayout_9.addWidget(self.towerTab_tagWidget)
        self.leftTagsScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_8.addWidget(self.leftTagsScrollArea)
        self.mainScrollArea = QtWidgets.QScrollArea(self.towerTab)
        self.mainScrollArea.setWidgetResizable(True)
        self.mainScrollArea.setObjectName("mainScrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 871, 651))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.towerTab_basicAttributeTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.towerTab_basicAttributeTable.setShowGrid(False)
        self.towerTab_basicAttributeTable.setObjectName("towerTab_basicAttributeTable")
        self.towerTab_basicAttributeTable.setColumnCount(0)
        self.towerTab_basicAttributeTable.setRowCount(0)
        self.towerTab_basicAttributeTable.horizontalHeader().setVisible(False)
        self.verticalLayout_8.addWidget(self.towerTab_basicAttributeTable)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.towerTab_damageTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.towerTab_damageTable.setObjectName("towerTab_damageTable")
        self.towerTab_damageTable.setColumnCount(0)
        self.towerTab_damageTable.setRowCount(0)
        self.verticalLayout_8.addWidget(self.towerTab_damageTable)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_8.addWidget(self.label_6)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(0)
        self.tableWidget_3.setRowCount(0)
        self.verticalLayout_8.addWidget(self.tableWidget_3)
        self.verticalLayout_8.setStretch(1, 9)
        self.verticalLayout_8.setStretch(3, 5)
        self.verticalLayout_8.setStretch(5, 4)
        self.mainScrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_8.addWidget(self.mainScrollArea)
        self.groupBox_6 = QtWidgets.QGroupBox(self.towerTab)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.basicTab_recallRecordBtn_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.basicTab_recallRecordBtn_2.setObjectName("basicTab_recallRecordBtn_2")
        self.horizontalLayout_11.addWidget(self.basicTab_recallRecordBtn_2)
        self.basicTab_resetModifyBtn_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.basicTab_resetModifyBtn_2.setObjectName("basicTab_resetModifyBtn_2")
        self.horizontalLayout_11.addWidget(self.basicTab_resetModifyBtn_2)
        self.basicTab_exportRecordBtn_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.basicTab_exportRecordBtn_2.setObjectName("basicTab_exportRecordBtn_2")
        self.horizontalLayout_11.addWidget(self.basicTab_exportRecordBtn_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_11)
        self.basicTab_modifyRecordListWidget_2 = QtWidgets.QListWidget(self.groupBox_6)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.basicTab_modifyRecordListWidget_2.setFont(font)
        self.basicTab_modifyRecordListWidget_2.setObjectName("basicTab_modifyRecordListWidget_2")
        self.verticalLayout_11.addWidget(self.basicTab_modifyRecordListWidget_2)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_12.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_12.addWidget(self.pushButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_8.addWidget(self.groupBox_6)
        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 17)
        self.tabWidget.addTab(self.towerTab, "")
        self.levelTab = QtWidgets.QWidget()
        self.levelTab.setObjectName("levelTab")
        self.tabWidget.addTab(self.levelTab, "")
        self.researchTab = QtWidgets.QWidget()
        self.researchTab.setObjectName("researchTab")
        self.tabWidget.addTab(self.researchTab, "")
        self.achievementTab = QtWidgets.QWidget()
        self.achievementTab.setObjectName("achievementTab")
        self.tabWidget.addTab(self.achievementTab, "")
        self.statTab = QtWidgets.QWidget()
        self.statTab.setObjectName("statTab")
        self.tabWidget.addTab(self.statTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        ModifyWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModifyWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1294, 24))
        self.menubar.setObjectName("menubar")
        self.menuLoad = QtWidgets.QMenu(self.menubar)
        self.menuLoad.setObjectName("menuLoad")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        ModifyWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModifyWindow)
        self.statusbar.setObjectName("statusbar")
        ModifyWindow.setStatusBar(self.statusbar)
        self.actionLoad_game_path = QtWidgets.QAction(ModifyWindow)
        self.actionLoad_game_path.setObjectName("actionLoad_game_path")
        self.actionLoad_archive = QtWidgets.QAction(ModifyWindow)
        self.actionLoad_archive.setObjectName("actionLoad_archive")
        self.actionLoad_resource = QtWidgets.QAction(ModifyWindow)
        self.actionLoad_resource.setObjectName("actionLoad_resource")
        self.actionLoad_custom_conf = QtWidgets.QAction(ModifyWindow)
        self.actionLoad_custom_conf.setObjectName("actionLoad_custom_conf")
        self.actionSave_modify = QtWidgets.QAction(ModifyWindow)
        self.actionSave_modify.setObjectName("actionSave_modify")
        self.actionSave_As = QtWidgets.QAction(ModifyWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionExit = QtWidgets.QAction(ModifyWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionGenerate_backup = QtWidgets.QAction(ModifyWindow)
        self.actionGenerate_backup.setObjectName("actionGenerate_backup")
        self.actionRestore_backup = QtWidgets.QAction(ModifyWindow)
        self.actionRestore_backup.setObjectName("actionRestore_backup")
        self.actionBackup_list = QtWidgets.QAction(ModifyWindow)
        self.actionBackup_list.setObjectName("actionBackup_list")
        self.actionVersion_information = QtWidgets.QAction(ModifyWindow)
        self.actionVersion_information.setObjectName("actionVersion_information")
        self.actionAuthor = QtWidgets.QAction(ModifyWindow)
        self.actionAuthor.setObjectName("actionAuthor")
        self.actionReport_bugs = QtWidgets.QAction(ModifyWindow)
        self.actionReport_bugs.setObjectName("actionReport_bugs")
        self.menuLoad.addAction(self.actionLoad_game_path)
        self.menuLoad.addAction(self.actionLoad_archive)
        self.menuLoad.addAction(self.actionLoad_resource)
        self.menuLoad.addSeparator()
        self.menuLoad.addAction(self.actionLoad_custom_conf)
        self.menuLoad.addAction(self.actionSave_modify)
        self.menuLoad.addAction(self.actionSave_As)
        self.menuLoad.addSeparator()
        self.menuLoad.addAction(self.actionExit)
        self.menu.addAction(self.actionGenerate_backup)
        self.menu.addAction(self.actionRestore_backup)
        self.menu.addSeparator()
        self.menu.addAction(self.actionBackup_list)
        self.menu_2.addAction(self.actionVersion_information)
        self.menu_2.addAction(self.actionAuthor)
        self.menu_2.addAction(self.actionReport_bugs)
        self.menubar.addAction(self.menuLoad.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(ModifyWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ModifyWindow)

    def retranslateUi(self, ModifyWindow):
        _translate = QtCore.QCoreApplication.translate
        ModifyWindow.setWindowTitle(_translate("ModifyWindow", "Infinitode2修改器"))
        self.groupBox.setTitle(_translate("ModifyWindow", "搜索/筛选"))
        self.label_2.setText(_translate("ModifyWindow", "搜索"))
        self.basicTab_searchBtn.setText(_translate("ModifyWindow", "搜索"))
        self.label_3.setText(_translate("ModifyWindow", "筛选"))
        self.basicTab_selectComboBox_1.setItemText(0, _translate("ModifyWindow", "塔属性"))
        self.basicTab_selectComboBox_1.setItemText(1, _translate("ModifyWindow", "技能"))
        self.basicTab_selectComboBox_1.setItemText(2, _translate("ModifyWindow", "杂项"))
        self.basicTab_selectBtn.setText(_translate("ModifyWindow", "筛选"))
        self.basicTab_tableWidget.setSortingEnabled(False)
        item = self.basicTab_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ModifyWindow", "变量"))
        item = self.basicTab_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ModifyWindow", "含义"))
        item = self.basicTab_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ModifyWindow", "类型"))
        item = self.basicTab_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ModifyWindow", "默认值"))
        item = self.basicTab_tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ModifyWindow", "修改值"))
        self.groupBox_2.setTitle(_translate("ModifyWindow", "导入-初始基础变量文件路径"))
        self.groupBox_4.setTitle(_translate("ModifyWindow", "修改记录"))
        self.basicTab_modifyRecordListWidget.setSortingEnabled(False)
        self.basicTab_recallRecordBtn.setText(_translate("ModifyWindow", "撤回修改"))
        self.basicTab_resetModifyBtn.setText(_translate("ModifyWindow", "重置修改"))
        self.basicTab_exportRecordBtn.setText(_translate("ModifyWindow", "导出记录"))
        self.groupBox_3.setTitle(_translate("ModifyWindow", "导出"))
        self.label.setText(_translate("ModifyWindow", "<html><head/><body><p>可以选择直接覆盖原有 <span style=\" text-decoration: underline;\">game-value.josn</span> 文件</p><p>也可以导出到其他目录</p></body></html>"))
        self.basicTab_applyBtn.setText(_translate("ModifyWindow", "应用/覆盖"))
        self.basicTab_outputBtn.setText(_translate("ModifyWindow", "导出"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.basicTab), _translate("ModifyWindow", "基础变量修改"))
        self.label_4.setText(_translate("ModifyWindow", "基础属性"))
        self.towerTab_basicAttributeTable.setSortingEnabled(False)
        self.label_5.setText(_translate("ModifyWindow", "伤害倍率"))
        self.label_6.setText(_translate("ModifyWindow", "特殊能力"))
        self.groupBox_6.setTitle(_translate("ModifyWindow", "修改记录"))
        self.basicTab_recallRecordBtn_2.setText(_translate("ModifyWindow", "撤回修改"))
        self.basicTab_resetModifyBtn_2.setText(_translate("ModifyWindow", "重置修改"))
        self.basicTab_exportRecordBtn_2.setText(_translate("ModifyWindow", "导出记录"))
        self.basicTab_modifyRecordListWidget_2.setSortingEnabled(False)
        self.pushButton_2.setText(_translate("ModifyWindow", "导出"))
        self.pushButton.setText(_translate("ModifyWindow", "应用/覆盖"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.towerTab), _translate("ModifyWindow", "防御塔属性修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.levelTab), _translate("ModifyWindow", "关卡任务修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.researchTab), _translate("ModifyWindow", "研究修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.achievementTab), _translate("ModifyWindow", "成就修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.statTab), _translate("ModifyWindow", "统计数据修改"))
        self.menuLoad.setTitle(_translate("ModifyWindow", "文件"))
        self.menu.setTitle(_translate("ModifyWindow", "备份"))
        self.menu_2.setTitle(_translate("ModifyWindow", "关于"))
        self.actionLoad_game_path.setText(_translate("ModifyWindow", "载入游戏路径"))
        self.actionLoad_archive.setText(_translate("ModifyWindow", "载入存档"))
        self.actionLoad_resource.setText(_translate("ModifyWindow", "载入资源文件"))
        self.actionLoad_custom_conf.setText(_translate("ModifyWindow", "打开修改文件"))
        self.actionSave_modify.setText(_translate("ModifyWindow", "保存修改文件"))
        self.actionSave_As.setText(_translate("ModifyWindow", "另存为"))
        self.actionExit.setText(_translate("ModifyWindow", "退出"))
        self.actionGenerate_backup.setText(_translate("ModifyWindow", "生成备份"))
        self.actionRestore_backup.setText(_translate("ModifyWindow", "恢复备份"))
        self.actionBackup_list.setText(_translate("ModifyWindow", "管理备份"))
        self.actionVersion_information.setText(_translate("ModifyWindow", "版本信息"))
        self.actionAuthor.setText(_translate("ModifyWindow", "作者信息"))
        self.actionReport_bugs.setText(_translate("ModifyWindow", "报告错误"))
import img.tower_rc
from widgets.tag import Tag
