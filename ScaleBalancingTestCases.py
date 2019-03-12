import ScaleBalancing
import unittest

class ScaleBalancingTestCases(unittest.TestCase): 
    def test_Greater_scaleWeight(self):
        inputValue = '"[3, 4, 5]", "[1, 2, 7, 7]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please only enter 2 positive weights for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Greater_scaleWeight - PASSED")

    def test_Less_scaleWeight(self):
        inputValue = '"[13]", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter 2 positive weights for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Less_scaleWeight - PASSED")

    def test_Negative_scaleWeight(self):
        inputValue = '"[13, -2]", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric values for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Negative_scaleWeight - PASSED")

    def test_NonNumeric_scaleWeight(self):
        inputValue = '"[13, \'A\']", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric values for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case:  NonNumeric_scaleWeight - PASSED")

    def test_NoValue_givenWeight(self):
        inputValue = '"[13, 4]", "[]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter at least 1 positive numeric weight for the Weight Balance")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Negative_scaleWeight - PASSED")

    def test_NonNumeric_givenWeight(self):
        inputValue = '"[13, 4]", "[\'A\', 1, 2]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric values for the Weight Balance (excluding 0)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Negative_scaleWeight - PASSED")

    def test_Zero_givenWeight(self):
        inputValue = '"[13, 4]", "[1, 2, 0]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric value for the Weight Balance (excluding 0)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Negative_scaleWeight - PASSED")

    def test_Negative_givenWeight(self):
        inputValue = '"[13, 4]", "[1, -2, 0]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric value for the Weight Balance (excluding 0)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Negative_scaleWeight - PASSED")

if __name__ == "__main__":
    unittest.main()
