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
