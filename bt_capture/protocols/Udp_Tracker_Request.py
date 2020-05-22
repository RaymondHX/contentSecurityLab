
class Udp_Tracker_Request:
    '''
    用来表示UDP tracker protocol request协议
    分为三种：
        1、connect request
        2、announce request
        3、scrape request
    '''
    def __init__(self, protocol_id, action, transaction_id, **kwargs):
        self.protocol_id = protocol_id
        self.action = action
        self.transaction_id = transaction_id
        self.info_hash = kwargs['info_hash']
        self.peer_id = kwargs['peer_id']
        self.downloaded = kwargs['downloaded']
        self.left = kwargs['left']
        self.uploaded = kwargs['uploaded']
        self.event = kwargs['event']
        self.ip_addr = kwargs['ip_addr']
        self.key = kwargs['key']
        self.num_want = kwargs['num_want']
        self.port = kwargs['port']

    def __hash__(self):
        pass

    def __eq__(self, other):
        pass

    def __str__(self):
        pass

