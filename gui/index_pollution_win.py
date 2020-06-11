import sys
from bt_capture.Capture import Capture
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui.index_pollution import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from gui.check import *
from bt_index_pollution.send_pollution import *

class IndexPollutionWindow(QDialog):
    def __init__(self):
        super(IndexPollutionWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.init_widget()

    def init_widget(self):
        self.ui.pollute_b.clicked.connect(self.pollute)

    def pollute(self):
        tracker_ip_str = self.ui.tracker_ip_l.text()
        tracker_port_str = self.ui.tracker_port_l.text()
        pollute_port_str = self.ui.polluted_port_l.text()
        min_ip_1_str = self.ui.min_ip_1_l.text()
        min_ip_2_str = self.ui.min_ip_2_l.text()
        min_ip_3_str = self.ui.min_ip_3_l.text()
        min_ip_4_str = self.ui.min_ip_4_l.text()

        max_ip_1_str = self.ui.max_ip_1_l.text()
        max_ip_2_str = self.ui.max_ip_2_l.text()
        max_ip_3_str = self.ui.max_ip_3_l.text()
        max_ip_4_str = self.ui.max_ip_4_l.text()

        # 进行数据检查
        # 对污染的ip地址范围内的输入进行检查
        try:
            min_ip_1 = int(min_ip_1_str)
            min_ip_2 = int(min_ip_2_str)
            min_ip_3 = int(min_ip_3_str)
            min_ip_4 = int(min_ip_4_str)

            max_ip_1 = int(max_ip_1_str)
            max_ip_2 = int(max_ip_2_str)
            max_ip_3 = int(max_ip_3_str)
            max_ip_4 = int(max_ip_4_str)
        except ValueError:
            print('用于污染的ip地址格式不合法')
            pass
            return
        for ip_part in [min_ip_1, min_ip_2, min_ip_3, min_ip_4, max_ip_1, max_ip_2, max_ip_3, max_ip_4]:
            if ip_part < 0 or ip_part > 255:
                print('用于污染的ip地址格式不合法')
                pass

        # 判断max_ip '大于' min_ip
        for min_ip_part, max_ip_part in zip([min_ip_4, min_ip_3, min_ip_2, min_ip_1],
                                            [max_ip_4, max_ip_3, max_ip_2, max_ip_1]):
            if max_ip_part > min_ip_part:
                break
            if max_ip_part == min_ip_part:
                continue
            else:
                print('max_ip 小于 min_ip!,不合法')
                return



        # 对污染的port进行检查
        if not port_check(pollute_port_str):
            print('用于污染的端口不合法')
            return
        pollute_port = pollute_port_str

        # 对tracker ip进行检查
        if not ip_check(tracker_ip_str):
            print('tracker ip不合法')
            return
        tracker_ip = tracker_ip_str

        # 对tracker port进行检查
        if not port_check(tracker_port_str):
            print('tracker port不合法')
            return
        tracker_port = int(tracker_port_str)

        # 下面开始进行污染
        send_pollution().send_http_announce(tracker_ip,tracker_port,min_ip_part,max_ip_part, pollute_port)
