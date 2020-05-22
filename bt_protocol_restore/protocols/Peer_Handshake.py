class Peer_Handshake:
    '''
    表示peer 之间发送数据之前的handshake协议
    | proto | 'BitTorrent protocol' | 保留 | sha1-hash | peer_id |
    '''
    def __init__(self, sha1_hash, peer_id, packet_info):
        self.proto = 19
        self.handshake_str = 'BitTorrent protocol'
        self.sha1_hash = sha1_hash
        self.peer_id = peer_id
        self.packet_info = packet_info

    def __str__(self):
        show_str = '''peer handshake protocol:\n%s
                \t protocol_id:%s
                \t handshake_str:%s
                \t sha1_hash:%s
                \t peer_id:%s
                ''' % (
        self.packet_info, self.proto, self.handshake_str, self.sha1_hash, self.peer_id)
        return show_str