import unittest
from main import Elevator
from main import Human


class TestElevator(unittest.TestCase):

    def test_move(self):
        self.assertEqual(self.Elevator_went(2),2)

    def setUp(self):
        self.elevator = Elevator(5, 300)
        self.human = Human()

if __name__ == '__main__':
    unittest.main()
