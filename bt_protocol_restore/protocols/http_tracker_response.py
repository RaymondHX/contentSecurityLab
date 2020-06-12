
class Http_Tracker_Response:
    '''
    存储http tracker request协议的url的特殊字段

    '''

    def __init__(self):
        self.data = None

    def data(self, data):
        self.data = data

    def __str__(self):
        pass