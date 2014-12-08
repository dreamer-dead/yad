import socket

class Connection(object):
	def __init__(self):
		self.socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

	def connect(self, socket_name):
		self.socket.connnect(socket_name)

	def close(self):
		self.socket.close()

	def send_with_answer(message):
		packet = self._create_packet(message)
		self.socket.sendall(packet)
		c = self.socket.recv()
		answer_packet = ''
		while c and c != ' ':
			answer_packet += c
			c = self.socket.recv()
		len = _parse_packet_length()

	def _create_packet(self, message):
		return str(len(message)) + ' ' + message

	def _parse_packet_length(self, packet):
		if len(packet) <= 1:
			return 0

		space_idx = packet.find(' ')
		return packet[0:space_idx] if space_idx >= 0 else 0


if __name__ == '__main__':
	c = Connection()
	print c._parse_packet_length('1')
	print c._parse_packet_length('1 ')
	print c._parse_packet_length('2 ')
	print c._parse_packet_length('100 ')
	print c._parse_packet_length('1100')
	print c._create_packet('12')
	print c._create_packet('{1111}')
