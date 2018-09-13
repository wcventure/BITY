# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import sys
import os
from Normalization import *
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
        self.submit.setGeometry(QtCore.QRect(250, 500, 75, 23))
        self.submit.setObjectName("submit")

        self.transformbotton = QtWidgets.QPushButton(Dialog)
        self.transformbotton.setGeometry(QtCore.QRect(350, 500, 75, 23))
        self.transformbotton.setObjectName("transform")

        self.predictbotton = QtWidgets.QPushButton(Dialog)
        self.predictbotton.setGeometry(QtCore.QRect(450, 500, 75, 23))
        self.predictbotton.setObjectName("predict")

        self.retranslateUi(Dialog)
        self.submit.clicked.connect(self.save)
        self.predictbotton.clicked.connect(self.predict)
        self.transformbotton.clicked.connect(self.transfrom)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.title.setText(_translate("Dialog", "IDA Assembly Language"))
        self.submit.setText(_translate("Dialog", "submit"))
        self.predictbotton.setText(_translate("Dialog", "predict"))
        self.transformbotton.setText(_translate("Dialog", "transform"))

    def save(self):
        try:
            with open('SaveData/tempCode/predict/tempCode/tempCode.txt', 'w') as tempCode:
                tempCode.writelines(self.textEdit.toPlainText())
        except IOError as err:
            print("File error:" + str(err))

    def predict(self):
        os.system("GUIPredict_SVM_Model.py")

    def transfrom(self):
        os.system("TransformExplorerFile.py")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())