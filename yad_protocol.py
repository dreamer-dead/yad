import json

class YadProtocol(object):
    def __init__(self):
        pass

    def pack_object(self, data_obj):
        return self._create_packet(json.dumps(data_obj))

    def _create_packet(self, message):
        return str(len(message)) + ' ' + message

    def read_object(self, socket):
        c = ''
        size_str = ''
        while c != ' ':
            c = socket.recv(1)
            if not c:
                print 'Got end of stream (1)'
                return None
            size_str += c
        if not size_str:
            print 'Got empty size string'
            return None
        answer_size = int(size_str)
        json_data = socket.recv(answer_size)
        return json.loads(json_data) if json_data else None

