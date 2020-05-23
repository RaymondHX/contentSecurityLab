import struct


def sub_bytes(payload, start, length):
    '''
    获得载荷的一个子字节序列[start, start+len)
    :param payload:
    :param start:字节序列在负载中的开始索引
    :param len: 字节序列的长度
    :return: 子字节序列
    '''

    if len(payload) < (start + length):
        raise Exception
    subbytes = payload[start:start + length]
    return subbytes

def ntohs(buffer):
    '''
    将buffer中的网络字节顺序的值转换为主机字节顺序表示的16位有符号整数
    :param buffer: 网络字节顺序
    :return:
    '''
    result = struct.unpack('!h', buffer)
    return result[0]

def ntohi(buffer):
    '''
    将buffer中的网络字节顺序的值转换为主机字节顺序表示的32位有符号整数
    :param buffer: 网络字节顺序
    :return:
    '''
    result = struct.unpack('!i', buffer)
    return result[0]

def ntohq(buffer):
    '''
    将buffer中的网络字节顺序的值转换为主机字节顺序表示的64位有符号整数
    :param buffer: 网络字节顺序
    :return:
    '''
    result = struct.unpack('!q', buffer)
    return result[0]

def int2ip(addr):
    '''
    把32位的int整数转换为点分十进制字符串形式的ip地址
    :param self:
    :param addr:
    :return:
    '''
    ip = str(addr & 0xff)
    for i in range(1, 4):
        ip += '.' + str((addr >> 8 * i) & 0xff)
    return ip