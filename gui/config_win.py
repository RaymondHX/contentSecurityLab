import sys
from bt_capture.Capture import Capture
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from gui.configure import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from config import Configure
import socket
from log import Log

class ConfigWindow(QDialog):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.init_widget()

    def init_widget(self):

        self.ui.del_log_b.clicked.connect(self.delete_logs)
        # 获取本机计算机名称
        hostname = socket.gethostname()

        if Configure.host_ip is None:
            # 获取本机ip
            ip = socket.gethostbyname(hostname)
            self.ui.host_ip_t.setText(ip)
            Configure.host_ip = ip
        else:
            self.ui.host_ip_t.setText(Configure.host_ip)

        self.ui.log_c.setChecked(Configure.log)
        self.ui.db_c.setChecked(Configure.db)


    def accept(self):
        Configure.host_ip = self.ui.host_ip_t.text()
        Configure.db =  self.ui.db_c.isChecked()
        Configure.log = self.ui.log_c.isChecked()
        self.close()

    def delete_logs(self):
        ans = QMessageBox.question(self, '日志删除', '确定删除所有日志？', QMessageBox.Yes | QMessageBox.No)
        if ans == QMessageBox.No:
            return
        log = Log()
        log.delete_logs()
        QMessageBox.information(self, '日志删除', '已删除所有日志', QMessageBox.Yes)






