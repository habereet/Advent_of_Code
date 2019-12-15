import unittest
from unittest.mock import patch
from solutionPart1 import *

class tests(unittest.TestCase):
    def test_getFiveDigitIntCode_1(self):
        expected = [0, 0, 0, 0, 1]
        self.assertEqual(expected, getFiveDigitIntCode(1))
        
    def test_getFiveDigitIntCode_3_3_3(self):
        expected = [0, 0, 3, 3, 3]
        self.assertEqual(expected, getFiveDigitIntCode(333))
        
    def test_getValue_position(self):
        expected = 33
        self.assertEqual(expected, value([1002, 4, 3, 4, 33], 0, 1))
        
    def test_getValue_direct(self):
        expected = 3
        self.assertEqual(expected, value([1002, 4, 3, 4, 33], 1, 2))
        
    def test_increaseValueByFour(self):
        expected = 5
        self.assertEqual(expected, increaseValueByFour(1))
        
    def test_increaseValueByTwo(self):
        expected = 3
        self.assertEqual(expected, increaseValueByTwo(1))
    
    def test_addition(self):
        expected = ([2, 4, 3, 4, 8], 4)
        self.assertEqual(expected, addition([2, 4, 3, 4, 33], 0, 0, 1))
    
    def test_multiply(self):
        expected = ([2, 4, 3, 4, 16], 4)
        self.assertEqual(expected, multiply([2, 4, 3, 4, 33], 0, 0, 1))
    
    def test_output(self):
        expected = 2
        self.assertEqual(expected, printIntCodeData([2, 4, 3, 4, 33], 0, 1))
    
    @patch('builtins.input', lambda *args: '1')
    def test_UserInput(self):
        expected = ([3, 4, 3, 1, 33], 3)
        self.assertEqual(expected, userInput([3, 4, 3, 4, 33], 0, 1))

if __name__ == "__main__":
    unittest.main()