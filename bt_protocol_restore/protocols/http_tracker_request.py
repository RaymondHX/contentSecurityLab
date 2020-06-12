
class Http_Tracker_Request:
    '''
    存储http tracker request协议的url的特殊字段

    '''

    def __init__(self, packet_info):
        self.packet_info = packet_info
        self.request_field = {}


    def add_field(self, field_key, field_value):
        self.request_field[field_key] = field_value

    def __str__(self):
        show_str = 'http tracker announce request protocol:\n%s\n' % (str(self.packet_info))
        for k, v in self.request_field.items():
            show_str += '\t%s:%s\n' %(k, v)
        return show_str