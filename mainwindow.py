# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(373, 387)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lable_mTitle = QtWidgets.QLabel(self.tab)
        self.lable_mTitle.setObjectName("lable_mTitle")
        self.gridLayout_3.addWidget(self.lable_mTitle, 1, 0, 1, 1)
        self.lineEdit_mTitle = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_mTitle.setObjectName("lineEdit_mTitle")
        self.gridLayout_3.addWidget(self.lineEdit_mTitle, 1, 1, 1, 1)
        self.label_blurayName = QtWidgets.QLabel(self.tab)
        self.label_blurayName.setObjectName("label_blurayName")
        self.gridLayout_3.addWidget(self.label_blurayName, 0, 0, 1, 1)
        self.lineEdit_blurayName = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_blurayName.setReadOnly(True)
        self.lineEdit_blurayName.setObjectName("lineEdit_blurayName")
        self.gridLayout_3.addWidget(self.lineEdit_blurayName, 0, 1, 1, 1)
        self.getOpen_blurayName = QtWidgets.QToolButton(self.tab)
        self.getOpen_blurayName.setObjectName("getOpen_blurayName")
        self.gridLayout_3.addWidget(self.getOpen_blurayName, 0, 2, 1, 1)
        self.gridLayout_3.setRowMinimumHeight(0, 25)
        self.gridLayout_3.setRowMinimumHeight(1, 25)
        self.verticalLayout_3.addLayout(self.gridLayout_3)
        self.tableWidget_naming = QtWidgets.QTableWidget(self.tab)
        self.tableWidget_naming.setEnabled(False)
        self.tableWidget_naming.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_naming.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_naming.setRowCount(1)
        self.tableWidget_naming.setColumnCount(1)
        self.tableWidget_naming.setObjectName("tableWidget_naming")
        self.tableWidget_naming.horizontalHeader().setDefaultSectionSize(75)
        self.tableWidget_naming.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_naming.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_3.addWidget(self.tableWidget_naming)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_showCrop = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_showCrop.sizePolicy().hasHeightForWidth())
        self.pushButton_showCrop.setSizePolicy(sizePolicy)
        self.pushButton_showCrop.setObjectName("pushButton_showCrop")
        self.horizontalLayout_5.addWidget(self.pushButton_showCrop)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_saveTitle = QtWidgets.QPushButton(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_saveTitle.sizePolicy().hasHeightForWidth())
        self.pushButton_saveTitle.setSizePolicy(sizePolicy)
        self.pushButton_saveTitle.setObjectName("pushButton_saveTitle")
        self.horizontalLayout_5.addWidget(self.pushButton_saveTitle)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_mTitle = QtWidgets.QLabel(self.tab_2)
        self.label_mTitle.setObjectName("label_mTitle")
        self.gridLayout_4.addWidget(self.label_mTitle, 1, 0, 1, 1)
        self.label_blurayEnc = QtWidgets.QLabel(self.tab_2)
        self.label_blurayEnc.setObjectName("label_blurayEnc")
        self.gridLayout_4.addWidget(self.label_blurayEnc, 0, 0, 1, 1)
        self.getOpen_blurayEnc = QtWidgets.QToolButton(self.tab_2)
        self.getOpen_blurayEnc.setObjectName("getOpen_blurayEnc")
        self.gridLayout_4.addWidget(self.getOpen_blurayEnc, 0, 2, 1, 1)
        self.comboBox_mTitle = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_mTitle.setObjectName("comboBox_mTitle")
        self.gridLayout_4.addWidget(self.comboBox_mTitle, 1, 1, 1, 1)
        self.lineEdit_blurayEnc = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_blurayEnc.setReadOnly(True)
        self.lineEdit_blurayEnc.setObjectName("lineEdit_blurayEnc")
        self.gridLayout_4.addWidget(self.lineEdit_blurayEnc, 0, 1, 1, 1)
        self.pushButton_mrefresh = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_mrefresh.sizePolicy().hasHeightForWidth())
        self.pushButton_mrefresh.setSizePolicy(sizePolicy)
        self.pushButton_mrefresh.setObjectName("pushButton_mrefresh")
        self.gridLayout_4.addWidget(self.pushButton_mrefresh, 1, 2, 1, 1)
        self.gridLayout_4.setRowMinimumHeight(0, 25)
        self.gridLayout_4.setRowMinimumHeight(1, 25)
        self.verticalLayout_2.addLayout(self.gridLayout_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_5.setSpacing(6)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.progressbar_encoding = QtWidgets.QProgressBar(self.tab_2)
        self.progressbar_encoding.setProperty("value", 24)
        self.progressbar_encoding.setObjectName("progressbar_encoding")
        self.gridLayout_5.addWidget(self.progressbar_encoding, 0, 0, 1, 1)
        self.pushButton_startEncoding = QtWidgets.QPushButton(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_startEncoding.sizePolicy().hasHeightForWidth())
        self.pushButton_startEncoding.setSizePolicy(sizePolicy)
        self.pushButton_startEncoding.setObjectName("pushButton_startEncoding")
        self.gridLayout_5.addWidget(self.pushButton_startEncoding, 0, 1, 1, 1)
        self.label_encoding = QtWidgets.QLabel(self.tab_2)
        self.label_encoding.setObjectName("label_encoding")
        self.gridLayout_5.addWidget(self.label_encoding, 1, 0, 1, 1)
        self.label_progess = QtWidgets.QLabel(self.tab_2)
        self.label_progess.setObjectName("label_progess")
        self.gridLayout_5.addWidget(self.label_progess, 2, 0, 1, 1)
        self.gridLayout_5.setRowMinimumHeight(0, 25)
        self.gridLayout_5.setRowMinimumHeight(1, 15)
        self.gridLayout_5.setRowMinimumHeight(2, 15)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.gridLayout_2.setSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_ffmpeg = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_ffmpeg.setReadOnly(True)
        self.lineEdit_ffmpeg.setObjectName("lineEdit_ffmpeg")
        self.gridLayout_2.addWidget(self.lineEdit_ffmpeg, 0, 1, 1, 1)
        self.lineEdit_plexMovie = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_plexMovie.setReadOnly(True)
        self.lineEdit_plexMovie.setObjectName("lineEdit_plexMovie")
        self.gridLayout_2.addWidget(self.lineEdit_plexMovie, 1, 1, 1, 1)
        self.getOpen_plexMovie = QtWidgets.QToolButton(self.tab_3)
        self.getOpen_plexMovie.setObjectName("getOpen_plexMovie")
        self.gridLayout_2.addWidget(self.getOpen_plexMovie, 1, 2, 1, 1)
        self.getOpen_ffmpeg = QtWidgets.QToolButton(self.tab_3)
        self.getOpen_ffmpeg.setObjectName("getOpen_ffmpeg")
        self.gridLayout_2.addWidget(self.getOpen_ffmpeg, 0, 2, 1, 1)
        self.label_ffmpeg = QtWidgets.QLabel(self.tab_3)
        self.label_ffmpeg.setObjectName("label_ffmpeg")
        self.gridLayout_2.addWidget(self.label_ffmpeg, 0, 0, 1, 1)
        self.label_plex = QtWidgets.QLabel(self.tab_3)
        self.label_plex.setObjectName("label_plex")
        self.gridLayout_2.addWidget(self.label_plex, 1, 0, 1, 1)
        self.label_vlc = QtWidgets.QLabel(self.tab_3)
        self.label_vlc.setObjectName("label_vlc")
        self.gridLayout_2.addWidget(self.label_vlc, 3, 0, 1, 1)
        self.lineEdit_vlc = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_vlc.setReadOnly(True)
        self.lineEdit_vlc.setObjectName("lineEdit_vlc")
        self.gridLayout_2.addWidget(self.lineEdit_vlc, 3, 1, 1, 1)
        self.getOpen_vlc = QtWidgets.QToolButton(self.tab_3)
        self.getOpen_vlc.setObjectName("getOpen_vlc")
        self.gridLayout_2.addWidget(self.getOpen_vlc, 3, 2, 1, 1)
        self.lineEdit_plexSeries = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_plexSeries.setReadOnly(True)
        self.lineEdit_plexSeries.setObjectName("lineEdit_plexSeries")
        self.gridLayout_2.addWidget(self.lineEdit_plexSeries, 2, 1, 1, 1)
        self.getOpen_plexSeries = QtWidgets.QToolButton(self.tab_3)
        self.getOpen_plexSeries.setObjectName("getOpen_plexSeries")
        self.gridLayout_2.addWidget(self.getOpen_plexSeries, 2, 2, 1, 1)
        self.label_plexSeries = QtWidgets.QLabel(self.tab_3)
        self.label_plexSeries.setObjectName("label_plexSeries")
        self.gridLayout_2.addWidget(self.label_plexSeries, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_cancelOptions = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_cancelOptions.setObjectName("pushButton_cancelOptions")
        self.horizontalLayout_2.addWidget(self.pushButton_cancelOptions)
        self.pushButton_saveOptions = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_saveOptions.setObjectName("pushButton_saveOptions")
        self.horizontalLayout_2.addWidget(self.pushButton_saveOptions)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab_3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PlexConformer"))
        self.lable_mTitle.setText(_translate("MainWindow", "Movie-Title"))
        self.label_blurayName.setText(_translate("MainWindow", "BluRay-Location"))
        self.getOpen_blurayName.setText(_translate("MainWindow", "..."))
        self.pushButton_showCrop.setText(_translate("MainWindow", "Show Crop"))
        self.pushButton_saveTitle.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "naming"))
        self.label_mTitle.setText(_translate("MainWindow", "Movie-Title"))
        self.label_blurayEnc.setText(_translate("MainWindow", "BluRay-Location"))
        self.getOpen_blurayEnc.setText(_translate("MainWindow", "..."))
        self.pushButton_mrefresh.setText(_translate("MainWindow", "Refresh"))
        self.pushButton_startEncoding.setText(_translate("MainWindow", "Start Encoding"))
        self.label_encoding.setText(_translate("MainWindow", "Encoding: title0100.mkv"))
        self.label_progess.setText(_translate("MainWindow", "1/22"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "encoding"))
        self.getOpen_plexMovie.setText(_translate("MainWindow", "..."))
        self.getOpen_ffmpeg.setText(_translate("MainWindow", "..."))
        self.label_ffmpeg.setText(_translate("MainWindow", "ffmpeg"))
        self.label_plex.setText(_translate("MainWindow", "Plex Movie"))
        self.label_vlc.setText(_translate("MainWindow", "VLC"))
        self.getOpen_vlc.setText(_translate("MainWindow", "..."))
        self.getOpen_plexSeries.setText(_translate("MainWindow", "..."))
        self.label_plexSeries.setText(_translate("MainWindow", "Plex Series"))
        self.pushButton_cancelOptions.setText(_translate("MainWindow", "Cancel"))
        self.pushButton_saveOptions.setText(_translate("MainWindow", "Save"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "options"))

