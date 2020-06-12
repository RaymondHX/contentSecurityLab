
class Http_Tracker_Request:
    '''
    存储http tracker request协议的url的特殊字段

    '''

    def __init__(self):
        self.request_field = {}


    def add_field(self, field_key, field_value):
        self.request_field[field_key] = field_value

    def __str__(self):
        pass