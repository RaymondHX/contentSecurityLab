import sys
from bt_capture.Capture import Capture
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from gui.configure import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets


class ConfigWindow(QDialog):
    def __init__(self):
        super(ConfigWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # self.init_widget()

    # def init_widget(self):
    #     self.ui.pushButton.clicked(self.accept)
    def accept(self):
        print('hello')




