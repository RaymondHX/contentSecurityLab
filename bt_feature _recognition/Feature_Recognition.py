import struct

from bt_protocol_restore.Protocol_Restore import Protocol_Restore
from bt_protocol_restore.convert import *


class Feature_Recognition:

    def __init__(self):
        self.proto_restore = Protocol_Restore()


    def tcp_recognition(self, payload):
        '''
        对tcp数据包进行特征识别
        目前只包括
            peer_handshake协议
            peer_message协议
        :return:
        '''
        pass

    def udp_recognition(self, payload):
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
            if rec() is True:
                return


    def http_recognition(self):
        '''
        对http数据包进行特征识别
        目前没有协议
        :return:
        '''
        pass


    def udp_tracker_request_rec(self, payload):
        action_n = sub_bytes(payload, 8, 4)
        action = ntohi(action_n)
        # connect request
        if len(payload) == 16 and action == 0:
            self.proto_restore.udp_tracker_connect_request(payload)
            return True
        # announce request
        elif len(payload) == 98 and action == 1:
            self.proto_restore.udp_tracker_announce_request(payload)
            return True
        # scrape request
        elif (len(payload)-16) % 20 == 0 and action == 2:
            self.proto_restore.udp_tracker_scrape__request(payload)
            return True
        return False


    def udp_tracker_response_rec(self, payload):
        action_n = sub_bytes(payload, 0, 4)
        action = ntohi(action_n)
        # connect response
        if len(payload) == 16 and action == 0:
            self.proto_restore.udp_tracker_connect_response(payload)
            return True
        # announce response
        elif (len(payload)-20) % 6 == 0 and action == 1:
            self.proto_restore.udp_tracker_announce_response(payload)
            return True
        #  scrape response
        elif (len(payload) - 8) % 12 == 0 and action == 1:
            self.proto_restore.udp_tracker_scrape__response(payload)
            return True
        # error response
        elif len(payload) > 8 and action == 1:
            self.proto_restore.udp_tracker_error_response(payload)
            return True
        return False


    def tcp_peer_handshake_rec(self):
        pass

    def tcp_peer_message_rec(self):
        pass







