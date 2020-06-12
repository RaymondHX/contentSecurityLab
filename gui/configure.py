# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'configure.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(773, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(190, 250, 341, 32))
        self.buttonBox.setStyleSheet("\n"
"background-color: rgb(155, 255, 88);\n"
"font: 9pt \"微软雅黑\";    \n"
"\n"
"    ")
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(90, 40, 371, 92))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.host_ip_t = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.host_ip_t.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.host_ip_t.setObjectName("host_ip_t")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.host_ip_t)
        self.log_c = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.log_c.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.log_c.setObjectName("log_c")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.log_c)
        self.db_c = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.db_c.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.db_c.setObjectName("db_c")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.db_c)
        self.del_log_b = QtWidgets.QPushButton(Dialog)
        self.del_log_b.setGeometry(QtCore.QRect(490, 80, 91, 28))
        self.del_log_b.setStyleSheet("\n"
"background-color: rgb(255, 85, 0);\n"
"font: 9pt \"微软雅黑\";    \n"
"\n"
"    ")
        self.del_log_b.setObjectName("del_log_b")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "configure"))
        self.label.setText(_translate("Dialog", "本地ip地址"))
        self.log_c.setText(_translate("Dialog", "是否记录日志"))
        self.db_c.setText(_translate("Dialog", "是否将捕获的数据存入数据库"))
        self.del_log_b.setText(_translate("Dialog", "删除日志"))
