import sys
from bt_capture.Capture import Capture
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui.mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 创建一个捕包的类
        self.data_capture = Capture()

        # 因为当数据改变是我们需要data_statistics发出相应的信号，这样我们就可以实现界面中
        # 数据的变化
        self.data_statistics = self.data_capture.rec.proto_restore.statistic

        self.init_widget()


    def init_widget(self):
        '''
        对主窗口的widget进行初始化，包括初始化widget数据，以及进行事件的绑定。
        :return:
        '''
        # 点击开始捕包按钮进行捕包
        self.ui.start_cap_b.clicked.connect(self.start_capture)

        self.ui.stop_cap_b.clicked.connect(self.data_capture.stop_capture)

        # 点击tracker信息显示tracker的相关信息
        self.ui.show_tracker_info_b.clicked.connect(self.show_tracker_info)

        # 点击peers信息显示peers的相关信息
        self.ui.show_peers_info_b.clicked.connect(self.show_peers_info)

        # self.data_statistic.signal.connect(event)
        # 以下代码仅是个例子
        self.data_statistics.dataChanged.connect(self.data_changed)


    def start_capture(self):
        '''
        当点击开始捕包按钮时进行捕包
        :return:
        '''
        self.data_capture.capture()
        print('start capturing!')

    def show_tracker_info(self):
        '''
        点击tracker信息按钮是展示tracker的信息
        :return:
        '''
        print('show tracker info!')

    def show_peers_info(self):
        '''
        点击peer信息按钮时展示peers的信息
        :return:
        '''
        print('show peers info1')
        pass

    def data_changed(self):
        pass



if __name__ == '__main__':
    app =  QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())