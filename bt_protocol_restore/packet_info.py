class Inet_Info:
    '''
    记录载荷所在包的信息，包括
    源ip, 目的ip, 源端口, 目的端口, 以及有效载荷长度,传输层的整个数据包
    '''
    def __init__(self, sip, dip, sport, dport, pld_len, t_pkt):
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.pld_len = pld_len
        self.t_pkt = t_pkt

    def __str__(self):
        show_str = "%s[%s]  -->---  %s[%s]   length of payload:%s" \
                   % (self.sip, self.sport, self.dip, self.dport, self.pld_len)
        return show_str

