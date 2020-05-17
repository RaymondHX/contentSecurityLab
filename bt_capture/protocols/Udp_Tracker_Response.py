class Udp_Tracker_Connect_response:
    '''
    表示UDP tracker connect repoonse protocol
    |action|tansaction_id|connection_id|
    action = 0
    '''
    def __init__(self, action, transaction_id, connection_id):
        self.action = action
        self.transaction_id = transaction_id
        self.connection_id = connection_id

class Udp_Tracker_Announce_response:
    '''
    表示UDP tracker announce response protocol
    | action | transaction_id | interval | leechers | seeders | IP address | TCP port|
    action = 1
    '''
    def __init__(self,
                 action,
                 transaction_id,
                 interval,
                 leechers,
                 seeders,
                 ip_addr,
                 tcp_port):
        self.action = action
        self.transaction_id = transaction_id
        self.interval = interval
        self.leechers = leechers
        self.seeders = seeders
        self.ip_addr = ip_addr
        self.tcp_port = tcp_port

class Udp_Tracker_scrape_response:
    '''
    表示UDP tracker scrape response protocol
    | action | transaction_id | seeders | completed | leechers|
    action = 2
    '''
    def __init__(self, action, transaction_id, connection_id):
        self.action = action
        self.transaction_id = transaction_id
        self.connection_id = connection_id

class udp_tracker_error_response:
    '''
    表示UDP tracker error response protocol
    | action | transaction_id | error message |
    '''

    def __init__(self, action, transaction_id, error_msg):
        self.action = action
        self.transaction_id = transaction_id
        self.error_msg = error_msg
