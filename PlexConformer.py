#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import configparser
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

from mainwindow import Ui_MainWindow

version = '0.1'
myappid = 'SeBier.PlexConformer.Subproduct.'+version # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.readConfig()

        # set app icon
        appIcon = QtGui.QIcon()
        appIcon.addFile('gui/icons/16x16.png', QtCore.QSize(16,16))
        appIcon.addFile('gui/icons/24x24.png', QtCore.QSize(24,24))
        appIcon.addFile('gui/icons/32x32.png', QtCore.QSize(32,32))
        appIcon.addFile('gui/icons/48x48.png', QtCore.QSize(48,48))
        appIcon.addFile('gui/icons/64x64.png', QtCore.QSize(64,64))
        appIcon.addFile('gui/icons/128x128.png', QtCore.QSize(128,128))
        appIcon.addFile('gui/icons/256x256.png', QtCore.QSize(256,256))
        appIcon.addFile('gui/icons/512x512.png', QtCore.QSize(512,512))
        self.setWindowIcon(appIcon)

        # Naming
        self.ui.getOpen_blurayName.clicked.connect( self.namingBluray)
        self.ui.pushButton_showCrop.clicked.connect( self.showCrop)

        # Encoding
        self.ui.getOpen_blurayEnc.clicked.connect( self.locationbluray)
        self.ui.pushButton_mrefresh.clicked.connect( self.titleRefresh)
        self.ui.pushButton_startEncoding.clicked.connect( self.startEncoding)

        # Options
        self.ui.getOpen_ffmpeg.clicked.connect( self.locationFfmpeg)
        self.ui.getOpen_plexMovie.clicked.connect( self.locationPlexMovie)
        self.ui.getOpen_plexSeries.clicked.connect( self.locationPlexSeries)
        self.ui.getOpen_vlc.clicked.connect( self.locationVlc)
        self.ui.pushButton_saveOptions.clicked.connect( self.saveOptions)

    # funtions for the naming tab
    def namingBluray(self):
        self.locationbluray()


    def showCrop(self):
        pass

    # funtions for the encoding tab
    def locationbluray(self):
        dirBluray = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select BluRay-Rip Directory')
        self.ui.lineEdit_blurayName.setText(dirBluray)
        self.ui.lineEdit_blurayEnc.setText(dirBluray)

    def titleRefresh(self):
        pass

    def startEncoding(self):
        self.ui.label_encoding.setText("Encoding: test")
        for i in range(101):
            sleep( 0.05)
            self.ui.progressbar_encoding.setProperty("value", i)
        self.ui.label_encoding.setText("Encoding: finished")

    # funtions for the options tab

    def locationFfmpeg(self):
        dirFfmpeg = QtWidgets.QFileDialog.getOpenFileName(self, 'Select FFMPEG.exe', 'c:\\',"FFMPEG.exe (ffmpeg.exe)")
        self.ui.lineEdit_ffmpeg.setText(dirFfmpeg[0])

    def locationPlexMovie(self):
        dirPlex = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Plex Movie/Series Directory')
        self.ui.lineEdit_plexMovie.setText(dirPlex)

    def locationPlexSeries(self):
        dirPlex = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Plex Movie/Series Directory')
        self.ui.lineEdit_plexSeries.setText(dirPlex)

    def locationVlc(self):
        dirVlc = QtWidgets.QFileDialog.getOpenFileName(self, 'Select VLC.exe', 'c:\\',"VLC.exe (vlc.exe)")
        self.ui.lineEdit_vlc.setText(dirVlc[0])

    def saveOptions(self):
        dirFfmpeg = self.ui.lineEdit_ffmpeg.text()
        dirPlex = self.ui.lineEdit_plex.text()
        dirVlc = self.ui.lineEdit_vlc.text()
        print(dirFfmpeg)
        print(dirPlex)
        print(dirVlc)

    def readConfig(self):
        config = configparser.ConfigParser()
        config.read('default.cfg')
        if 'NAMING' in config:
            pass

        if 'ENCODING' in config:
            pass

        if 'LOCATIONS' in config:
            self.ui.lineEdit_ffmpeg.setText(config['LOCATIONS']['ffmpeg'])
            self.ui.lineEdit_plexMovie.setText(config['LOCATIONS']['plexmovie'])
            self.ui.lineEdit_plexSeries.setText(config['LOCATIONS']['plexseries'])
            self.ui.lineEdit_vlc.setText(config['LOCATIONS']['vlc'])

    def writeConfig(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())
