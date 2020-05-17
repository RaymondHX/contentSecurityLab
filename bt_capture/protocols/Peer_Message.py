class Peer_Message:
    '''
    peer之间发送消息的协议
    | 长度 | 类型 | 载荷 |
    '''
    def __init__(self, length, type, payload):
        self.length = length
        self.type = type
        self.payload = payload