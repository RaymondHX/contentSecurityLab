from bt_protocol_restore.convert import *
from bt_protocol_restore.protocols.Udp_Tracker_Request import *
from bt_protocol_restore.protocols.Udp_Tracker_Response import *
from bt_protocol_restore.protocols.Peer_Handshake import *
from bt_protocol_restore.protocols.Peer_Message import *
from bt_statistic.statistic import *
from database import *
from bt_protocol_restore.convert import *
import datetime

class Protocol_Restore:

    def __init__(self):
        self.statistic = Statistic()
        self.connect = Mysql_Connect("root", "sl488234", "bt_data")

    def udp_tracker_connect_request(self, payload, packet_info):
        conn_id_n = sub_bytes(payload, 0, 8)
        action = 0
        tran_id_n = sub_bytes(payload, 12, 4)

        conn_id = ntohq(conn_id_n)
        tran_id = ntohi(tran_id_n)
        proto_pkt = Udp_Tracker_Connect_Request(packet_info, conn_id, action, tran_id)
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into udp_tracker_connect_request_protocol (action, connection_id, transaction_id, time, src_ip, src_port, dst_ip, dst_port) values " \
              + "(0, "+str(proto_pkt.protocol_id) +", "+ str(proto_pkt.transaction_id) + ", '"+ now + "', '" + str(
            packet_info.sip) + "', '" + str(packet_info.sport) + "', '" + str(packet_info.dip) + "', '" + str(
            packet_info.dport) + "')"
        print(sql)
        self.connect.insert(sql)
        self.statistic.add_tracker_pkt(proto_pkt, type='request')
        print(proto_pkt)


    def udp_tracker_announce_request(self, payload, packet_info):
        conn_id_n = sub_bytes(payload, 0, 8)
        action = 1
        tran_id_n = sub_bytes(payload, 12, 4)
        info_hash_n = sub_bytes(payload, 16, 20)
        peer_id_n = sub_bytes(payload, 36, 20)
        downloaded_n = sub_bytes(payload, 56, 8)
        left_n = sub_bytes(payload, 64, 8)
        uploaded_n = sub_bytes(payload, 72, 8)
        event_n = sub_bytes(payload, 80, 4)
        ip_addr_n = sub_bytes(payload, 84, 4)
        key_n = sub_bytes(payload, 88, 4)
        num_want_n = sub_bytes(payload, 92, 4)
        port_n = sub_bytes(payload, 96, 2)

        conn_id = ntohq(conn_id_n)
        tran_id = ntohi(tran_id_n)
        info_hash = byets2ints(info_hash_n)
        peer_id = byets2ints(peer_id_n)
        downloaded = ntohq(downloaded_n)
        left = ntohq(left_n)
        uploaded = ntohq(uploaded_n)
        event = ntohi(event_n)
        ip_addr = ntohi(ip_addr_n)
        key = ntohi(key_n)
        num_want = ntohi(num_want_n)
        port = ntohs(port_n)
        proto_pkt = Udp_Tracker_Announce_Request(packet_info, conn_id, action, tran_id, info_hash, peer_id, downloaded,
                                        left, uploaded, event, ip_addr, key, num_want, port)
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into udp_tracker_announce_request_protocol (action, connection_id, transaction_id, info_hash, peer_id, downloaded, `left`, uploaded, event, ip_addr, `key`, num_want, port, time, src_ip, src_port, dst_ip, dst_port) values " \
              + "(1, " + str(proto_pkt.protocol_id) + ", " + str(proto_pkt.transaction_id) +", '"+proto_pkt.info_hash+"', '"+proto_pkt.peer_id+"', "+str(proto_pkt.downloaded)+", "+str(proto_pkt.left)+", "+str(proto_pkt.uploaded)+", "+str(proto_pkt.event)\
              +", "+str(proto_pkt.ip_addr)+", "+str(proto_pkt.key)+", "+str(proto_pkt.num_want)+", "+str(proto_pkt.port)+", '" + now + "', '" + str(
            packet_info.sip) + "', '" + str(packet_info.sport) + "', '" + str(packet_info.dip) + "', '" + str(
            packet_info.dport) + "')"
        print(sql)
        self.connect.insert(sql)
        self.statistic.add_tracker_pkt(proto_pkt, type='request')
        print(proto_pkt)

    def udp_tracker_scrape__request(self, payload, packet_info):
        conn_id_n = sub_bytes(payload, 0, 8)
        action = 2
        tran_id_n = sub_bytes(payload, 12, 4)

        conn_id = ntohq(conn_id_n)
        tran_id = ntohi(tran_id_n)
        info_hash_list = []
        offset = 16
        while len(payload) > offset:
            info_hash_n = sub_bytes(payload, offset, 20)
            info_hash = byets2ints(info_hash_n)
            offset += 20
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        proto_pkt =  Udp_Tracker_Scrape_Request(packet_info, conn_id, action, tran_id, info_hash_list)
        sql = "insert into udp_tracker_scrape__request_protocol (action, transaction_id, connection_id, time, src_ip, src_port, dst_ip, dst_port) values " \
              + "( 2, " + str(tran_id) + ", " + str(conn_id) + ", '" + now + "', '" + str(
            packet_info.sip) + "', '" + str(packet_info.sport) + "', '" + str(packet_info.dip) + "', '" + str(
            packet_info.dport) + "')"
        for info_hash in info_hash_list:
            sql = "insert into info_hash_list (connection_id, time, info_hash) values ("+str(conn_id)+", '"+now+"', '"+info_hash+"')"
            print(sql)
        self.statistic.add_tracker_pkt(proto_pkt, type='request')
        print(proto_pkt)

    def udp_tracker_connect_response(self, payload, packet_info):
        tran_id_n = sub_bytes(payload, 4, 4)
        conn_id_n = sub_bytes(payload, 8, 8)
        tran_id = ntohi(tran_id_n)
        conn_id = ntohq(conn_id_n)
        proto_pkt = Udp_Tracker_Connect_response(packet_info, tran_id, conn_id)
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into udp_tracker_connect_response_protocol (action, transaction_id, connection_id, time, src_ip, src_port, dst_ip, dst_port) values "\
              +"( 0, "+str(tran_id)+", "+str(conn_id)+", '" + now + "', '" + str(
            packet_info.sip) + "', '" + str(packet_info.sport) + "', '" + str(packet_info.dip) + "', '" + str(
            packet_info.dport) + "')"
        print(sql)
        self.connect.insert(sql)
        self.statistic.add_tracker_pkt(proto_pkt, type='response')
        print(proto_pkt)

    def udp_tracker_announce_response(self, payload, packet_info):
        tran_id_n = sub_bytes(payload, 4, 4)
        interval_n = sub_bytes(payload, 8, 4)
        leechers_n = sub_bytes(payload, 12, 4)
        seeders_n = sub_bytes(payload, 16, 4)
        tran_id = ntohi(tran_id_n)
        interval = ntohi(interval_n)
        leechers = ntohi(leechers_n)
        seeders = ntohi(seeders_n)

        offset = 20
        ip_port_list = []
        while len(payload) > offset:
            ip_addr_n = sub_bytes(payload, offset, 4)
            tcp_port_n = sub_bytes(payload, offset+4, 2)
            ip_addr = int2ip(ntohi(ip_addr_n))
            tcp_port = ntohs(tcp_port_n)
            ip_port_list.append((ip_addr, tcp_port))
            offset += 6
        proto_pkt = Udp_Tracker_Announce_response(packet_info, tran_id, interval, leechers, seeders, ip_port_list)
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into udp_tracker_announce_response_protocol (action, transaction_id, `interval`, leechers, seeders, time, src_ip, src_port, dst_ip, dst_port) values "\
              +"(1, "+str(tran_id)+", "+str(interval)+", "+str(leechers)+", "+str(seeders)+", '"+ now + "', '" + str(
            packet_info.sip) + "', '" + str(packet_info.sport) + "', '" + str(packet_info.dip) + "', '" + str(
            packet_info.dport) + "')"
        print(sql)
        self.connect.insert(sql)
        for ip, port in ip_port_list:
            sql = "insert into ip_port_list (transaction_id, time, ip_addr, port) values ("+str(tran_id)+", '"+now+"', '"+str(ip)+"', "+str(port)+")"
            print(sql)
            self.connect.insert(sql)
        self.statistic.add_tracker_pkt(proto_pkt, type='response')
        print(proto_pkt)

    def udp_tracker_scrape__response(self, payload, packet_info):
        tran_id_n = sub_bytes(payload, 4, 4)
        seeders_n = sub_bytes(payload, 16, 4)
        completed_n = sub_bytes(payload, 4, 4)
        leechers_n = sub_bytes(payload, 16, 4)
        tran_id = ntohi(tran_id_n)
        seeders = ntohi(seeders_n)
        completed = ntohi(completed_n)
        leechers = ntohi(leechers_n)
        proto_pkt = Udp_Tracker_scrape_response(packet_info, tran_id, seeders, completed, leechers)
        self.statistic.add_tracker_pkt(proto_pkt, type='response')
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into udp_tracker_scrape_response_protocol (action, transaction_id, seeders, completed, leechers, time, src_ip, src_port, dst_ip, dst_port) values "\
              +"(2, "+str(proto_pkt.transaction_id)+", "+str(proto_pkt.seeders)+", "+str(proto_pkt.completed)+", "+str(proto_pkt.leechers)+", '"+now+"', '"+str(packet_info.sip)+"', '"+str(packet_info.sport)+"', '"+str(packet_info.dip)+"', '"+str(packet_info.dport)+"')"
        print(sql)
        self.connect.insert(sql)
        print(proto_pkt)

    def udp_tracker_error_response(self, payload, packet_info):
        action = 3
        tran_id_n = sub_bytes(payload, 4, 4)
        error_n = sub_bytes(payload, 8, len(payload)-8)
        tran_id = ntohi(tran_id_n)
        error = str(error_n).replace("'", "''")

        proto_pkt = Udp_Tracker_Error_response(packet_info, tran_id, error)
        self.statistic.add_tracker_pkt(proto_pkt, type='response')
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into udp_tracker_error_response_protocol (action, transaction_id,error_message, time, src_ip, src_port, dst_ip, dst_port) values "\
              +"(3, "+str(proto_pkt.transaction_id)+", '"+proto_pkt.error_msg+"', '"+now+"', '"+str(packet_info.sip)+"', '"+str(packet_info.sport)+"', '"+str(packet_info.dip)+"', '"+str(packet_info.dport)+"')"
        print(sql)
        self.connect.insert(sql)
        print(proto_pkt)

    def peer_handshake(self, payload, packet_info):
        protocol_name = 0x13
        protocol_str = str(sub_bytes(payload, 1, 19))
        reserve = sub_bytes(payload, 20, 8)
        sha1_hash = byets2ints(sub_bytes(payload, 28, 20))
        peer_id = byets2ints(sub_bytes(payload, 48, 20))
        proto_pkt = Peer_Handshake(sha1_hash, peer_id,packet_info)
        # self.statistic.add_peer_pkt(proto_pkt)
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into peer_handshake (proto, handshake_str, sha1_hash, peer_id, time, src_ip, src_port, dst_ip, dst_port) values (19, '"+proto_pkt.handshake_str\
              +"', '"+proto_pkt.sha1_hash+"', '"+peer_id+"', '"+now+"', '"+str(packet_info.sip)+"', '"+str(packet_info.sport)+"', '"+str(packet_info.dip)+"', '"+str(packet_info.dport)+"')"
        print(sql)
        self.connect.insert(sql)
        print(proto_pkt)

    def peer_message(self, payload, packet_info):
        length = ntohi(sub_bytes(payload, 0, 4))
        type = byets2ints(sub_bytes(payload, 4, 1))
        data = sub_bytes(payload, 5, len(payload)-5)
        proto_pkt = Peer_Message(length, type, data, packet_info)
        now = datetime.datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        sql = "insert into peer_message (length, type,  time, src_ip, src_port, dst_ip, dst_port) values ("+str(proto_pkt.length)+", "+proto_pkt.type+\
              ", '"+now+"', '"+str(packet_info.sip)+"', '"+str(packet_info.sport)+"', '"+str(packet_info.dip)+"', '"+str(packet_info.dport)+"')"
        print(sql)
        self.connect.insert(sql)
        self.statistic.add_peer_pkt(proto_pkt)
        print(proto_pkt)

