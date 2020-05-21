class Metainfo:
    '''
    BT协议中的种子文件，该文件通过bencoding进行编码为一个字典。
    字典的键包括下面几个
    announce
    announce list
    creation date
    info
    '''
    pass

class announce:
    '''
    用于表示种子文件中的annoucne项
    '''
    pass

class announce_list:
    '''
    用来表示种子文件中的announce list
    '''
    pass

class info:
    '''
    种子文件中的info
    files:
    name:
    piece length
    piece:
    path:
    '''
    pass

class file:
    '''
    表示info files中的每一个项
    length
    path:
    '''
    pass
