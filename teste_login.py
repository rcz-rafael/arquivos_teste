# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 308)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Ebrima")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(170, 80, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Candara")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 130, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Candara")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.input_usuario = QtWidgets.QLineEdit(Dialog)
        self.input_usuario.setGeometry(QtCore.QRect(130, 100, 131, 21))
        self.input_usuario.setText("")
        self.input_usuario.setObjectName("input_usuario")
        self.input_senha = QtWidgets.QLineEdit(Dialog)
        self.input_senha.setGeometry(QtCore.QRect(130, 150, 133, 21))
        self.input_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_senha.setObjectName("input_senha")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 280, 121, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 200, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tela de Login"))
        self.label.setText(_translate("Dialog", "LOGIN"))
        self.label_2.setText(_translate("Dialog", "USUÁRIO"))
        self.label_3.setText(_translate("Dialog", "SENHA"))
        self.input_usuario.setPlaceholderText(_translate("Dialog", "Digite seu e-mail ou CPF."))
        self.input_senha.setPlaceholderText(_translate("Dialog", "Digite sua senha."))
        self.label_4.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600; text-decoration: underline;\">RECUPERAR SENHA</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "ENTRAR"))
        self.pushButton_2.setText(_translate("Dialog", "CANCELAR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
