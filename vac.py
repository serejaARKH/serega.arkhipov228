import unittest
from main import Perevorot

class TestPerevorot(unittest.TestCase):
    def test(self):
        self.assertEqual(Perevorot('val'),'lav')

if __name__ == '__main__':
    unittest.main()