

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 101))
        font = QtGui.QFont()
        font.setFamily("Roboto Cn")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(168, 168, 168);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(75, 325, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.btn_ravno = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ravno.setGeometry(QtCore.QRect(150, 325, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_ravno.setFont(font)
        self.btn_ravno.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.btn_ravno.setObjectName("btn_ravno")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(0, 325, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_0.setObjectName("btn_0")
        self.btn_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_1.setGeometry(QtCore.QRect(0, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_1.setObjectName("btn_1")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(150, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_3.setObjectName("btn_3")
        self.btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_2.setGeometry(QtCore.QRect(75, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_2.setObjectName("btn_2")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(150, 175, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_6.setObjectName("btn_6")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(75, 175, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_5.setObjectName("btn_5")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(0, 175, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_4.setObjectName("btn_4")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(150, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_9.setObjectName("btn_9")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(75, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_8.setObjectName("btn_8")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(0, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.btn_7.setObjectName("btn_7")
        self.btn_plus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_plus.setGeometry(QtCore.QRect(225, 100, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_plus.setFont(font)
        self.btn_plus.setStyleSheet("background-color: rgb(255, 116, 3);")
        self.btn_plus.setObjectName("btn_plus")
        self.btn_minus = QtWidgets.QPushButton(self.centralwidget)
        self.btn_minus.setGeometry(QtCore.QRect(225, 175, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_minus.setFont(font)
        self.btn_minus.setStyleSheet("background-color: rgb(255, 116, 3);")
        self.btn_minus.setObjectName("btn_minus")
        self.btn_umn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_umn.setGeometry(QtCore.QRect(225, 250, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_umn.setFont(font)
        self.btn_umn.setStyleSheet("background-color: rgb(255, 116, 3);")
        self.btn_umn.setObjectName("btn_umn")
        self.btn_del = QtWidgets.QPushButton(self.centralwidget)
        self.btn_del.setGeometry(QtCore.QRect(225, 325, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_del.setFont(font)
        self.btn_del.setStyleSheet("background-color: rgb(255, 116, 3);")
        self.btn_del.setObjectName("btn_del")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.add_func()
        self.a = "0"
        self.b = "0"
        self.znak = ""

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label.setText(_translate("MainWindow", "0"))
        self.pushButton.setText(_translate("MainWindow", ","))
        self.btn_ravno.setText(_translate("MainWindow", "="))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_4.setText(_translate("MainWindow", "4"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_plus.setText(_translate("MainWindow", "+"))
        self.btn_minus.setText(_translate("MainWindow", "-"))
        self.btn_umn.setText(_translate("MainWindow", "*"))
        self.btn_del.setText(_translate("MainWindow", "/"))

    #все что после def можно обозвать как угодно тут обрабатываеся событие клик которое в свою очередь отправлсяе в метод write_number то что мы хотим
    def add_func(self):
        self.btn_0.clicked.connect(lambda: self.write_number("0"))
        self.btn_1.clicked.connect(lambda: self.write_number("1"))
        self.btn_2.clicked.connect(lambda: self.write_number("2"))
        self.btn_3.clicked.connect(lambda: self.write_number("3"))
        self.btn_4.clicked.connect(lambda: self.write_number("4"))
        self.btn_5.clicked.connect(lambda: self.write_number("5"))
        self.btn_6.clicked.connect(lambda: self.write_number("6"))
        self.btn_7.clicked.connect(lambda: self.write_number("7"))
        self.btn_8.clicked.connect(lambda: self.write_number("8"))
        self.btn_9.clicked.connect(lambda: self.write_number("9"))
        self.btn_plus.clicked.connect(lambda: self.deistvie("+"))
        self.btn_minus.clicked.connect(lambda: self.deistvie("-"))
        self.btn_umn.clicked.connect(lambda: self.deistvie("*"))
        self.btn_del.clicked.connect(lambda: self.deistvie("/"))
        self.btn_ravno.clicked.connect(lambda: self.deistvie("="))

    # обрабатываем то что нам прилетело из кнопки
    def write_number(self, number):
        if self.label.text() == "0" and number != "0":
            self.label.setText(number)
            return
        if self.label.text() == "0" and number == "0":
            self.label.setText(number)
            return
        else:
            self.label.setText(self.label.text() + number)

    # обрабатываем то что нам прилетело из кнопки
    def deistvie(self, action):
        if action != "=" and self.a == "0":
            self.a = self.label.text()
            self.label.clear()
            self.znak = action
        else:
            self.b = self.label.text()
            if self.znak == "+":
                rezult = float(self.a)+float(self.b)
                self.label.setText(str(rezult))
                self.a = "0"
            if self.znak == "-":
                rezult = float(self.a)-float(self.b)
                self.label.setText(str(rezult))
                self.a = "0"
            if self.znak == "*":
                rezult = float(self.a)*float(self.b)
                self.label.setText(str(rezult))
                self.a = "0"
            if self.znak == "/":
                rezult = float(self.a)/float(self.b)
                self.label.setText(str(rezult))
                self.a = "0"






#Обязательная херня без которой не запустится программа
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(Window)
    Window.show()
    sys.exit(app.exec())