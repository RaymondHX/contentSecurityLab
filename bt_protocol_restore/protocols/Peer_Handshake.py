class Peer_Handshake:
    '''
    表示peer 之间发送数据之前的handshake协议
    | proto | 'BitTorrent protocol' | 保留 | sha1-hash | peer_id |
    '''
    def __init__(self, sha1_hash, peer_id):
        self.proto = 19
        self.handshake_str = 'BitTorrent protocol'
        self.sha1_hash = sha1_hash
        self.peer_id = peer_id