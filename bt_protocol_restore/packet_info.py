class Inet_Info:
    '''
    记录在和所在包的信息，包括
    源ip, 目的ip, 源端口, 目的端口, 以及有效载荷长度
    '''
    def __init__(self, sip, dip, sport, dport, pld_len):
        self.sip = sip
        self.dip = dip
        self.sport = sport
        self.dport = dport
        self.pld_len = pld_len

    def __str__(self):
        show_str = "%s[%s]  -->---  %s[%s]   length of payload:%s" \
                   % (self.sip, self.sport, self.dip, self.dport, self.pld_len)
        return show_str

    # def int2ip(self, addr):
    #     ip = str(addr & 0xff)
    #     for i in range(1, 4):
    #         ip += '.' + (addr >> 8 * i) & 0xff
    #     return ip