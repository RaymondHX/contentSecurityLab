# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1182, 806)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.start_cap_b = QtWidgets.QPushButton(self.centralwidget)
        self.start_cap_b.setGeometry(QtCore.QRect(80, 40, 93, 28))
        self.start_cap_b.setObjectName("start_cap_b")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 500, 1111, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.show_peers_info_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.show_peers_info_b.setObjectName("show_peers_info_b")
        self.gridLayout.addWidget(self.show_peers_info_b, 0, 1, 1, 1)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget_2.setRowCount(10)
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.gridLayout.addWidget(self.tableWidget_2, 1, 1, 1, 1)
        self.show_tracker_info_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.show_tracker_info_b.setObjectName("show_tracker_info_b")
        self.gridLayout.addWidget(self.show_tracker_info_b, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(570, 0, 541, 501))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.tracker_req_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.tracker_req_line.setObjectName("tracker_req_line")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.tracker_req_line)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.tracker_res_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.tracker_res_line.setObjectName("tracker_res_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.tracker_res_line)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.peer_hs_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.peer_hs_line.setObjectName("peer_hs_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.peer_hs_line)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.peer_msg_line = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.peer_msg_line.setObjectName("peer_msg_line")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.peer_msg_line)
        self.verticalLayout.addLayout(self.formLayout)
        self.stop_cap_b = QtWidgets.QPushButton(self.centralwidget)
        self.stop_cap_b.setGeometry(QtCore.QRect(80, 130, 93, 28))
        self.stop_cap_b.setObjectName("stop_cap_b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1182, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start_cap_b.setText(_translate("MainWindow", "开始捕包"))
        self.show_peers_info_b.setText(_translate("MainWindow", "peers信息"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ip"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "port"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "client"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "upload_speed"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "download_speed"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "downloaded"))
        self.show_tracker_info_b.setText(_translate("MainWindow", "tracker信息"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ip"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "port"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "state"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "seeders"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "users"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "1"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("MainWindow", "tracker request包的数量"))
        self.label_2.setText(_translate("MainWindow", "tracker response包的数量"))
        self.label_3.setText(_translate("MainWindow", "peer handshake包的数量"))
        self.label_4.setText(_translate("MainWindow", "peer message包的数量"))
        self.stop_cap_b.setText(_translate("MainWindow", "停止捕包"))
