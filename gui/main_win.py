import sys
from bt_capture.Capture import Capture
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.mainwindow import Ui_MainWindow
from gui.config_win import ConfigWindow
from gui.block_win import BlockWindow
from gui.index_pollution_win import IndexPollutionWindow
from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 创建一个捕包的类 线程
        self.data_capture = Capture(self.ui.show_info_text)

        # 因为当数据改变是我们需要data_statistics发出相应的信号，这样我们就可以实现界面中
        # 数据的变化
        self.data_statistics = self.data_capture.rec.proto_restore.statistic

        # 捕包状态
        self.cap_state = False
        self.init_widget()

    def init_widget(self):
        '''
        对主窗口的widget进行初始化，包括初始化widget数据，以及进行事件的绑定。
        :return:
        '''
        # 点击开始捕包按钮进行捕包
        self.ui.start_cap_b.clicked.connect(self.start_capture)

        self.ui.config_b.clicked.connect(self.show_config)

        self.ui.block_b.clicked.connect(self.show_block)

        self.ui.index_b.clicked.connect(self.show_index_pollution)

        # self.ui.block_b.clicked.connect(self.data_statistics.block)

        # 点击tracker信息显示tracker的相关信息
        self.ui.show_tracker_info_b.clicked.connect(self.show_tracker_info)

        # 点击peers信息显示peers的相关信息
        self.ui.show_peers_info_b.clicked.connect(self.show_peers_info)

        # self.data_statistic.signal.connect(event)
        # 以下代码仅是个例子
        #
        self.data_statistics.tracker_pkt_cnt_changed.connect(self.change_track_pkt_cnt)

        self.data_statistics.peer_pkt_cnt_changed.connect(self.change_peer_pkt_cnt)

        self.data_statistics.tracker_info_changed.connect(self.show_tracker_info)

        self.data_statistics.peer_info_changed.connect(self.show_peers_info)
        #self.data_statistics.peer_pkt_cnt_changed

    def show_config(self):
        self.config_window = ConfigWindow()
        self.config_window.show()

    def show_block(self):
        self.block_window = BlockWindow()
        self.block_window.show()

    def show_index_pollution(self):
        self.index_pollution_window = IndexPollutionWindow()
        self.index_pollution_window.show()

    def start_capture(self):
        '''
        当点击开始捕包按钮时进行捕包
        :return:
        '''
        if self.cap_state is False:
            self.ui.show_info_text.append('start capturing!')
            # print('start capturing!')
            self.cap_state = True
            self.data_capture.start()
            _translate = QtCore.QCoreApplication.translate
            self.ui.start_cap_b.setText(_translate("MainWindow", "停止捕包"))

        else:
            self.ui.show_info_text.append('stop capturing!')
            # print('stop capturing!')
            self.cap_state = False
            _translate = QtCore.QCoreApplication.translate
            self.ui.start_cap_b.setText(_translate("MainWindow", "开始捕包"))
            self.data_capture.stop_capture()

    def show_tracker_info(self):
        '''
        点击tracker信息按钮是展示tracker的信息
        :return:
        '''
        # print('show tracker info!')
        _translate = QtCore.QCoreApplication.translate
        # print(self.data_statistics.tracker_stat)
        for row, stat in zip(range(len(self.data_statistics.tracker_stat.values())), self.data_statistics.tracker_stat.values()):
            for column, i in zip(range(6), stat.get_info_list()):
                item = QtWidgets.QTableWidgetItem()
                self.ui.tableWidget.setItem(row, column, item)
                item = self.ui.tableWidget.item(row, column)
                item.setText(_translate("MainWindow", str(i)))

    def show_peers_info(self):
        '''
        点击peer信息按钮时展示peers的信息
        :return:
        '''
        # print('show peers info1')
        _translate = QtCore.QCoreApplication.translate
        # print(self.data_statistics.peer_stat)
        for row, stat in zip(range(len(self.data_statistics.peer_stat.values())),
                             self.data_statistics.peer_stat.values()):
            for column, i in zip(range(6), stat.get_info_list()):
                item = QtWidgets.QTableWidgetItem()
                self.ui.tableWidget_2.setItem(row, column, item)
                item = self.ui.tableWidget_2.item(row, column)
                item.setText(_translate("MainWindow", str(i)))
        pass

    def change_track_pkt_cnt(self, req_cnt, res_cnt):
        self.ui.tracker_req_line.setText(str(req_cnt))
        self.ui.tracker_res_line.setText(str(res_cnt))
    #
    def change_peer_pkt_cnt(self, hs_cnt, msg_cnt):
        self.ui.peer_hs_line.setText(str(hs_cnt))
        self.ui.peer_msg_line.setText(str(msg_cnt))


if __name__ == '__main__':
    app =  QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())