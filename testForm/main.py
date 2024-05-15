from PyQt5 import QtCore, QtGui, QtWidgets
from Form2 import Ui_Form2
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(350, 370, 75, 23))
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(450, 370, 75, 23))
        self.btn_2.setObjectName("btn_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.Form2 = QtWidgets.QMainWindow()
        self.ui2 = Ui_Form2()
        self.ui2.setupUi(self.Form2)

        self.btn_1.clicked.connect(self.open_second_window)
        self.btn_2.clicked.connect(self.resize_window)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_1.setText(_translate("MainWindow", "Open Form2"))
        self.btn_2.setText(_translate("MainWindow", "Resize Window"))

    def open_second_window(self):
        self.Form2.show()

    def resize_window(self):
        Window.resize(300, 300)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec_())