from scapy.all import *

from bt_capture.Capture import Capture


def test():
    def hello(x):
        print(x.show())

        print(x.type)

    package = sniff(count=100, prn=lambda x: hello(x), promisc=True)  # 扫描eth0网卡的数据包，总数为10个
def test_capture():
    c = Capture()
    c.capture()

def test1():

    TCPlayer = TCP(sport="目标主机端口", dport="自家主机端口")
    # 使用scapy TCP函数构建第二层。

    pkt = IPlayer / TCPlayer  # 组合构建成完整数据包

    send(pkt) # 发送数据包

class send_pollutions:

     def send_udp_announce(self, src, dst):
         a = Ether() / IP(dst='114.114.114.114') / TCP(dport=80)
         send(IP(dst='1.2.3.4') / UDP(dport=123))

if __name__ == '__main__':
    test_capture()
    # test()
    # test1()
    # send_pollutions().send_udp_announce('111','333')