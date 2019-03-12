import ast

debug_Mode = True

def debug_Print(msg):
    if debug_Mode == True:
        print(msg)

def determineBalance(scale_Weight, given_Weight):
    if (scale_Weight[0] == scale_Weight[1]):
        return "\""
    
    return "Output"

def checkInput(list_Input):
    ## Check Scale Weight Inputs
    scale_Weight = ast.literal_eval(list_Input[0])
    debug_Print(scale_Weight)

    if (len(scale_Weight) > 2):
        print("Error: Please only enter 2 weights for the Balance Scale (left and right side weights)")
        return
    elif (len(scale_Weight) < 2):
        print("Error: Please enter 2 weights for the Balance Scale (left and right side weights)")
        return

    for i in scale_Weight:
        try:
            int(i)
        except ValueError:
            print("Error: Please enter numeric values for the Balance Scale (left and right side weights)")
            return
        
    ## Check Given Weight Inputs
    given_Weight = sorted(ast.literal_eval(list_Input[1]))
    debug_Print(given_Weight)

    if (len(given_Weight) < 1):
        print("Error: Please enter at least 1 numeric weight for the Weight Balance")
        return

    for i in given_Weight:
        try:
            int(i)
        except ValueError:
            print("Error: Please enter numeric values for the Weight Balance (excluding 0)")
            return
        
    for i in given_Weight:
        if (i == 0):
            print("Error: Please enter numeric value for the Weight Balance (excluding 0)")
            return

    return scale_Weight, given_Weight

def main():
    list_Input = input("Input: ") ##"[3, 4]", "[7, 7, 2, 1]"
    scale_Weight, given_Weight = checkInput(ast.literal_eval(list_Input))

    determine_Balance = determineBalance(scale_Weight, given_Weight)
    print(determine_Balance)

if __name__ == "__main__":
    main()
