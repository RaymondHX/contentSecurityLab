# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'index_pollution.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(857, 350)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 101, 20))
        self.label_2.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_2.setObjectName("label_2")
        self.tracker_ip_l = QtWidgets.QLineEdit(Dialog)
        self.tracker_ip_l.setGeometry(QtCore.QRect(120, 60, 151, 21))
        self.tracker_ip_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.tracker_ip_l.setObjectName("tracker_ip_l")
        self.tracker_port_l = QtWidgets.QLineEdit(Dialog)
        self.tracker_port_l.setGeometry(QtCore.QRect(120, 90, 71, 21))
        self.tracker_port_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.tracker_port_l.setObjectName("tracker_port_l")
        self.min_ip_4_l = QtWidgets.QLineEdit(Dialog)
        self.min_ip_4_l.setGeometry(QtCore.QRect(70, 160, 41, 21))
        self.min_ip_4_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.min_ip_4_l.setObjectName("min_ip_4_l")
        self.min_ip_3_l = QtWidgets.QLineEdit(Dialog)
        self.min_ip_3_l.setGeometry(QtCore.QRect(140, 160, 41, 21))
        self.min_ip_3_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.min_ip_3_l.setObjectName("min_ip_3_l")
        self.min_ip_2_l = QtWidgets.QLineEdit(Dialog)
        self.min_ip_2_l.setGeometry(QtCore.QRect(210, 160, 41, 21))
        self.min_ip_2_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.min_ip_2_l.setObjectName("min_ip_2_l")
        self.min_ip_1_l = QtWidgets.QLineEdit(Dialog)
        self.min_ip_1_l.setGeometry(QtCore.QRect(280, 160, 41, 21))
        self.min_ip_1_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.min_ip_1_l.setObjectName("min_ip_1_l")
        self.max_ip_4_l = QtWidgets.QLineEdit(Dialog)
        self.max_ip_4_l.setGeometry(QtCore.QRect(70, 190, 41, 21))
        self.max_ip_4_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.max_ip_4_l.setObjectName("max_ip_4_l")
        self.max_ip_3_l = QtWidgets.QLineEdit(Dialog)
        self.max_ip_3_l.setGeometry(QtCore.QRect(140, 190, 41, 21))
        self.max_ip_3_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.max_ip_3_l.setObjectName("max_ip_3_l")
        self.max_ip_2_l = QtWidgets.QLineEdit(Dialog)
        self.max_ip_2_l.setGeometry(QtCore.QRect(210, 190, 41, 21))
        self.max_ip_2_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.max_ip_2_l.setObjectName("max_ip_2_l")
        self.max_ip_1_l = QtWidgets.QLineEdit(Dialog)
        self.max_ip_1_l.setGeometry(QtCore.QRect(280, 190, 41, 21))
        self.max_ip_1_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.max_ip_1_l.setObjectName("max_ip_1_l")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(120, 160, 21, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(190, 160, 21, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(260, 160, 21, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(190, 190, 21, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(120, 190, 21, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(260, 190, 21, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(10, 154, 72, 21))
        self.label_10.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(10, 185, 72, 20))
        self.label_11.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_11.setObjectName("label_11")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 220, 72, 21))
        self.label_3.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.label_3.setObjectName("label_3")
        self.polluted_port_l = QtWidgets.QLineEdit(Dialog)
        self.polluted_port_l.setGeometry(QtCore.QRect(70, 220, 113, 21))
        self.polluted_port_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.polluted_port_l.setObjectName("polluted_port_l")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(0, 30, 151, 16))
        self.label_12.setStyleSheet("color:rgb(111, 210, 255);\n"
"font: 9pt \"微软雅黑\";")
        self.label_12.setObjectName("label_12")
        self.pollute_b = QtWidgets.QPushButton(Dialog)
        self.pollute_b.setGeometry(QtCore.QRect(60, 290, 93, 28))
        self.pollute_b.setStyleSheet("font: 9pt \"微软雅黑\";    \n"
"")
        self.pollute_b.setObjectName("pollute_b")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(0, 130, 181, 16))
        self.label_13.setStyleSheet("color:rgb(111, 210, 255);\n"
"font: 9pt \"微软雅黑\";")
        self.label_13.setObjectName("label_13")
        self.pollution_info_l = QtWidgets.QTextEdit(Dialog)
        self.pollution_info_l.setGeometry(QtCore.QRect(410, 40, 441, 281))
        self.pollution_info_l.setStyleSheet("font: 9pt \"微软雅黑\";")
        self.pollution_info_l.setObjectName("pollution_info_l")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(420, 20, 121, 16))
        self.label_14.setStyleSheet("color:rgb(111, 210, 255);\n"
"font: 9pt \"微软雅黑\";")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "索引污染"))
        self.label.setText(_translate("Dialog", "tracker ip"))
        self.label_2.setText(_translate("Dialog", "tracker port"))
        self.label_4.setText(_translate("Dialog", "-"))
        self.label_5.setText(_translate("Dialog", "-"))
        self.label_6.setText(_translate("Dialog", "-"))
        self.label_7.setText(_translate("Dialog", "-"))
        self.label_8.setText(_translate("Dialog", "-"))
        self.label_9.setText(_translate("Dialog", "-"))
        self.label_10.setText(_translate("Dialog", "最小ip"))
        self.label_11.setText(_translate("Dialog", "最大ip"))
        self.label_3.setText(_translate("Dialog", "port"))
        self.label_12.setText(_translate("Dialog", "污染的tracker信息"))
        self.pollute_b.setText(_translate("Dialog", "开始污染"))
        self.label_13.setText(_translate("Dialog", "用于污染的ip和port信息"))
        self.label_14.setText(_translate("Dialog", "污染信息显示"))
