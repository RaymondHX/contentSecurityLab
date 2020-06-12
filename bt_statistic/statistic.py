from bt_protocol_restore.protocols.Peer_Handshake import *
from PyQt5.QtCore import pyqtSignal, QObject
import time

from bt_data_control.control import Control
from config import Configure
from log import Log


class Statistic(QObject):

    # 定义信号
    # 第1个int表示requst包的数量，第2个int表示response包的数量
    tracker_pkt_cnt_changed = pyqtSignal(int, int)

    # 第1个int表示handshake包的数量，第2个int表示message包的数量
    peer_pkt_cnt_changed = pyqtSignal(int, int)

    # tracker中的信息增加时发送信号，更新UI信息
    tracker_info_changed = pyqtSignal()

    # peer中信息改变是发送的信号，更新UI信息
    peer_info_changed = pyqtSignal()



    def __init__(self):
        super(Statistic, self).__init__()
        # ip : tracker
        self.iip = '192.168.1.9'
        self.tracker_stat = {}
        self.peer_stat = {}

        self.tracker_req_pkt_cnt = 0
        self.tracker_res_pkt_cnt = 0
        self.peer_msg_pkt_cnt = 0
        self.peer_hs_pkt_cnt = 0
        self.peer_upload_time = {}
        self.peer_download_time = {}
        self.ctrl = Control()
        # log
        self.log = Log()

    def add_tracker_pkt(self, pkt, type):
        # # 发送信
        # self.dataChanged.emit("old status", "new status")
        pkt_info = pkt.packet_info
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if type == 'response':
            self.tracker_res_pkt_cnt+=1
            ip = pkt_info.sip
            port = pkt_info.sport
        else:
            self.tracker_req_pkt_cnt+=1
            ip = pkt_info.dip
            port = pkt_info.dport

        if ip in self.tracker_stat.keys():
            stat = self.tracker_stat[ip]
        else:
            stat = Tracker_Info(ip, port)
            self.tracker_stat[ip] = stat
        if type == 'response':
            if pkt.action == 0:
                self.log.add_log('[%s]:udp tracker[ip:%s port:%s]进行了connect response\n' % (cur_time, ip, port))
            elif pkt.action == 1:
                seeders = pkt.seeders
                user_cnt = len(pkt.ip_port_list)
                stat.set_seeders(seeders)
                stat.set_users(user_cnt)
                self.log.add_log('[%s]:udp tracker[ip:%s port:%s]进行了announce response\n' % (cur_time, ip, port))
            elif pkt.action == 2:
                self.log.add_log('[%s]:udp tracker[ip:%s port:%s]进行了scrapy response\n' % (cur_time, ip, port))
                pass
            elif pkt.action == 3:
                self.log.add_log('[%s]:udp tracker[ip:%s port:%s]进行了error response\n' % (cur_time, ip, port))
                pass
        else:
            if pkt.action == 0:
                pass
                self.log.add_log('[%s]:本地主机向udp tracker[ip:%s port:%s]进行了connect request\n' % (cur_time, ip, port))
            elif pkt.action == 1:
                pass
                self.log.add_log('[%s]:本地主机向udp tracker[ip:%s port:%s]进行了announce request\n' % (cur_time, ip, port))
            elif pkt.action == 2:
                pass
                self.log.add_log('[%s]:本地主机向udp tracker[ip:%s port:%s]进行了scrapy request\n' % (cur_time, ip, port))
        self.tracker_info_changed.emit()
        self.tracker_pkt_cnt_changed.emit(self.tracker_res_pkt_cnt, self.tracker_req_pkt_cnt)

    def add_http_tracker(self, pkt, type):
        pass


    def add_peer_pkt(self, pkt):
        ticks = time.time()
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        pkt_info = pkt.packet_info

        if pkt_info.sip == self.iip:
            ip = pkt_info.dip
            port = pkt_info.dport
        else:
            ip = pkt_info.sip
            port = pkt_info.sport

        if Control.block_all_flag:
            self.ctrl.add_blocked_addr(ip, port)

        if ip in self.peer_stat.keys():
            stat = self.peer_stat[ip]
        else:
            stat = Peer_Info(ip, port)
            self.peer_stat[ip] = stat

        # 统计握手协议
        if isinstance(pkt, Peer_Handshake):
            self.peer_hs_pkt_cnt+=1
            self.log.add_log('[%s]:本地主机与peer[ip:%s port:%s]进行了handshake\n' % (cur_time, ip, port))
        else:
            self.log.add_log('[%s]:本地主机与peer[ip:%s port:%s]发送了数据\n' % (cur_time, ip, port))
            self.peer_msg_pkt_cnt+=1
            last_time = 0
            speed = self.peer_stat[ip].upload_speed
            # 上传
            if self.iip == pkt_info.sip:
                if ip in self.peer_upload_time.keys():
                    last_time = self.peer_upload_time[ip]
            # 下载
            else:
                if ip in self.peer_download_time.keys():
                    last_time = self.peer_download_time[ip]
            # 计算速度
            if ticks - last_time ==0:
                pass
            else:
                speed = round(pkt_info.pld_len / (ticks - last_time), 2)
            # 上传
            if self.iip == pkt_info.sip:
                self.peer_upload_time[ip] = ticks
                self.peer_stat[ip].upload_speed = speed
            # 下载
            else:
                self.peer_download_time[ip] = ticks
                self.peer_stat[ip].download_speed = speed
        self.peer_info_changed.emit()
        self.peer_pkt_cnt_changed.emit(self.peer_hs_pkt_cnt, self.peer_msg_pkt_cnt)


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
    def get_info_list(self):
        return [self.ip, self.port, self.state, self.seeders, self.users]


class Peer_Info:

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.client = "BitTorrent"
        self.download_speed = 0
        self.upload_speed = 0
        self.downloaded = 0

    def __str__(self):
        pass

    def get_info_list(self):
        return [self.ip, self.port, self.client, self.download_speed, self.upload_speed, self.downloaded]




