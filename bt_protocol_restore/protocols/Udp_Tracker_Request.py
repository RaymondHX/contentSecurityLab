class Udp_Tracker_Request:
    '''
    用来表示UDP tracker protocol request协议
    分为三种：
        1、connect request
        2、announce request
        3、scrape request

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
    def __init__(self, protocol_id, action, transaction_id,
                 info_hash=None,
                 peer_id=None,
                 downloaded=None,
                 left=None,
                 uploaded=None,
                 event=None,
                 ip_addr=None,
                 key=None,
                 num_want=None,
                 port=None):
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
        show_str = '''protocol_id:%s\n
                    action:%s\n
                    transaction_id:%s\n
                    info_hash:%s\n
                    peer_id:%s\n
                    downloaded:%s\n
                    left:%s\n
                    uploaded:%s\n
                    event:%s\n
                    ip address:%s\n
                    key:%s\n
                    num want:%s\n
                    port:%s\n''' %(self.protocol_id, self.action, self.transaction_id, self.info_hash, self.peer_id,
                                   self.downloaded, self.left, self.uploaded, self.event, self.ip_addr, self.key, self.num_want, self.peer_id)
        return show_str



