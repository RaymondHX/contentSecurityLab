class Peer_Message:
    '''
    peer之间发送消息的协议
    | 长度 | 类型 | 载荷 |
    '''
    def __init__(self, length, type, data, packet_info):
        self.length = length
        self.type = type
        self.data = data
        self.packet_info = packet_info

    def __str__(self):
        show_str = '''peer message protocol:\n%s
         \t length:%s
         \t type:%s
         \t data:%s
         ''' % (
            self.packet_info, self.length, self.type, self.data)
        return show_str