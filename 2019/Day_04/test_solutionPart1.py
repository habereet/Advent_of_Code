import unittest
import solutionPart1

class tests(unittest.TestCase):
    def test_RangeGeneration(self):
        expected = [1,2,3,4]
        self.assertEqual(expected, solutionPart1.getPossiblePasswords(1, 4))
    
    def test_SplittingSixDigitNumberIntoIntegers_111111(self):
        expected=[1,1,1,1,1,1]
        self.assertEqual(expected, solutionPart1.splitIntegerIntoDigits(111111))
    
    def test_SplittingSixDigitNumberIntoIntegers_135790(self):
        expected=[1,3,5,7,9,0]
        self.assertEqual(expected, solutionPart1.splitIntegerIntoDigits(135790))
        
    def test_CheckForAdjacentEqualNumbers_112345(self):
        expected=True
        self.assertEqual(expected, solutionPart1.checkForEqualNumbers(112345))
        
    def test_CheckForAdjacentEqualNumbers_111111(self):
        expected=True
        self.assertEqual(expected, solutionPart1.checkForEqualNumbers(111111))
        
    def test_CheckForAdjacentEqualNumbers_123456(self):
        expected=False
        self.assertEqual(expected, solutionPart1.checkForEqualNumbers(123456))
    
    def test_checkForAscending_123456(self):
        expected=True
        self.assertEqual(expected, solutionPart1.checkForAscendingValue(123456))
        
    def test_checkForAscending_654321(self):
        expected=False
        self.assertEqual(expected, solutionPart1.checkForAscendingValue(654321))
    
    def test_allThree_111111(self):
        expected=True
        self.assertEqual(expected, solutionPart1.runAllTests(111111))
    
    def test_allThree_223450(self):
        expected=False
        self.assertEqual(expected, solutionPart1.runAllTests(223450))
    
    def test_allThree_123789(self):
        expected=False
        self.assertEqual(expected, solutionPart1.runAllTests(123789))