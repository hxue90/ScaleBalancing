import ScaleBalancing
import unittest

class ScaleBalancingTestCases(unittest.TestCase):
    def test_1_Greater_scaleWeight(self):
        inputValue = '"[3, 4, 5]", "[1, 2, 7, 7]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please only enter 2 positive weights for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Greater_scaleWeight - PASSED\n")

    def test_2_Less_scaleWeight(self):
        inputValue = '"[13]", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter 2 positive weights for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Less_scaleWeight - PASSED\n")

    def test_3_Negative_scaleWeight(self):
        inputValue = '"[13, -2]", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric values for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Negative_scaleWeight - PASSED\n")

    def test_4_NonNumeric_scaleWeight(self):
        inputValue = '"[13, \'A\']", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric values for the Balance Scale (left and right side weights)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case:  NonNumeric_scaleWeight - PASSED\n")

    def test_5_NoValue_givenWeight(self):
        inputValue = '"[13, 4]", "[]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter at least 1 positive numeric weight for the Weight Balance")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: NoValue_givenWeight - PASSED\n")

    def test_6_NonNumeric_givenWeight(self):
        inputValue = '"[13, 4]", "[\'A\', 1, 2]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric values for the Weight Balance (excluding 0)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: NonNumeric_givenWeight - PASSED\n")

    def test_7_Zero_givenWeight(self):
        inputValue = '"[13, 4]", "[1, 2, 0]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric value for the Weight Balance (excluding 0)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Zero_givenWeight - PASSED\n")

    def test_8_Negative_givenWeight(self):
        inputValue = '"[13, 4]", "[1, -2, 0]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), "Error: Please enter positive numeric value for the Weight Balance (excluding 0)")
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: Nagtive_givenWeight - PASSED\n")

    def test_9_1_Weight(self):
        inputValue = '"[3, 4]", "[1, 2, 7, 7]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '1')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: 1_Weight - PASSED\n")

    def test_10_2_Weight(self):
        inputValue = '"[13, 4]", "[1, 2, 3, 6, 14]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '3,6')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: 2_Weight - PASSED\n")
 
    def test_11_2_Weight_Unsorted(self):
        inputValue = '"[13, 4]", "[14, 6, 3, 2, 1]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '3,6')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: 2_Weight_Unsorted - PASSED\n")

    def test_12_No_Weight_Solution(self):
        inputValue = '"[8, 3]", "[8]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), 'No possible solution. Please try again.')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: No_Weight_Solution - PASSED\n")

    def test_13_No_Weight_Needed(self):
        inputValue = '"[8, 8]", "[1, 1]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: No_Weight_Needed - PASSED\n")

    def test_14_IncorrectFormat_scaleBalance(self):
        inputValue = '"[, 8]", "[1, 1]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), 'Error: Please enter the correct format for the Balance Scale')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: IncorrectFormat_scaleBalance - PASSED\n")

    def test_15_IncorrectFormat_givenWeight(self):
        inputValue = '"[8, 8]", "[1, , 1]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), 'Error: Please enter the correct format for the Weight Balance')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: IncorrectFormat_givenWeight - PASSED\n")

    def test_16_2_Weight_Case1(self):
        inputValue = '"[5, 9]", "[1, 2, 6, 7]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '2,6')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: 2_Weight_Case1 - PASSED\n")

    def test_17_2_Weight_Case2(self):
        inputValue = '"[9, 5]", "[1, 2, 6, 7]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '2,6')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: 2_Weight_Case2 - PASSED\n")

    def test_18_2_Weight_Case3(self):
        inputValue = '"[3, 3]", "[1, 1, 2, 2, 3, 3]"'
        print('Input:' + str(inputValue))
        self.assertEqual(str(ScaleBalancing.checkInput(inputValue)), '')
        print('Output:\"' + str(ScaleBalancing.checkInput(inputValue)) + "\"")
        print("Test Case: 2_Weight_Case3 - PASSED\n")

if __name__ == "__main__":
    unittest.main()
