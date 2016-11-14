import sys
from time import sleep
from PyQt5 import QtCore, QtGui, QtWidgets

from mainwindow import Ui_MainWindow


class Main(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_StartEncoding.clicked.connect( self.btn_Encoding)

    def btn_Encoding(self):
        self.ui.lbl_encoding.setText("Encoding: test")
        for i in range(101):
            sleep( 0.05)
            self.ui.progressBar.setProperty("value", i)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()

    sys.exit(app.exec_())