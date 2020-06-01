from bt_protocol_restore.protocols.Peer_Handshake import *
from PyQt5.QtCore import pyqtSignal, QObject

class Statistic:
    # 定义信号
    # 第1个int表示requst包的数量，第2个int表示response包的数量
    # tracker_pkt_cnt_changed = pyqtSignal(int, int)

    # 第1个int表示handshake包的数量，第2个int表示message包的数量
    # peer_pkt_cnt_changed = pyqtSignal(int, int)

    def __init__(self):
        # super().__init__()
        # ip : tracker
        self.iip = '192.168.1.9'
        self.tracker_stat = {}
        self.peer_stat = {}
        self.tracker_res_pkt_cnt = 0
        self.tracker_req_pkt_cnt = 0
        self.peer_hs_pkt_cnt = 0
        self.peer_msg_pkt_cnt = 0


    def add_tracker_pkt(self, pkt, type):

        pkt_info = pkt.packet_info
        if type == 'response':
            self.tracker_res_pkt_cnt += 1
            # 发送信号
            # self.tracker_pkt_cnt_changed.emit(self.tracker_req_pkt_cnt, self.tracker_res_pkt_cnt)
            ip = pkt_info.sip
            port = pkt_info.sport
        else:
            self.tracker_req_pkt_cnt += 1
            # 发送信号
            # self.tracker_pkt_cnt_changed.emit(self.tracker_req_pkt_cnt, self.tracker_res_pkt_cnt)

            ip = pkt_info.dip
            port = pkt_info.dport

        if ip in self.tracker_stat.keys():
            stat = self.tracker_stat[ip]
        else:
            stat = Tracker_Info(ip, port)
            self.tracker_stat[ip] = stat
        if type == 'response':
            if pkt.action == 0:
                pass
            elif pkt.action == 1:
                seeders = pkt.seeders
                user_cnt = len(pkt.ip_port_list)
                stat.set_seeders(seeders)
                stat.set_users(user_cnt)
            elif pkt.action == 2:
                pass
            elif pkt.action == 3:
                pass
        else:
            if pkt.action == 0:
                pass
            elif pkt.action == 1:
                pass
            elif pkt.action == 2:
                pass

    def add_peer_pkt(self, pkt):
        self.peer_pkt_cnt += 1
        pkt_info = pkt.packet_info

        if ticks - last_time == 0:
            speed = last_speed
        if pkt_info.sip == self.iip:
            ip = pkt_info.dip
            port = pkt_info.dport
        else:
            ip = pkt_info.sip
            port = pkt_info.sport
        if ip in self.peer_stat.keys():
            stat = self.peer_stat[ip]
        else:
            stat = Peer_Info(ip, port)
            self.peer_stat[ip] = stat
        # 统计握手协议
        if isinstance(pkt, Peer_Handshake):
            self.peer_hs_pkt_cnt += 1
            # 发送信号
            # print('in add_peer_pkt method')
            # self.peer_pkt_cnt_changed.emit(self.peer_hs_pkt_cnt, self.peer_msg_pkt_cnt)

        else:
            self.peer_msg_pkt_cnt += 1
            # 发送信号
            # self.peer_pkt_cnt_changed.emit(self.peer_hs_pkt_cnt, self.peer_msg_pkt_cnt)



class Tracker_Info:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.state = 0
        self.seeders = 0
        self.users = 0

    def set_seeders(self, seeders):
        self.seeders = seeders

    def set_state(self, state):
        pass

    def set_users(self, users):
        self.users = users

    def __str__(self):
        pass


class Peer_Info:

    def __init__(self, ip, port):
        self.ip = 0
        self.port = 0
        self.client = 0
        self.download_speed = 0
        self.upload_speed = 0
        self.downloaded = 0

    def __str__(self):
        pass




