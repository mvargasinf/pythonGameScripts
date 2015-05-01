#!usr/bin/python2.79
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datTextEditor.ui'
#
# Created: Thu Apr 09 19:20:22 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import Tkinter, tkFileDialog, binascii

root = Tkinter.Tk()
root.withdraw()

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
        Form.resize(548, 204)

        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 20, 131, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 0, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))

        self.lineEdit_2 = QtGui.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 60, 131, 20))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))

        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.lineEdit_3 = QtGui.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 100, 131, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))

        self.lineEdit_4 = QtGui.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(0, 140, 131, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))

        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 91, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(Form)

        self.line.setGeometry(QtCore.QRect(120, -10, 20, 211))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(140, 0, 401, 201))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))

        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 141, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))

        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 70, 381, 121))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))

        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(284, 10, 111, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(0, 160, 131, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.plainTextEdit.setPlainText('Text will be here.')
        self.pushButton.clicked.connect(self.LoadFile)
        
    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "ThatOneMessageEditor", None))
        self.label.setText(_translate("Form", "Size", None))
        self.label_2.setText(_translate("Form", "End of Text", None))
        self.label_3.setText(_translate("Form", "Amount of Entries", None))
        self.label_4.setText(_translate("Form", "Text Entries", None))
        self.groupBox.setTitle(_translate("Form", "Text Editor", None))
        self.label_5.setText(_translate("Form", "Text Entry Select", None))
        self.pushButton_2.setText(_translate("Form", "Save Message File", None))
        self.pushButton.setText(_translate("Form", "Load Message File", None))

    def LoadFile(self, pressed):
        msg_File = tkFileDialog.askopenfilename(title='Open a message file!', filetypes=[('Message File', '*.bmd')])
        file_read = open(msg_File, 'rb').read()

        # header stuff
        size_msgFile = binascii.hexlify(file_read[5])
        size_tblFile = binascii.hexlify(file_read[17])
        size_amtFile = binascii.hexlify(file_read[21])
        size_textFile = binascii.hexlify(file_read[24])

        # converts the offsets to a usable form
        size_msgFile = int(size_msgFile + binascii.hexlify(file_read[4]), 16)
        size_tblFile = int(size_tblFile + binascii.hexlify(file_read[16]), 16)
        size_amtFile = size_amtFile + binascii.hexlify(file_read[20])
        size_textFile = int(size_textFile, 16)
        
        # some calculations to find end of table
        size_endset = size_tblFile - 32
        size_endset = hex(size_endset)
        size_endset = str(size_endset[4:7]) + str(size_endset[2:4])
        print(size_endset)
        # end of calculations
        
        # find value pos
        posHex = file_read.find(hexText)
        print(posHex)

        # load text
        self.lineEdit.setText(str(size_msgFile))
        self.lineEdit_2.setText(str(size_tblFile))
        self.lineEdit_3.setText(str(size_amtFile))
        self.lineEdit_4.setText(str(size_textFile))
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

