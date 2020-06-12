
class Http_Tracker_Response:
    '''
    存储http tracker request协议的url的特殊字段

    '''

    def __init__(self, packet_info):
        self.packet_info = packet_info
        self.data = None

    def set_data(self, data):
        self.data = data

    def __str__(self):
        show_str = '''http tracker announce request protocol:\n
        %s'''  % (self.packet_info)
        return show_str