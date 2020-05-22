class Udp_Tracker_Connect_response:
    '''
    表示UDP tracker connect repoonse protocol
    +--------+---------------+---------------+
    | action | tansaction_id | connection_id |
    +--------+---------------+---------------+
      4(int)      4(int)          8(int)
    action = 0
    '''
    def __init__(self, packet_info, transaction_id = None, connection_id = None):
        self.packet_info = packet_info
        self.action = 0
        self.transaction_id = transaction_id
        self.connection_id = connection_id

    def set_transaction_id(self, id):
        self.transaction_id = id

    def set_connection_id(self, id):
        self.connection_id = id
    def __str__(self):
        show_str = '''tracker connect response protocol:\n%s
        \t action:%s
        \t transaction_id:%s
        \t connection_id:%s\n''' % (self.packet_info, self.action, self.transaction_id, self.connection_id)
        return show_str

class Udp_Tracker_Announce_response:
    '''
    表示UDP tracker announce response protocol
    +--------+----------------+----------+----------+---------+------------+----------+-------------+
    | action | transaction_id | interval | leechers | seeders | IP address | TCP port | (IP, Port)* |
    +--------+----------------+----------+----------+---------+------------+----------+-------------+
      4(int)       4(int)        4(int)     4(int)     4(int)     4(int)      2(int)
    action = 1
    '''
    def __init__(self,
                 packet_info,
                 transaction_id,
                 interval,
                 leechers,
                 seeders,
                 ip_port_list):
        self.packet_info = packet_info
        self.action = 1
        self.transaction_id = transaction_id
        self.interval = interval
        self.leechers = leechers
        self.seeders = seeders
        self.ip_port_list = ip_port_list

    def __str__(self):
        show_str = '''trakcer announce response protocol:\n%s
        \t action:%s
        \t ransaction_id:%s
        \t interval:%s
        \t leechers:%s
        \t seeders:%s\n''' % (self.packet_info, self.action, self.transaction_id, self.interval, self.leechers, self.seeders)
        for ip, port in self.ip_port_list:
            show_str +="\t ip address:%s\n" \
                       "\t tcp port:%s\n" % (ip, port)
        return show_str

class Udp_Tracker_scrape_response:
    '''
    表示UDP tracker scrape response protocol
    +--------+----------------+---------+-----------+---------+-----+
    | action | transaction_id | seeders | completed | leechers| ... |
    +--------+----------------+---------+-----------+---------+-----+
      4(int)       4(int)       4(int)     4(int)     4(int)
    action = 2
    '''
    def __init__(self, packet_info, transaction_id, seeders, completed, leechers):
        self.packet_info = packet_info
        self.action = 2
        self.transaction_id = transaction_id
        self.seeders = seeders
        self.completed = completed
        self.leechers = leechers

    def __str__(self):
        show_str = '''tracker scrape response protocol:\n%s
        \t action:%s
        \t transaction_id:%s
        \t seeders:%s
        \t completed:%s
        \t leechers:%s\n''' % (self.packet_info, self.action, self.transaction_id, self.seeders, self.completed, self.leechers)
        return show_str

class Udp_Tracker_Error_response:
    '''
    表示UDP tracker error response protocol
    +--------+----------------+---------------+
    | action | transaction_id | error message |
    +--------+----------------+---------------+
      4(int)       4(int)          (str)
    '''

    def __init__(self, packet_info, transaction_id, error_msg):
        self.packet_info = packet_info
        self.action = 3
        self.transaction_id = transaction_id
        self.error_msg = error_msg

    def __str__(self):
        show_str = '''tracker error response message:\n%s
        \t action:%s
        \t transaction_id:%s
        \t error_msg:%s\n''' % (self.packet_info, self.action, self.transaction_id, self.error_msg)
        return show_str

