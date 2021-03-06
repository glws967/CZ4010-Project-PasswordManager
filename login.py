import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import Qt
import library.api
import library.account
import manager

class Ui_Dialog(QtWidgets.QMainWindow):
    def loginCheck(self):
        username = self.leUsername.text().strip()
        password = self.lePassword.text().strip()
        if username and password:
            session = library.api.login(username,password)
            if session==False:
                self.lblMessage.setText("Login failed.")
            elif isinstance(session,library.api.usersession):

                self.w = manager.Ui_MainWindow()
                self.w.Dialog = QtWidgets.QDialog(None, Qt.WindowCloseButtonHint)
                self.w.Dialog.setFixedSize(670, 487)
                self.w.setupUi(self.w.Dialog,session,MainWindow, app)
                self.w.Dialog.show()
                MainWindow.hide()
                self.lblMessage.setText("")
            else:
                self.lblMessage.setText("Login failed.")
        elif not username or not password:
            self.lblMessage.setText("Login failed,Empty Strings detected.")
        else:
            self.lblMessage.setText("Login failed.")
    def registerCheck(self):
        username = self.leUsername.text().strip()
        password = self.lePassword.text().strip()
        if username and password:
            session = library.api.createNewAccount(username,password)
            if session==False:
                self.lblMessage.setText("Signup failed.")
            elif isinstance(session,library.api.usersession):
                self.lblMessage.setText("Signup Successful!")
            else:
                self.lblMessage.setText("Signup failed.")
        elif not username or not password:
            self.lblMessage.setText("Signup failed.Empty Strings detected.")
        else:
            self.lblMessage.setText("Signup failed.")
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(588, 426)
        self.lblTitle = QtWidgets.QLabel(Dialog)
        self.lblTitle.setGeometry(QtCore.QRect(70, 70, 461, 61))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(20)
        
        self.lblTitle.setFont(font)
        self.lblTitle.setObjectName("lblTitle")
        self.lblUsername = QtWidgets.QLabel(Dialog)
        self.lblUsername.setGeometry(QtCore.QRect(100, 130, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblUsername.setFont(font)
        self.lblUsername.setObjectName("lblUsername")
        self.lblPassword = QtWidgets.QLabel(Dialog)
        self.lblPassword.setGeometry(QtCore.QRect(100, 170, 111, 21))
        
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lblPassword.setFont(font)
        self.lblPassword.setObjectName("lblPassword")
        self.leUsername = QtWidgets.QLineEdit(Dialog)
        self.leUsername.setGeometry(QtCore.QRect(230, 130, 241, 31))
        self.leUsername.returnPressed.connect(self.loginCheck)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.leUsername.setFont(font)
        self.leUsername.setObjectName("leUsername")
        self.lePassword = QtWidgets.QLineEdit(Dialog)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePassword.setGeometry(QtCore.QRect(230, 170, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lePassword.setFont(font)
        self.lePassword.setObjectName("lePassword")
        self.lePassword.returnPressed.connect(self.loginCheck)
        self.btnLogin = QtWidgets.QPushButton(Dialog)
        self.btnLogin.setGeometry(QtCore.QRect(250, 220, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnLogin.setFont(font)
        self.btnLogin.setObjectName("btnLogin")
        self.btnLogin.clicked.connect(self.loginCheck)
        self.btnSignup = QtWidgets.QPushButton(Dialog)
        self.btnSignup.setGeometry(QtCore.QRect(240, 320, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnSignup.setFont(font)
        self.btnSignup.setObjectName("btnSignup")
        self.btnSignup.clicked.connect(self.registerCheck)

        self.lblMessage = QtWidgets.QLabel(Dialog)
        self.lblMessage.setGeometry(QtCore.QRect(10, 370, 571, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblMessage.setFont(font)
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setObjectName("lblMessage")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login/Signup"))
        self.lblTitle.setText(_translate("Dialog", "Team YOLO PASSWORD MANAGER"))
        self.lblUsername.setText(_translate("Dialog", "User name:"))
        self.lblPassword.setText(_translate("Dialog", "Password:"))
        self.btnLogin.setText(_translate("Dialog", "Login"))
        self.btnSignup.setText(_translate("Dialog", "Sign Up"))

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        app.setStyle("Fusion")
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(53, 53, 53))
        palette.setColor(QPalette.WindowText, Qt.white)
        palette.setColor(QPalette.Base, QColor(25, 25, 25))
        palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        palette.setColor(QPalette.ToolTipBase, Qt.black)
        palette.setColor(QPalette.ToolTipText, Qt.white)
        palette.setColor(QPalette.Text, Qt.white)
        palette.setColor(QPalette.Button, QColor(53, 53, 53))
        palette.setColor(QPalette.ButtonText, Qt.white)
        palette.setColor(QPalette.BrightText, Qt.red)
        palette.setColor(QPalette.Link, QColor(42, 130, 218))
        palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        app.setPalette(palette)
        MainWindow = QtWidgets.QMainWindow()
        library.api.initializeDatabaseConnection()
        ui = Ui_Dialog()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
