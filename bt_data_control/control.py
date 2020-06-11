from scapy.all import *

class Control:
    #  [(ip, port)]
    block_addr = []

    block_all_flag = False
    def __init__(self):
        pass

    def add_blocked_addr(self, ip, port):
        print('ip:%s, port:%s is bloking' % (ip, port))
        if (ip, port) not in Control.block_addr:
            Control.block_addr.append((ip, port))

    def block(self, n_pkt):
        t_pkt = n_pkt[1]
        print(Control.block_addr)
        if (n_pkt.src, t_pkt.sport) in Control.block_addr:
            IPlayer = IP(dst=n_pkt.src)

            fin_pkt = IPlayer / TCP(sport=t_pkt.dport, dport=t_pkt.sport, flags='FA', seq=t_pkt.ack,
                                    ack=t_pkt.seq + len(t_pkt.payload))

            fin_ack_pkt = sr1(fin_pkt, timeout=5)
            if fin_ack_pkt is None:
                print('对[ip:%s port:%s]阻断失败，正在尝试下一次阻断' % (n_pkt.src, t_pkt.dport))
                return
            last_ack_pkt = IPlayer / TCP(sport=t_pkt.sport, dport=t_pkt.dport, flags='A', ack=fin_ack_pkt.seq + 1)
            send(last_ack_pkt)
            Control.block_addr.remove((n_pkt.src, t_pkt.sport))
            print('block ip:%s, port%s sucessfully' % (n_pkt.src, t_pkt.sport))





