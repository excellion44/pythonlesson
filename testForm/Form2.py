

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form2):
        Form2.setObjectName("Form2")
        Form2.resize(400, 300)
        self.label = QtWidgets.QLabel(Form2)
        self.label.setGeometry(QtCore.QRect(180, 50, 47, 13))
        self.label.setObjectName("label")


        self.retranslateUi(Form2)
        QtCore.QMetaObject.connectSlotsByName(Form2)
        self.label.mouseDoubleClickEvent = self.closeform(Form2)


    def retranslateUi(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "Dialog"))
        self.label.setText(_translate("Form2", "TextLabel"))



    def closeform(self, Form2):
        _translate = QtCore.QCoreApplication.translate
        Form2.setWindowTitle(_translate("Form2", "1111111111"))
        print("2222222222")

