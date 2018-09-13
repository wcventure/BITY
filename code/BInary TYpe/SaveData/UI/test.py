# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(765, 550)
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(310, 20, 141, 31))
        self.title.setObjectName("title")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 60, 711, 431))
        self.textEdit.setObjectName("textEdit")
        self.submit = QtWidgets.QPushButton(Dialog)
        self.submit.setGeometry(QtCore.QRect(350, 500, 75, 23))
        self.submit.setObjectName("submit")

        self.retranslateUi(Dialog)
        self.submit.clicked.connect(self.textEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "IDA Assembly Language"))
        self.submit.setText(_translate("Dialog", "submit"))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
