from PyQt5 import QtCore, QtGui, QtWidgets
from library.account import account
from library.api import updateVault
from library.crypto import generatePassword

class Ui_Form(QtWidgets.QDialog):

    emitter = QtCore.pyqtSignal(str)

    def setupUi(self, Form, session):
        self.currentsession=session
        Form.setObjectName("Form")
        Form.resize(410, 385)
        self.lblAccountName = QtWidgets.QLabel(Form)
        self.lblAccountName.setGeometry(QtCore.QRect(10, 20, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        
        self.lblAccountName.setFont(font)
        self.lblAccountName.setObjectName("lblAccountName")
        self.lnPassword = QtWidgets.QLineEdit(Form)
        self.lnPassword.setGeometry(QtCore.QRect(10, 140, 391, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.lnPassword.setFont(font)
        self.lnPassword.setText("")
        self.lnPassword.setMaxLength(64)
        self.lnPassword.setObjectName("lnPassword")
        self.lblPassword = QtWidgets.QLabel(Form)
        self.lblPassword.setGeometry(QtCore.QRect(10, 120, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.lblErrorMessage = QtWidgets.QLabel(Form)
        self.lblErrorMessage.setGeometry(QtCore.QRect(10, 320 , 391, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblErrorMessage.setFont(font)
        self.lblErrorMessage.setObjectName("lblErrorMessage")
        self.lblErrorMessage.setTextFormat(QtCore.Qt.RichText)
        self.lblPassLen = QtWidgets.QLabel(Form)
        self.lblPassLen.setGeometry(QtCore.QRect(10, 200, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPassLen.setFont(font)
        self.lblPassLen.setObjectName("lblPassLen")
        self.sliderPassLen = QtWidgets.QSlider(Form)
        self.sliderPassLen.setGeometry(QtCore.QRect(10, 220, 391, 22))
        self.sliderPassLen.setMinimum(8)
        self.sliderPassLen.setMaximum(64)
        self.sliderPassLen.setProperty("value", 64)
        self.sliderPassLen.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPassLen.setObjectName("sliderPassLen")
        self.sliderPassLen.valueChanged.connect(self.changed_slider)
        self.cBoxSymbols = QtWidgets.QCheckBox(Form)
        self.cBoxSymbols.setGeometry(QtCore.QRect(10, 240, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBoxSymbols.setFont(font)
        self.cBoxSymbols.setChecked(True)
        self.cBoxSymbols.setObjectName("cBoxSymbols")
        self.cBoxSymbols.stateChanged.connect(self.RegeneratePassword)
        self.cBoxDigits = QtWidgets.QCheckBox(Form)
        self.cBoxDigits.setGeometry(QtCore.QRect(10, 260, 101, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBoxDigits.setFont(font)
        self.cBoxDigits.setChecked(True)
        self.cBoxDigits.setObjectName("cBoxDigits")
        self.cBoxDigits.stateChanged.connect(self.RegeneratePassword)
        self.lnAccountName = QtWidgets.QLineEdit(Form)
        self.lnAccountName.setGeometry(QtCore.QRect(10, 40, 391, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.lnAccountName.setFont(font)
        self.lnAccountName.setText("")
        self.lnAccountName.setMaxLength(64)
        self.lnAccountName.setObjectName("lnAccountName")
        self.lblUserName = QtWidgets.QLabel(Form)
        self.lblUserName.setGeometry(QtCore.QRect(10, 70, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblUserName.setFont(font)
        self.lblUserName.setObjectName("lblUserName")
        self.lnUserName = QtWidgets.QLineEdit(Form)
        self.lnUserName.setGeometry(QtCore.QRect(10, 90, 391, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.lnUserName.setFont(font)
        self.lnUserName.setText("")
        self.lnUserName.setMaxLength(64)
        self.lnUserName.setObjectName("lnUserName")
        self.btnRegenerate = QtWidgets.QPushButton(Form)
        self.btnRegenerate.setGeometry(QtCore.QRect(140, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRegenerate.setFont(font)
        self.btnRegenerate.setObjectName("btnRegenerate")
        self.btnRegenerate.clicked.connect(self.RegeneratePassword)
        self.btnAdd = QtWidgets.QPushButton(Form)
        self.btnAdd.setGeometry(QtCore.QRect(140, 280, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAdd.setFont(font)
        self.btnAdd.setObjectName("btnAdd")
        self.btnAdd.clicked.connect(self.AddAccount)
        self.lblSliderValue = QtWidgets.QLabel(Form)
        self.lblSliderValue.setGeometry(QtCore.QRect(120, 200, 16, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSliderValue.setFont(font)
        self.lblSliderValue.setObjectName("lblSliderValue")
        self.RegeneratePassword()
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form) 
        self.Dialog = Form
        

    def AddAccount(self):
        ErrorMessage=""
        Error=False
        ANupdate=False
        #check if empty
        if self.lnAccountName.text() and self.lnUserName.text() and self.lnPassword.text():
            #check password is >8 and <64
            if len(self.lnPassword.text()) >=8 and len(self.lnPassword.text())<=64:
                if not self.currentsession.checkAccountExists(self.lnAccountName.text()):
                        ANupdate = True
                else:
                        Error = True
                        ErrorMessage+="This AccountName already exists<br>"
                if ANupdate and Error == False:
                    
                    new_account = account(self.lnAccountName.text(),self.lnUserName.text(),self.lnPassword.text())
                    self.currentsession.vault.append(new_account)
                    updateVault(self.currentsession)
                    try:
                        self.emitter.emit(self.lnAccountName.text())
                        self.Dialog.close()
                    except:
                        self.lblErrorMessage.setText("Error Occurred")
                else:
                    self.lblErrorMessage.setText(ErrorMessage+"No changes made.")
            else:
                self.lblErrorMessage.setText("Password must be <br>1)Less than or equal to 64 characters.<br>2)More than or equal to 8 characters.")
        else:
            self.lblErrorMessage.setText("The above inputs must not be empty.")
        
    def changed_slider(self):
        value = self.sliderPassLen.value()
        self.lblSliderValue.setText(str(value))
        self.RegeneratePassword()

    def RegeneratePassword(self):
        options = ['upper']
        if self.cBoxDigits.isChecked():
            options.append('digits')
        if self.cBoxSymbols.isChecked():
            options.append('symbols')
        generatedpassword = generatePassword(self.sliderPassLen.value(),options)
        self.lnPassword.setText(generatedpassword)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Add Account"))
        self.lblAccountName.setText(_translate("Form", "Account Name"))
        self.lblPassword.setText(_translate("Form", "Password"))
        self.lblPassLen.setText(_translate("Form", "Password Length:"))
        self.cBoxSymbols.setText(_translate("Form", "Allow Symbols"))
        self.cBoxDigits.setText(_translate("Form", "Allow Digits"))
        self.lblUserName.setText(_translate("Form", "User Name"))
        self.btnRegenerate.setText(_translate("Form", "Generate Password"))
        self.btnAdd.setText(_translate("Form", "Add Account"))
        self.lblSliderValue.setText(_translate("Form", "64"))


