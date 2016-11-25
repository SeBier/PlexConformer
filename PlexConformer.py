#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import configparser
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets
import ctypes

from mainwindow import Ui_MainWindow
from media_encode import checkcrop

import media_rename
import media_encode

version = '0.1'
myappid = 'SeBier.PlexConformer.Subproduct.'+version # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

# global variable for headers
horHeaders = ['New Title', 'Special', 'Ratio', 'Deinterlace']
verHeaders = []

cuda = False

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

        #setup the tableWidget under the naming tab
        self.ui.tableWidget_naming.setColumnCount(len(horHeaders))
        self.ui.tableWidget_naming.setHorizontalHeaderLabels(horHeaders)
        self.ui.tableWidget_naming.setVerticalHeaderLabels( ['None'])
        self.ui.tableWidget_naming.resizeColumnsToContents()

        # File Combobox with data
        self.titleRefresh()

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
        self.ui.pushButton_saveOptions.clicked.connect( self.writeConfig)

    # funtions for the naming tab
    def namingBluray(self):
        dirBluray = self.locationbluray()

        if os.path.exists( dirBluray) == False:
            return ;
        elif dirBluray == '':
            return ;

        filelist = filter(lambda f: f.split('.')[-1] == 'mkv', os.listdir(dirBluray))
        filelist = sorted(filelist)

        if filelist == []:
            self.ui.tableWidget_naming.setRowCount( 1)
            self.ui.tableWidget_naming.setVerticalHeaderLabels([ 'None'])
            self.ui.tableWidget_naming.setEnabled(False)
            return ;


        #Set Row Count Table
        self.ui.tableWidget_naming.setRowCount( len(filelist))

        #Add Header
        global verHeaders
        verHeaders = filelist

        self.ui.tableWidget_naming.setVerticalHeaderLabels(verHeaders)
        self.ui.tableWidget_naming.setEnabled(True)
        self.ui.tableWidget_naming.resizeColumnsToContents()

        for f in filelist:
            path = os.path.join(dirBluray + '/' + f)
            crop = media_encode.cropDetect( path, cuda)

            try:
                res = crop[1][2].split(' ')

                #cropAdjusted = media_encode.correctAR( crop[0], res[0])

                row = filelist.index( f)
                collumn = horHeaders.index('Ratio')
                #item = cropAdjusted
                item = crop[0]

                self.ui.tableWidget_naming.setItem( row, collumn, QtWidgets.QTableWidgetItem(item))
            except:
                print( 'Error: %s is not readable.' % f)



        '''
        data = {'title04.mkv':['Mad Max - Fury Road (2015)','','2.40', 'false'],
                'title17.mkv':['Crash & Smash','behindthescenes','1.78', 'false'],
                'title18.mkv':['Die Dreharbeiten','behindthescenes','1.78', 'false']}

        for m, key in enumerate(sorted(data.keys())):
            for n, item in enumerate(data[key]):
                newitem = QtWidgets.QTableWidgetItem(item)
                self.ui.tableWidget_naming.setItem(m, n, newitem)
        '''


    def showCrop(self):
        #try:
            indexes = self.ui.tableWidget_naming.selectionModel().selectedRows()
            rows = set(index.row() for index in self.ui.tableWidget_naming.selectedIndexes())
            row = list(rows)[0]
            collumn = horHeaders.index('Ratio')

            crop = self.ui.tableWidget_naming.item( row, collumn).text()

            path = os.path.join(self.ui.lineEdit_blurayName.text() + '/' + verHeaders[row])
            checkcrop( path, crop)
        #except:
        #    print( 'Error')

    # funtions for the encoding tab
    def locationbluray(self):
        dirBluray = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select BluRay-Rip Directory')
        self.ui.lineEdit_blurayName.setText(dirBluray)
        self.ui.lineEdit_blurayEnc.setText(dirBluray)
        return dirBluray

    def titleRefresh(self):
        cwd = os.getcwd()
        moviePath = cwd + '\movie_titles'

        titleList = filter(lambda f: f.split('.')[-1] == 'pcf', os.listdir(moviePath))
        titleList = sorted(titleList)

        newtitleList = []

        for f in titleList:
            newtitleList.append(f[:-4])

        # clear Combobox before adding titles
        self.ui.comboBox_mTitle.clear()
        self.ui.comboBox_mTitle.addItems( newtitleList)

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

    def readConfig(self):
        config = configparser.ConfigParser()
        config.read('user.cfg')
        if 'GENERAL' in config:
            global cuda
            cuda = config['GENERAL']['cuda']

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
        config = configparser.ConfigParser()
        config.read('user.cfg')
        config['LOCATIONS'] = {'ffmpeg': self.ui.lineEdit_ffmpeg.text(),
                                'plexmovie': self.ui.lineEdit_plexMovie.text(),
                                'plexseries': self.ui.lineEdit_plexSeries.text(),
                                'vlc': self.ui.lineEdit_vlc.text()}


        with open('user.cfg', 'w') as configfile:
            config.write(configfile)


def DefaultConfig():
    if os.path.exists('user.cfg') == False:
        config = configparser.ConfigParser()
        config['GENERAL'] = {'cuda': 'false'}
        config['ENCODING'] = {'deinterlace': 'bwdif',
                                'codec': 'libx264',
                                'preset': 'superfast',
                                'tune': 'film',
                                'profile': 'high',
                                'level': '4.2',
                                'crf_value': '20',
                                'format': 'mkv',
                                'allowedratios' : '1.33, 1.55, 1.78, 1.85, 2.35, 2.39, 2.40'}
        with open('user.cfg', 'w') as configfile:
            config.write(configfile)


if __name__ == '__main__':
    DefaultConfig()
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())
