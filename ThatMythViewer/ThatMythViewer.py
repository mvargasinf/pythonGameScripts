# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datMythViewer.ui'
#
# Created: Sat Mar 21 02:44:43 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import scripts.that_offset_list as tofl
import scripts.MythName as myth_array
import sys

currentText = ''

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(381, 129)
        
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 131, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.pushButton2 = QtGui.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(140, 90, 121, 23))
        self.pushButton2.setObjectName(_fromUtf8("pushButton2"))
        self.pushButton2.setCheckable(False)
        self.pushButton2.clicked.connect(self.myth_load)
        
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 30, 121, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 16))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 361, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        
        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 30, 113, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 10, 51, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.comboBox.addItems(myth_array.myth_Name)
    
    def myth_load(self):
        currentText = str(self.comboBox.currentText())
        self.lineEdit_2.setText(str(tofl.mythDict[currentText]))
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ThatMythViewer - [r1-beta]", None))
        self.pushButton.setText(_translate("Form", "Add modifications", None))
        self.pushButton2.setText(_translate("Form", "Load text", None))
        self.label.setText(_translate("Form", "MythName", None))
        self.label_2.setText(_translate("Form", "HexValue", None))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

def MythRefLoad(self):
    print 'test'

