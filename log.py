from config import Configure
class Log:
    def __init__(self):
        pass
    def add_log(self, log_info):
        if Configure.log:
            with open("./log.txt", "a+") as f:
                f.write(log_info)


    def delete_logs(self):
        '''
        删除日志的所有内容
        :return:
        '''
        with open("./log.txt", "w") as f:
            pass

