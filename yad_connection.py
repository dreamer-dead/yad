import socket
from yad_protocol import YadProtocol

class YadConnection(object):
    def __init__(self):
        self.protocol = YadProtocol()
        self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    def connect(self, socket_name):
        self.socket.connect(socket_name)

    def close(self):
        self.socket.close()

    def send_with_answer(self, message):
        packet = self.protocol.pack_object(message)
        print '<<<', packet
        self.socket.sendall(packet)
        return self.protocol.read_object(self.socket)

