
from PyQt5 import QtCore, QtGui, QtWidgets
from library.api import updateVault
class Settings(QtWidgets.QDialog):

    def setupUi(self, Form,session):
        self.currentsession = session
        self.clipboardlist = [5000,10000,15000,20000,30000,45000,60000,90000,120000]
        self.locklist = [0,5000,10000,30000,60000,180000,300000,600000,1800000,3600000,7200000]
        Form.setObjectName("Form")
        self.Dialog = Form
        Form.resize(322, 160)
        self.lblLock = QtWidgets.QLabel(Form)
        self.lblLock.setGeometry(QtCore.QRect(10, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblLock.setFont(font)
        self.lblLock.setObjectName("lblLock")
        self.lblClipboard = QtWidgets.QLabel(Form)
        self.lblClipboard.setGeometry(QtCore.QRect(10, 70, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblClipboard.setFont(font)
        self.lblClipboard.setObjectName("lblClipboard")
        self.cboxClipboard = QtWidgets.QComboBox(Form)
        self.cboxClipboard.setGeometry(QtCore.QRect(190, 70, 121, 21))
        self.cboxClipboard.setObjectName("cboxClipboard")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxClipboard.addItem("")
        self.cboxLock = QtWidgets.QComboBox(Form)
        self.cboxLock.setGeometry(QtCore.QRect(190, 20, 121, 22))
        self.cboxLock.setObjectName("cboxLock")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")
        self.cboxLock.addItem("")

        self.btnSave = QtWidgets.QPushButton(Form)
        self.btnSave.setGeometry(QtCore.QRect(90, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.SaveSettings)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.setCboxBySession()

    def setCboxBySession(self):
        lockindex = self.locklist.index(self.currentsession.lock)
        self.cboxClipboard.setCurrentIndex(self.clipboardlist.index(self.currentsession.clipboard))
        self.cboxLock.setCurrentIndex(lockindex)

    def SaveSettings(self):
        try:
            if((self.currentsession.lock != self.locklist[self.cboxLock.currentIndex()]) or (self.currentsession.clipboard != self.clipboardlist[self.cboxClipboard.currentIndex()])):
                self.currentsession.lock = self.locklist[self.cboxLock.currentIndex()]
                self.currentsession.clipboard = self.clipboardlist[self.cboxClipboard.currentIndex()]
                updateVault(self.currentsession)
                self.Dialog.close()
            else:
                self.Dialog.close()
        except:
            print("error")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Settings"))
        self.lblLock.setText(_translate("Form", "Lock after computer is idle for"))
        self.lblClipboard.setText(_translate("Form", "Clear clipboard contents after"))
        self.cboxClipboard.setItemText(0, _translate("Form", "5 Seconds "))
        self.cboxClipboard.setItemText(1, _translate("Form", "10  Seconds"))
        self.cboxClipboard.setItemText(2, _translate("Form", "15 Seconds"))
        self.cboxClipboard.setItemText(3, _translate("Form", "20 Seconds"))
        self.cboxClipboard.setItemText(4, _translate("Form", "30 Seconds"))
        self.cboxClipboard.setItemText(5, _translate("Form", "45 Seconds"))
        self.cboxClipboard.setItemText(6, _translate("Form", "1 Minute"))
        self.cboxClipboard.setItemText(7, _translate("Form", "90 Seconds"))
        self.cboxClipboard.setItemText(8, _translate("Form", "2 Minutes"))
        self.cboxLock.setItemText(0, _translate("Form", "Never"))
        self.cboxLock.setItemText(1, _translate("Form", "5 Seconds"))
        self.cboxLock.setItemText(2, _translate("Form", "10 Seconds"))
        self.cboxLock.setItemText(3, _translate("Form", "30 Seconds"))
        self.cboxLock.setItemText(4, _translate("Form", "1 Minute"))
        self.cboxLock.setItemText(5, _translate("Form", "3 Minutes"))
        self.cboxLock.setItemText(6, _translate("Form", "5 Minutes"))
        self.cboxLock.setItemText(7, _translate("Form", "10 Minutes"))
        self.cboxLock.setItemText(8, _translate("Form", "30 Minutes"))
        self.cboxLock.setItemText(9, _translate("Form", "1 Hour"))
        self.cboxLock.setItemText(10, _translate("Form", "2 Hours"))
        self.btnSave.setText(_translate("Form", "Save"))


