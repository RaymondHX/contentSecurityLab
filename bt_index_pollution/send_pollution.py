from scapy.all import *
from bt_protocol_restore.convert import *
from bt_protocol_restore.Protocol_Restore import *
class send_pollution:


    def send_udp_announce(self, dst):
        eth = Ether()
        IPlayer = IP( dst=dst)
        UDPlayer = UDP(sport=54066, dport = 80)
        # with open("D:\JuniorSpring\信息内容安全\contentSecurityLab\\test\\"+dst+".txt","rb") as f:
        #     data = f.read()
        # ip_addr = "45.168.249.205"
        # ip = socket.inet_aton(ip_addr)
        # data = exchange_bytes(bytearray(data), 84, 4, bytearray(ip))
        # peer_id_array = bytearray(os.urandom(20))
        # data = exchange_bytes(bytearray(data), 36, 20, peer_id_array)
        data = '123435'
        pkt = IPlayer / UDPlayer / data
        send(pkt)


if __name__ == '__main__':
    send_pollution().send_udp_announce("185.181.60.67")