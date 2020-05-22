from scapy.all import *

from bt_capture.Capture import Capture


def test():
    def hello(x):
        print(x.show())

        print(x.type)

    package = sniff(count=1, prn=lambda x: hello(x), promisc=True)  # 扫描eth0网卡的数据包，总数为10个
def test_capture():
    c = Capture()
    c.capture()

if __name__ == '__main__':
    test_capture()
    # test()