
from scapy.all import *
from Feature_Recognition import Feature_Recognition
from bt_protocol_restore.packet_info import Inet_Info


class Capture:

    def __init__(self):
        self.rec = Feature_Recognition()
        self.stop_flag = False

    def capture(self):
        def stop_handler(pkt):
            return self.stop_flag

        def packet_handler(pkt):
            # 仅处理IPv4数据包
            if pkt.type == 0x0800:
                # 网络层数据包即IP数据包
                n_pkt = pkt[1]
                # bytess = bytes(n_pkt)
                # print(hex(bytess[0]))
                # 处理TCP数据包
                if n_pkt.proto == 0x06:
                    # 获得应用层TCP数据包
                    t_pkt = pkt[2] # n_pkt[1]
                    # 获得该包的ip地址，port以及载荷长度(tcp载荷长度)
                    packet_info = Inet_Info(n_pkt.src, n_pkt.dst, t_pkt.sport, t_pkt.dport, len(t_pkt.payload))

                    # 进行TCP包的特征识别
                    if not isinstance(t_pkt.payload, NoPayload):
                        self.rec.tcp_recognition(t_pkt.payload, packet_info)
                # 处理udp数据包
                elif n_pkt.proto == 0x11:
                    # 获得应用层UDP数据包
                    t_pkt = pkt[2]
                    # 获得该包的ip地址，port以及载荷长度(udp载荷长度)
                    packet_info = Inet_Info(n_pkt.src, n_pkt.dst, t_pkt.sport, t_pkt.dport, len(t_pkt.payload))
                    # 进行UDP包的特征识别
                    if not isinstance(t_pkt.payload, NoPayload):
                        self.rec.udp_recognition(t_pkt.payload, packet_info)

        self.stop_flag = False
        package = sniff(count=1000, prn=lambda x: packet_handler(x), promisc=False, stop_filter = lambda x:stop_handler(x))#, filter='ip host 185.181.60.67')


    def stop_capture(self):
        self.stop_flag = True


