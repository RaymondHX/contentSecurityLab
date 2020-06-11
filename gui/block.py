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
        Dialog.resize(873, 421)
        self.block_info_t = QtWidgets.QTextEdit(Dialog)
        self.block_info_t.setGeometry(QtCore.QRect(300, 70, 561, 321))
        self.block_info_t.setObjectName("block_info_t")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 70, 72, 15))
        self.label.setObjectName("label")
        self.ip_l = QtWidgets.QLineEdit(Dialog)
        self.ip_l.setGeometry(QtCore.QRect(100, 70, 113, 21))
        self.ip_l.setObjectName("ip_l")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 72, 15))
        self.label_2.setObjectName("label_2")
        self.add_b = QtWidgets.QPushButton(Dialog)
        self.add_b.setGeometry(QtCore.QRect(10, 140, 61, 28))
        self.add_b.setObjectName("add_b")
        self.port_l = QtWidgets.QLineEdit(Dialog)
        self.port_l.setGeometry(QtCore.QRect(100, 100, 113, 21))
        self.port_l.setObjectName("port_l")
        self.peer_t = QtWidgets.QTextEdit(Dialog)
        self.peer_t.setGeometry(QtCore.QRect(10, 270, 271, 121))
        self.peer_t.setObjectName("peer_t")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 50, 111, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 141, 16))
        self.label_4.setObjectName("label_4")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 231, 32))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_block_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.start_block_b.setObjectName("start_block_b")
        self.horizontalLayout.addWidget(self.start_block_b)
        self.block_all_b = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.block_all_b.setObjectName("block_all_b")
        self.horizontalLayout.addWidget(self.block_all_b)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "peer ip"))
        self.label_2.setText(_translate("Dialog", "peer port"))
        self.add_b.setText(_translate("Dialog", "添加"))
        self.label_3.setText(_translate("Dialog", "阻断信息显示"))
        self.label_4.setText(_translate("Dialog", "要阻断的peer信息"))
        self.start_block_b.setText(_translate("Dialog", "开始阻断"))
        self.block_all_b.setText(_translate("Dialog", "阻断所有peers"))
