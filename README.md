# ScaleBalancing
------------------------------------------
Description
------------------------------------------
ScaleBalancing is a script which accepts two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being a list of available weights as positive integers. 
The ScaleBalancing will determine if you can balance the scale by using the least amounts of weights from the list, but using at most 2 weights in ascending order. ScaleBalancing will only use the available weights from the list once.

------------------------------------------
How To Use
------------------------------------------
ScaleBalancing will prompt a user to provide an input in the format "[X],[Y]", where X (13, 4) is two positive integer with a comma and Y (1, 2, 3, 6, 14) is 1 or more positive integer with a comma. ScaleBalancing will provide a user with the output in the format "Z", where Z (2,6) is 1 or 2 positive integer with a comma.

For Example:
ScaleBalancing prompts a user to provide an input
  Input:
A user inputs "[5, 9]", "[1, 2, 6, 7]"
  Input:"[5, 9]", "[1, 2, 6, 7]"
ScaleBalancing will provide a user with the output
  Input:"[5, 9]", "[1, 2, 6, 7]"
  Output:"2,6"
  
------------------------------------------
Test Strategies
------------------------------------------
There are 18 test cases in total for ScaleBalancing.

Test Cases:
1. Greater_scaleWeight
  Test Coverage: This test case is to verify a user can not enter more then 2 positive integer for the ScaleBalancing scale weight.
  
  Input:"[3, 4, 5]", "[1, 2, 7, 7]"
  
  Output:"Error: Please only enter 2 positive weights for the Balance Scale (left and right side weights)"
2. Less_scaleWeight
  Test Coverage: This test case is to verify a user can not enter less then 2 positive integer for the ScaleBalancing scale weight.
    
  Input:"[13]", "[1, 2, 3, 6, 14]"
  
  Output:"Error: Please enter 2 positive weights for the Balance Scale (left and right side weights)"
3. Negative_scaleWeight
  Test Coverage: This test case is to verify a user can not enter a negative integer for the ScaleBalancing scale weight.
    
  Input:"[13, -2]", "[1, 2, 3, 6, 14]"
  
  Output:"Error: Please enter positive numeric values for the Balance Scale (left and right side weights)"
4. NonNumeric_scaleWeight
  Test Coverage: This test case is to verify a user can not enter a non-numeric value for the ScaleBalancing scale weight.
    
  Input:"[13, 'A']", "[1, 2, 3, 6, 14]"
  
  Output:"Error: Please enter positive numeric values for the Balance Scale (left and right side weights)"
5. NoValue_givenWeight
  Test Coverage: This test case is to verify a user can not enter no numeric value for the ScaleBalancing weights available.
  
  Input:"[13, 4]", "[]"
  
  Output:"Error: Please enter at least 1 positive numeric weight for the Weight Balance"
6. NonNumeric_givenWeight
  Test Coverage: This test case is to verify a user can not enter a non-numeric value for the ScaleBalancing weights available.
    
  Input:"[13, 4]", "['A', 1, 2]"
  
  Output:"Error: Please enter positive numeric values for the Weight Balance (excluding 0)"
7. Zero_givenWeight
  Test Coverage: This test case is to verify a user can not enter a zero for the ScaleBalancing weights available.
    
  Input:"[13, 4]", "[1, 2, 0]"
  
  Output:"Error: Please enter positive numeric value for the Weight Balance (excluding 0)"
8. Negative_givenWeight
  Test Coverage: This test case is to verify a user can not enter a negative integer for the ScaleBalancing weights available.
    
  Input:"[13, 4]", "[1, -2, 0]"
  
  Output:"Error: Please enter positive numeric value for the Weight Balance (excluding 0)"
9. 1_Weight
  Test Coverage: This test case is to verify a user is provided with the correct output for the ScaleBalancing when only 1 weight is need.
    
  Input:"[3, 4]", "[1, 2, 7, 7]"
  
  Output:"1"
10. 2_Weight
  Test Coverage: This test case is to verify a user is provided with the correct output for the ScaleBalancing when 2 weight is need.
    
  Input:"[13, 4]", "[1, 2, 3, 6, 14]"
  
  Output:"3,6"
11. 2_Weight_Unsorted
  Test Coverage: This test case is to verify a user is provided with the correct output for the ScaleBalancing when only 2 weight is need and a user provided an unsorted input.
    
  Input:"[13, 4]", "[14, 6, 3, 2, 1]"
  
  Output:"3,6"
12. No_Weight_Solution
  Test Coverage: This test case is to verify a user is provided with the correct output for the ScaleBalancing when there is no solution.
    
  Input:"[8, 3]", "[8]"
  
  Output:"No possible solution. Please try again."
13. No_Weight_Needed
  Test Coverage: This test case is to verify a user is provided with the correct output for the ScaleBalancing when no weight is need.
    
  Input:"[8, 8]", "[1, 1]"
  
  Output:""
14. IncorrectFormat_scaleBalance
  Test Coverage: This test case is to verify a user can not enter incorrect format for the ScaleBalancing scale weight.
    
  Input:"[, 8]", "[1, 1]"
  
  Output:"Error: Please enter the correct format for the Weight Balance"
15. IncorrectFormat_givenWeight
  Test Coverage: This test case is to verify a user can not enter incorrect format for the ScaleBalancing weights available.
    
  Input:"[8, 8]", "[1, , 1]"
  
  Output:"Error: Please enter the correct format for the Weight Balance"
16. 2_Weight_Case1
  Test Coverage: This test case is to verify a user is provided with the correct output.
    
  Input:"[5, 9]", "[1, 2, 6, 7]"
  
  Output:"2,6"
17. 2_Weight_Case2
  Test Coverage: This test case is to verify a user is provided with the correct output.
    
  Input:"[9, 5]", "[1, 2, 6, 7]"
  
  Output:"2,6"
18. 2_Weight_Case3
  Test Coverage: This test case is to verify a user is provided with the correct output.
    
  Input:"[3, 3]", "[1, 1, 2, 2, 3, 3]"
  
  Output:""
