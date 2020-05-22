class Udp_Tracker_Connect_response:
    '''
    表示UDP tracker connect repoonse protocol
    |action|tansaction_id|connection_id|
    action = 0
    '''
    def __init__(self, transaction_id = None, connection_id = None):
        self.action = 0
        self.transaction_id = transaction_id
        self.connection_id = connection_id

    def set_transaction_id(self, id):
        self.transaction_id = id

    def set_connection_id(self, id):
        self.connection_id = id

class Udp_Tracker_Announce_response:
    '''
    表示UDP tracker announce response protocol
    | action | transaction_id | interval | leechers | seeders | IP address | TCP port|
    action = 1
    '''
    def __init__(self,
                 transaction_id,
                 interval,
                 leechers,
                 seeders,
                 ip_port_list):
        self.action = 1
        self.transaction_id = transaction_id
        self.interval = interval
        self.leechers = leechers
        self.seeders = seeders
        self.ip_port_list = ip_port_list

    def __str__(self):
        show_str = '''
                    action:%s\n
                    transaction_id:%s\n
                    interval:%s\n
                    leechers:%s\n
                    seeders:%s\n''' % (self.action, self.transaction_id, self.interval, self.leechers, self.seeders)
        for ip, port in self.ip_port_list:
            show_str +="ip address:%s\n" \
                       "tcp port:%s\n" % (ip, port)
        return show_str

class Udp_Tracker_scrape_response:
    '''
    表示UDP tracker scrape response protocol
    | action | transaction_id | seeders | completed | leechers|
    action = 2
    '''
    def __init__(self, transaction_id, seeders, completed, leechers):
        self.action = 2
        self.transaction_id = transaction_id
        self.seeders = seeders
        self.completed = completed
        self.leechers = leechers

    def __str__(self):
        show_str = '''
                    action:%s\n
                    transaction_id:%s\n
                    seeders:%s\n
                    completed:%s\n
                    leechers:%s\n''' % (self.action, self.transaction_id, self.seeders, self.completed, self.leechers)
        return show_str

class Udp_Tracker_Error_response:
    '''
    表示UDP tracker error response protocol
    | action | transaction_id | error message |
    '''

    def __init__(self, transaction_id, error_msg):
        self.action = 3
        self.transaction_id = transaction_id
        self.error_msg = error_msg

    def __str__(self):
        show_str = '''
                    action:%s\n
                    transaction_id:%s\n
                    error_msg:%s\n''' % (self.action, self.transaction_id, self.error_msg)
        return show_str

