import struct


def sub_bytes(payload, start, len):
    '''
    获得载荷的一个子字节序列[start, start+len)
    :param start:字节序列在负载中的开始索引
    :param len: 字节序列的长度
    :return: 子字节序列
    '''
    if len(payload) < (start + len):
        raise Exception
    subbytes = payload[start:start + len]
    return subbytes


def ntohs( buffer):
    '''
    将buffer中的网络字节顺序的值转换为主机字节顺序表示的16位有符号整数
    :param buffer: 网络字节顺序
    :return:
    '''
    result = struct.unpack('!h', buffer)
    return result


def ntohi(buffer):
    '''
    将buffer中的网络字节顺序的值转换为主机字节顺序表示的32位有符号整数
    :param buffer: 网络字节顺序
    :return:
    '''
    result = struct.unpack('!i', buffer)
    return result


def ntohq(buffer):
    '''
    将buffer中的网络字节顺序的值转换为主机字节顺序表示的64位有符号整数
    :param buffer: 网络字节顺序
    :return:
    '''
    result = struct.unpack('!q', buffer)
    return result