# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firstpage.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
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
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.seller.setFont(font)
        self.seller.setObjectName("seller")
        self.gridLayout.addWidget(self.seller, 1, 1, 1, 1)
        self.customer = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.customer.setFont(font)
        self.customer.setObjectName("customer")
        self.gridLayout.addWidget(self.customer, 1, 0, 1, 1)
        self.admin = QtWidgets.QPushButton(Form)
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

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "با سلام، خوش‌آمدید، انتخاب کنید."))
        self.seller.setText(_translate("Form", "فروشنده"))
        self.customer.setText(_translate("Form", "خریدار"))
        self.admin.setText(_translate("Form", "ادمین"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

