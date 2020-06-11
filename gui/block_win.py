import sys
from bt_capture.Capture import Capture
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui.block import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
from bt_data_control.control import Control
import re


class BlockWindow(QDialog):
    def __init__(self):
        super(BlockWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.init_widget()

        self.ctrl = Control()

        self.block_peers = []


    def init_widget(self):
        # 添加需要阻断peer的信息
        self.ui.add_b.clicked.connect(self.add_block_peer)

        # 阻断所有的peers
        self.ui.block_all_b.clicked.connect(self.block_all_peers)

        # 开始阻断添加的peers
        self.ui.start_block_b.clicked.connect(self.start_block)

    def start_block(self):
        for ip, port in self.block_peers:
            self.ctrl.add_blocked_addr(ip, port)

    def block_all_peers(self):
        Control.block_all_flag = True


    def add_block_peer(self):
        ip_str = self.ui.ip_l.text()
        port_str = self.ui.port_l.text()
        # 对输入的数据进行检查
        match_result = re.match(r'^\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?$', ip_str)
        if match_result is None:
            # 显示错误信息
            pass
            return
        # 正确的ip格式
        ip = ip_str
        try:
            port = int(port_str)
        except ValueError:
            # 显示port错误信息
            pass
            return
        self.block_peers.append((ip, port))
        peer_info = 'IP:%s, PORT:%s [手动添加]' % (ip, port)
        self.ui.peer_t.append(peer_info)



    def accept(self):
        print('hello')

