from bt_protocol_restore.convert import *
from bt_protocol_restore.protocols.Udp_Tracker_Request import Udp_Tracker_Request
from bt_protocol_restore.protocols.Udp_Tracker_Response import *


class Protocol_Restore:

    def udp_tracker_connect_request(self, payload):
        conn_id_n = sub_bytes(payload, 0, 8)
        action = 0
        tran_id_n = sub_bytes(payload, 12, 4)

        conn_id = ntohq(conn_id_n)
        tran_id = ntohi(tran_id_n)
        proto_pkt = Udp_Tracker_Request(conn_id, action, tran_id)
        print(proto_pkt)


    def udp_tracker_announce_request(self, payload):
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
        info_hash = str(info_hash_n)
        peer_id = str(peer_id_n)
        downloaded = ntohq(downloaded_n)
        left = ntohq(left_n)
        uploaded = ntohq(uploaded_n)
        event = ntohi(event_n)
        ip_addr = ntohi(ip_addr_n)
        key = ntohi(key_n)
        num_want = ntohi(num_want_n)
        port = ntohs(port_n)
        proto_pkt = Udp_Tracker_Request(conn_id, action, tran_id, info_hash_n, peer_id_n, downloaded,
                                        left, uploaded, event, ip_addr, key, num_want, peer_id_n)
        print(proto_pkt)


    def udp_tracker_scrape__request(self, payload):
        conn_id_n = sub_bytes(payload, 0, 8)
        action = 2
        tran_id_n = sub_bytes(payload, 12, 4)

        conn_id = ntohq(conn_id_n)
        tran_id = ntohi(tran_id_n)
        info_hash_list = []
        offset = 16
        while len(payload) == offset:
            info_hash_n = sub_bytes(payload, offset, 20)
            info_hash = str(info_hash_n)
            offset += 20

        proto_pkt =  Udp_Tracker_Request(conn_id, action, tran_id, info_hash_list)

    def udp_tracker_connect_response(self, payload):
        tran_id_n = sub_bytes(payload, 4, 4)
        conn_id_n = sub_bytes(payload, 8, 8)
        tran_id = ntohi(tran_id_n)
        conn_id = ntohq(conn_id_n)
        proto_pkt = Udp_Tracker_Connect_response(tran_id, conn_id)
        print(proto_pkt)



    def udp_tracker_announce_response(self, payload):
        tran_id_n = sub_bytes(payload, 4, 4)
        interval_n = sub_bytes(payload, 8, 4)
        leechers_n = sub_bytes(payload, 12, 4)
        seeders_n = sub_bytes(payload, 16, 4)
        tran_id = ntohi(tran_id_n)
        interval = ntohi(interval_n)
        leechers = ntohi(leechers_n)
        seeders = ntohi(seeders_n)

        off = 20
        ip_port_list = []
        while len(payload) == off:
            ip_addr_n = sub_bytes(payload, off, 4)
            tcp_port_n = sub_bytes(payload, off+4, 8)
            ip_addr = ntohi(ip_addr_n)
            tcp_port = ntohs(tcp_port_n)
            ip_port_list.append((ip_addr, tcp_port))
            off += 6
        proto_pkt = Udp_Tracker_Announce_response(tran_id, interval, leechers, seeders, ip_port_list)
        print(proto_pkt)

    def udp_tracker_scrape__response(self, payload):
        tran_id_n = sub_bytes(payload, 4, 4)
        seeders_n = sub_bytes(payload, 16, 4)
        completed_n = sub_bytes(payload, 4, 4)
        leechers_n = sub_bytes(payload, 16, 4)
        tran_id = ntohi(tran_id_n)
        seeders = ntohi(seeders_n)
        completed = ntohi(completed_n)
        leechers = ntohi(leechers_n)
        proto_pkt = Udp_Tracker_scrape_response(tran_id, seeders, completed, leechers)
        print(proto_pkt)

    def udp_tracker_error_response(self, payload):
        action = 3
        tran_id_n = sub_bytes(payload, 4, 4)
        error_n = sub_bytes(payload, 8, len(payload)-8)
        tran_id = ntohi(tran_id_n)
        error = str(error_n)

        proto_pkt = Udp_Tracker_scrape_response(tran_id, error)


    def peer_handshake(self):
        pass

    def peer_message(self):
        pass

