import struct

from bt_protocol_restore.Protocol_Restore import Protocol_Restore
from bt_protocol_restore.convert import *
from urllib import parse
import re


class Feature_Recognition:

    def __init__(self, show_text):
        self.proto_restore = Protocol_Restore(show_text)
        self.show_text = show_text

    def tcp_recognition(self, payload, packet_info):
        '''
        对tcp数据包进行特征识别
        目前只包括
            peer_handshake协议
            peer_message协议
        :return:
        '''
        sub_rec = [self.tcp_peer_handshake_rec,
                   self.tcp_peer_message_rec,
                   self.tcp_tracker_request_rec,
                   self.tcp_tracker_response_rec]
        pkt_bytes = bytes(payload)
        for rec in sub_rec:
            if rec(pkt_bytes, packet_info) is True:
                return

    def udp_recognition(self, payload, packet_info):
        '''
        对udp数据包进行特征识别
        目前只包括
            tracker_request
            tracker_connect_response
            tracker_announce_response
            tracker_scrape_response
            tracker_erroor_response
        :return:
        '''
        sub_rec = [self.udp_tracker_request_rec,
                   self.udp_tracker_response_rec]

        pkt_bytes = bytes(payload)
        for rec in sub_rec:
            if rec(pkt_bytes, packet_info) is True:
                return


    def http_recognition(self):
        '''
        对http数据包进行特征识别
        目前没有协议
        :return:
        '''
        pass


    def udp_tracker_request_rec(self, payload, packet_info):
        try:
            action_n = sub_bytes(payload, 8, 4)
        except:
            return
        action = ntohi(action_n)
        # connect request
        if len(payload) == 16 and action == 0:
            self.proto_restore.udp_tracker_connect_request(payload, packet_info)
            return True
        # announce request
        elif len(payload) >= 98 and action == 1:
            self.proto_restore.udp_tracker_announce_request(payload, packet_info)
            return True
        # scrape request
        elif (len(payload)-16) % 20 == 0 and action == 2:
            self.proto_restore.udp_tracker_scrape__request(payload, packet_info)
            return True
        return False

    def udp_tracker_response_rec(self, payload, packet_info):
        try:
            action_n = sub_bytes(payload, 0, 4)
        except:
            return
        action = ntohi(action_n)
        # connect response
        if len(payload) == 16 and action == 0:
            self.proto_restore.udp_tracker_connect_response(payload, packet_info)
            return True
        # announce response
        elif (len(payload)-20) % 6 == 0 and action == 1:
            self.proto_restore.udp_tracker_announce_response(payload, packet_info)
            return True
        #  scrape response
        elif (len(payload) - 8) % 12 == 0 and action == 2:
            self.proto_restore.udp_tracker_scrape__response(payload, packet_info)
            return True
        # error response
        elif len(payload) > 8 and action == 3:
            self.proto_restore.udp_tracker_error_response(payload, packet_info)
            return True
        return False

    def tcp_tracker_request_rec(self, payload, packet_info):
        payload_str = str(payload)[2:]
        # http tracker协议
        if payload_str[0:14] == 'GET /announce?':
            # 进行协议恢复
            self.proto_restore.http_tracker_request(payload, packet_info)

    def tcp_tracker_response_rec(self, payload, packet_info):
        payload_str = str(payload)[2:]
        # # http tracker协议
        # print(payload_str[0:14])


        if payload_str[0:15] != 'HTTP/1.1 200 OK':
            return False

        match1 = re.match(r'(.|(\r)|(\n))*(d8:(.|(\r)|(\n))*)', payload_str)
        if match1 is None:
            return False
        self.proto_restore.http_tracker_response(match1.group(4), packet_info)

        return True


    def tcp_peer_handshake_rec(self, payload, packet_info):
        # if packet_info.sip != '192.168.2.101':
        #     print(packet_info)
        try:
            protocol_name = sub_bytes(payload, 0, 1)
        except:
            return
        if len(payload) >=68:
            # print(str(sub_bytes(payload, 1, 19)))
            if protocol_name[0] == 0x13 and str(sub_bytes(payload, 1, 19)) == "b'BitTorrent protocol'":
                self.proto_restore.peer_handshake(payload, packet_info)
                return True

    def tcp_peer_message_rec(self, payload, packet_info):
        # if packet_info.sip != '192.168.2.101':
        #     print(packet_info)
        if len(payload) < 5:
            return False
        type = sub_bytes(payload, 4, 1)
        if (type[0] == 0x00 or type[0] == 0x01 or type[0] == 0x02 or type[0] == 0x03) and len(payload) == 5:
             self.proto_restore.peer_message(payload, packet_info)
             return True
        if type[0] == 0x04 or type[0] == 0x05 or type[0] == 0x06 or type[0] == 0x07 or type[0] == 0x14 :
            cur_bt_offset = 0
            while True:
                if len(payload) - cur_bt_offset == 0:
                    break
                if len(payload) - cur_bt_offset < 5:
                    return False
                # cur_bt_offset后面跟的字节数大于等于5
                length = ntohi(sub_bytes(payload, cur_bt_offset, 4))
                if length < 0:
                    return False
                cur_bt_offset = cur_bt_offset + length + 4

            cur_bt_offset = 0
            while True:
                if len(payload) - cur_bt_offset == 0:
                    break
                length = ntohi(sub_bytes(payload, cur_bt_offset, 4))
                self.proto_restore.peer_message(sub_bytes(payload, cur_bt_offset, length + 4), packet_info)
                cur_bt_offset = cur_bt_offset + length + 4
            return True







