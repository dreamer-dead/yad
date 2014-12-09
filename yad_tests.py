from yad_connection import YadConnection
from yad_protocol import YadProtocol

def test_protocol():
    p = YadProtocol()
    print p.pack_object({'a': 1, 'b': '2'})
    print p._parse_packet_length('1')
    print p._parse_packet_length('1 ')
    print p._parse_packet_length('2 ')
    print p._parse_packet_length('100 ')
    print p._parse_packet_length('1100')
    print p._create_packet('12')
    print p._create_packet('{1111}')

if __name__ == '__main__':
    test_protocol()

