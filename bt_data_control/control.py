

def fin_tcp(t_pkt):
    '''

    :param t_pkt: TCP的包，TCP目的主机必须是我
    :return:
    '''
    print('fin_tcp')
    IPlayer = IP(dst=t_pkt.src)

    fin_pkt = IPlayer / TCP(sport=t_pkt.dport, dport=t_pkt.sport, flags='FA', seq=t_pkt.ack, ack=t_pkt.seq + len(t_pkt.payload))
    fin_ack_pkt = sr1(fin_pkt)
    last_ack_pkt = iplayer / TCP(sport=sport, dport=dport, flags='A', ack=fin_ack_pkt.seq+1)
    send(last_ack_pkt)
    print('send ok')


