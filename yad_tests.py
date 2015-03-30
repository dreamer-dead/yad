import unittest
from yad_protocol import YadProtocol

class TestYadProtocol(unittest.TestCase):

    def test_packobject(self):
        p = YadProtocol()
        self.assertEqual(p.pack_object({'a': 1, 'b': '2'}), '18 {"a": 1, "b": "2"}')

    def test_create_packet(self):
        p = YadProtocol()
        self.assertEqual(p._create_packet('test'), '4 test') 

if __name__ == '__main__':
    unittest.main()
