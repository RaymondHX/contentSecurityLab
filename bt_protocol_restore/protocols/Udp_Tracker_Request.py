class Udp_Tracker_Connect_Request:
    '''
    用来表示UDP tracker protocol connect request协议

    +---------------+--------+----------------+
    | connection_id | action | transaction_id |
    +---------------+--------+----------------+
        8(int)        4(int)      4(int)
    '''
    def __init__(self, packet_info, protocol_id, action, transaction_id):
        self.packet_info = packet_info
        self.protocol_id = protocol_id
        self.action = action
        self.transaction_id = transaction_id

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        show_str = '''tracker connect request protocol:\n%s
        \t protocol_id:%s
        \t action:%s
        \t transaction_id:%s\n''' %(self.packet_info, self.protocol_id, self.action, self.transaction_id)
        return show_str

class Udp_Tracker_Announce_Request:
    '''
    用来表示UDP tracker protocol announce request协议

    +---------------+--------+----------------+-----------+---------+------------+
    | connection_id | action | transaction_id | info_hash | peer_id | downloaded |-----|
    +---------------+--------+----------------+-----------+---------+------------+     |
            8(int)     4(int)      4(int)         20(str)    20(str)     8(int)        |
                  |--------------------------------------------------------------------|
                  +------+----------+-------+------------+-----+----------+------+
                  | left | uploaded | event | IP_address | key | num_want | port |
                  +------+----------+-------+------------+-----+----------+------+
                   8(int)   8(int)    4(int)    4(int)    4(int)  4(int)    2(int)
    '''
    def __init__(self, packet_info, protocol_id, action, transaction_id,
                 info_hash,
                 peer_id,
                 downloaded,
                 left,
                 uploaded,
                 event,
                 ip_addr,
                 key,
                 num_want,
                 port):
        self.packet_info = packet_info
        self.protocol_id = protocol_id
        self.action = action
        self.transaction_id = transaction_id
        self.info_hash = info_hash
        self.peer_id = peer_id
        self.downloaded = downloaded
        self.left = left
        self.uploaded = uploaded
        self.event = event
        self.ip_addr = ip_addr
        self.key = key
        self.num_want = num_want
        self.port = port

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        show_str = '''tracker announce request protocol:\n%s
        \t protocol_id:%s
        \t action:%s
        \t transaction_id:%s
        \t info_hash:%s
        \t peer_id:%s
        \t downloaded:%s
        \t left:%s
        \t uploaded:%s
        \t event:%s
        \t ip address:%s
        \t key:%s
        \t num want:%s
        \t port:%s\n''' %(self.packet_info, self.protocol_id, self.action, self.transaction_id, self.info_hash, self.peer_id,
                                   self.downloaded, self.left, self.uploaded, self.event, self.ip_addr, self.key, self.num_want, self.port)
        return show_str

class Udp_Tracker_Scrape_Request:
    '''
    用来表示UDP tracker protocol scrape request协议

    +---------------+--------+----------------+------------+
    | connection_id | action | transaction_id | info_hash+ |
    +---------------+--------+----------------+------------+
         8(int)       4(int)      4(int)         20(str)
    '''
    def __init__(self, packet_info, protocol_id, action, transaction_id,
                 info_hash_list):
        self.packet_info = packet_info
        self.protocol_id = protocol_id
        self.action = action
        self.transaction_id = transaction_id
        self.info_hash_list = info_hash_list

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        show_str = '''tracker scrape request protocol:\n%s
        \t protocol_id:%s
        \t action:%s
        \t transaction_id:%s\n''' % (self.packet_info, self.protocol_id, self.action, self.transaction_id)
        for info_hash in self.info_hash_list:
            show_str += '''
            \t info_hash%s\n''' % (info_hash)
        return show_str



