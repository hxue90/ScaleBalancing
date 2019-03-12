import ScaleBalancing
import unittest

class ScaleBalancingTestCases(unittest.TestCase): 
    def test_Greater_scaleWeight(self):
        print('Input:"[3, 4]", "[1, 2, 7, 7]"')
        self.assertEqual(str(ScaleBalancing.checkInput('"[3, 4]","[7, 7, 2, 1]"')), "1")
        print('Output:\"' + str(ScaleBalancing.checkInput('"[3, 4]","[7, 7, 2, 1]"')) + "\"")
        print("Test Case: Greater_scaleWeight - PASSED")

    def test_Less_scaleWeight(self):
        print('\nInput:"[13, 4]", "[1, 2, 3, 6, 14]"')
        self.assertEqual(str(ScaleBalancing.checkInput('"[13, 4]", "[1, 2, 3, 6, 14]"')), "3,6")
        print('Output:\"' + str(ScaleBalancing.checkInput('"[13, 4]", "[1, 2, 3, 6, 14]"')) + "\"")
        print("Test Case: Less_scaleWeight - PASSED")
              
if __name__ == "__main__":
    unittest.main()
