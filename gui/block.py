# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'block.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(881, 421)
        self.block_info_t = QtWidgets.QTextEdit(Dialog)
        self.block_info_t.setGeometry(QtCore.QRect(300, 70, 561, 321))
        self.block_info_t.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.block_info_t.setObjectName("block_info_t")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 64, 72, 21))
        self.label.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.ip_l = QtWidgets.QLineEdit(Dialog)
        self.ip_l.setGeometry(QtCore.QRect(100, 70, 141, 21))
        self.ip_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.ip_l.setObjectName("ip_l")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 72, 31))
        self.label_2.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.add_b = QtWidgets.QPushButton(Dialog)
        self.add_b.setGeometry(QtCore.QRect(10, 140, 61, 28))
        self.add_b.setStyleSheet("font: 9pt \"微软雅黑\";    \n"
"")
        self.add_b.setObjectName("add_b")
        self.port_l = QtWidgets.QLineEdit(Dialog)
        self.port_l.setGeometry(QtCore.QRect(100, 100, 71, 21))
        self.port_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.port_l.setObjectName("port_l")
        self.peer_t = QtWidgets.QTextEdit(Dialog)
        self.peer_t.setGeometry(QtCore.QRect(10, 270, 271, 121))
        self.peer_t.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.peer_t.setObjectName("peer_t")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 50, 111, 16))
        self.label_3.setStyleSheet("color:rgb(111, 210, 255);\n"
"font: 9pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 141, 16))
        self.label_4.setStyleSheet("color:rgb(111, 210, 255);\n"
"font: 9pt \"微软雅黑\";")
        self.label_4.setObjectName("label_4")
        self.start_block_b = QtWidgets.QPushButton(Dialog)
        self.start_block_b.setGeometry(QtCore.QRect(10, 0, 131, 33))
        self.start_block_b.setStyleSheet("font: 9pt \"微软雅黑\";    \n"
"")
        self.start_block_b.setObjectName("start_block_b")
        self.block_all_b = QtWidgets.QPushButton(Dialog)
        self.block_all_b.setGeometry(QtCore.QRect(150, 0, 121, 33))
        self.block_all_b.setStyleSheet("font: 9pt \"微软雅黑\";    \n"
"\n"
"    ")
        self.block_all_b.setObjectName("block_all_b")
        self.stop_block_b = QtWidgets.QPushButton(Dialog)
        self.stop_block_b.setGeometry(QtCore.QRect(290, 0, 101, 28))
        self.stop_block_b.setStyleSheet("\n"
"background-color: rgb(255, 85, 0);\n"
"font: 9pt \"微软雅黑\";    \n"
"\n"
"    ")
        self.stop_block_b.setObjectName("stop_block_b")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "block"))
        self.label.setText(_translate("Dialog", "peer ip"))
        self.label_2.setText(_translate("Dialog", "peer port"))
        self.add_b.setText(_translate("Dialog", "添加"))
        self.label_3.setText(_translate("Dialog", "阻断信息显示"))
        self.label_4.setText(_translate("Dialog", "要阻断的peer信息"))
        self.start_block_b.setText(_translate("Dialog", "阻断选择的peers"))
        self.block_all_b.setText(_translate("Dialog", "阻断所有peers"))
        self.stop_block_b.setText(_translate("Dialog", "停止所有阻断"))
