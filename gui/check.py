
def ip_check(ip_str):
    '''
    检查一个字符串是否为点分十进制ip地址格式，如果是返回True，否则返回False
    :param ip_str: 字符串
    :return:
    '''
    match_result = re.match(r'^\d\d?\d?\.\d\d?\d?\.\d\d?\d?\.\d\d?\d?$', ip_str)
    if match_result is None:
        # 显示错误信息
        return False
    return True


def port_check(port_str):
    '''
    检查一个字符串是否符合一个端口的格式
    端口应该是整数，并且范围在0-65535
    :param port_str:
    :return:
    '''

    try:
        port = int(port_str)
    except ValueError:
        return False
    if port < 0 or port > 65535:
        return False
    return True
