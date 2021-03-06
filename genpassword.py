from PyQt5 import QtCore, QtGui, QtWidgets
from library.crypto import generatePassword
class Ui_GeneratePassword(QtWidgets.QDialog):
    mainpassword = QtCore.pyqtSignal(str)

    def setupUi(self, GeneratePassword):
        GeneratePassword.setObjectName("GeneratePassword")
        GeneratePassword.resize(410, 203)
        self.sliderPassLen = QtWidgets.QSlider(GeneratePassword)
        self.sliderPassLen.setGeometry(QtCore.QRect(10, 90, 391, 22))
        self.sliderPassLen.setMinimum(8)
        self.sliderPassLen.setMaximum(64)
        self.sliderPassLen.setProperty("value", 64)
        self.sliderPassLen.setOrientation(QtCore.Qt.Horizontal)
        self.sliderPassLen.setObjectName("sliderPassLen")
        self.sliderPassLen.valueChanged.connect(self.changed_slider)
        self.lblPassLen = QtWidgets.QLabel(GeneratePassword)
        self.lblPassLen.setGeometry(QtCore.QRect(10, 70, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPassLen.setFont(font)
        self.lblPassLen.setObjectName("lblPassLen")
        self.lnPassword = QtWidgets.QLineEdit(GeneratePassword)
        self.lnPassword.setGeometry(QtCore.QRect(10, 40, 391, 20))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.lnPassword.setFont(font)
        self.lnPassword.setObjectName("lnPassword")
        self.lblPassName = QtWidgets.QLabel(GeneratePassword)
        self.lblPassName.setGeometry(QtCore.QRect(10, 20, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPassName.setFont(font)
        self.lblPassName.setObjectName("lblPassName")
        self.cBoxSymbols = QtWidgets.QCheckBox(GeneratePassword)
        self.cBoxSymbols.setGeometry(QtCore.QRect(10, 120, 120, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBoxSymbols.setFont(font)
        self.cBoxSymbols.setChecked(True)
        self.cBoxSymbols.setObjectName("cBoxSymbols")
        self.cBoxSymbols.stateChanged.connect(self.RegeneratePassword)
        self.cBoxDigits = QtWidgets.QCheckBox(GeneratePassword)
        self.cBoxDigits.setGeometry(QtCore.QRect(10, 140, 101, 17))
        self.cBoxDigits.stateChanged.connect(self.RegeneratePassword)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cBoxDigits.setFont(font)
        self.cBoxDigits.setChecked(True)
        self.cBoxDigits.setObjectName("cBoxDigits")
        self.btnRegenerate = QtWidgets.QPushButton(GeneratePassword)
        self.btnRegenerate.setGeometry(QtCore.QRect(80, 160, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnRegenerate.setFont(font)
        self.btnRegenerate.setObjectName("btnRegenerate")
        self.btnRegenerate.clicked.connect(self.RegeneratePassword)
        self.btnSelect = QtWidgets.QPushButton(GeneratePassword)
        self.btnSelect.setGeometry(QtCore.QRect(210, 160, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSelect.setFont(font)
        self.btnSelect.setObjectName("btnSelect")
        self.btnSelect.clicked.connect(self.SelectPassword)
        self.lblSliderValue = QtWidgets.QLabel(GeneratePassword)
        self.lblSliderValue.setGeometry(QtCore.QRect(380, 70, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblSliderValue.setFont(font)
        self.lblSliderValue.setObjectName("lblSliderValue")
        self.Dialog = GeneratePassword
        self.retranslateUi(GeneratePassword)
        QtCore.QMetaObject.connectSlotsByName(GeneratePassword)

    def SelectPassword(self):
        try:
            self.mainpassword.emit(self.lnPassword.text())
            self.Dialog.close()
        except:
            print("error")

    def RegeneratePassword(self):
        options = ['upper']
        if self.cBoxDigits.isChecked():
            options.append('digits')
        if self.cBoxSymbols.isChecked():
            options.append('symbols')
        generatedpassword = generatePassword(self.sliderPassLen.value(),options)
        self.lnPassword.setText(generatedpassword)

    def changed_slider(self):
        value = self.sliderPassLen.value()
        self.lblSliderValue.setText(str(value))
        self.RegeneratePassword()

    def retranslateUi(self, GeneratePassword):
        _translate = QtCore.QCoreApplication.translate
        GeneratePassword.setWindowTitle(_translate("GeneratePassword", "Password Generator"))
        self.lblPassLen.setText(_translate("GeneratePassword", "Password Length:"))
        self.lnPassword.setText(_translate("GeneratePassword", "b7@Dsewd$4#50b^iFgjjRt$?y*hm3VfpNbouQhnn0N?zxl@l#ca6&zr1jrznFgpw"))
        self.lblPassName.setText(_translate("GeneratePassword", "Password"))
        self.cBoxSymbols.setText(_translate("GeneratePassword", "Allow Symbols"))
        self.cBoxDigits.setText(_translate("GeneratePassword", "Allow Digits"))
        self.btnRegenerate.setText(_translate("GeneratePassword", "Regenerate"))
        self.btnSelect.setText(_translate("GeneratePassword", "Select Password"))
        self.lblSliderValue.setText(_translate("GeneratePassword", "64"))
        self.lnPassword.setText(generatePassword(self.sliderPassLen.value(),['upper', 'digits', 'symbols']))



