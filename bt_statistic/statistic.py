from bt_protocol_restore.protocols.Peer_Handshake import *
class Statistic:

    def __init__(self):
        # ip : tracker
        self.iip = '192.168.1.9'
        self.tracker_stat = {}
        self.peer_stat = {}
        self.tracker_pkt_cnt = 0
        self.peer_pkt_cnt = 0

    def add_tracker_pkt(self, pkt, type):
        self.tracker_pkt_cnt += 1
        pkt_info = pkt.packet_info
        if type == 'response':
            ip = pkt_info.sip
            port = pkt_info.sport
        else:
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
        if isinstance(stat, Peer_Handshake):
            pass
        else:
            pass


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




