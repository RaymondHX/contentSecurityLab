
from scapy.all import *



from Feature_Recognition import Feature_Recognition


class Capture:

    def __init__(self):
        self.rec = Feature_Recognition()

    def capture(self):
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
                    # 进行TCP包的特征识别
                    if not isinstance(t_pkt.payload, NoPayload):
                        self.rec.tcp_recognition(t_pkt[1])
                        print(type(t_pkt[1]))
                        print(str(t_pkt[1]))
                # 处理udp数据包
                elif n_pkt.proto == 0x11:
                    # 获得应用层UDP数据包
                    t_pkt = pkt[2]
                    # 进行UDP包的特征识别
                    if not isinstance(t_pkt.payload, NoPayload):
                        self.rec.udp_recognition(t_pkt.payload)
                        t_pkt.show()
        package = sniff(count=0, prn=lambda x: packet_handler(x), promisc=True)




