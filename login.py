# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class firstpage(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(608, 506)
        Form.setMaximumSize(QtCore.QSize(608, 608))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.seller = QtWidgets.QPushButton(Form)
        self.seller.clicked.connect(self.switch)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seller.setFont(font)
        self.seller.setObjectName("seller")
        self.gridLayout.addWidget(self.seller, 1, 1, 1, 1)
        self.customer = QtWidgets.QPushButton(Form)
        self.customer.clicked.connect(self.switch)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.customer.setFont(font)
        self.customer.setObjectName("customer")
        self.gridLayout.addWidget(self.customer, 1, 0, 1, 1)
        self.admin = QtWidgets.QPushButton(Form)
        self.admin.clicked.connect(self.switch)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.admin.setFont(font)
        self.admin.setObjectName("admin")
        self.gridLayout.addWidget(self.admin, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def switch(self):
        self.windows = QtWidgets.QWidget()
        self.ui = login()
        self.ui.setupUi(self.windows)
        Form.hide()
        self.windows.show()


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "با سلام، خوش‌آمدید، انتخاب کنید."))
        self.seller.setText(_translate("Form", "فروشنده"))
        self.customer.setText(_translate("Form", "خریدار"))
        self.admin.setText(_translate("Form", "ادمین"))

class login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(565, 500)
        Form.setMaximumSize(QtCore.QSize(608, 500))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.username = QtWidgets.QLineEdit(Form)
        self.username.setObjectName("username")
        self.gridLayout.addWidget(self.username, 0, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.label1 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 0, 1, 1, 2)
        self.label2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 1, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)
        self.enter = QtWidgets.QPushButton(Form)
        self.enter.setSizeIncrement(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.enter.setFont(font)
        self.enter.setObjectName("enter")
        self.verticalLayout.addWidget(self.enter)
        self.enter.clicked.connect(self.logintouracc)
        self.status = QtWidgets.QLabel(Form)
        self.status.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.status.setFont(font)
        self.status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.status.setText("")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def logintouracc(self):
        account = self.username.text()
        accpass = self.password.text()
        users = open("users.txt", 'r')
        users =users.readlines()
        users = [u.replace("\n",'').split() for u in users]
        flag =  False
        for i in range(len(users)):
            if account == users[i][0] and accpass ==users[i][1]:
                flag = True
                self.status.setStyleSheet("color:green;")
                self.status.setText('ورود با موفقیت انجام شد.')
                break
        if flag==False:
            self.status.setStyleSheet("color:red;")
            self.status.setText("ورود با شکست مواجه شد، لطفا دوباره تلاش کنید.")


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label1.setText(_translate("Form", "نام کاربری: "))
        self.label2.setText(_translate("Form", "رمز عبور: "))
        self.enter.setText(_translate("Form", "ورود"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = firstpage()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

