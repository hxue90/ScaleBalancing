import ast

debug_Mode = True

def debug_Print(msg):
    if debug_Mode == True:
        print(msg)

def checkInput(list_Input):
    ## Check Scale Weight Inputs
    scale_Weight = ast.literal_eval(list_Input[0])
    debug_Print(scale_Weight)

    if (len(scale_Weight) > 2):
        print("Please only enter 2 weights for the Balance Scale (left and right side weights)")
        return
    elif (len(scale_Weight) < 2):
        print("Please enter 2 weights for the Balance Scale (left and right side weights)")
        return

    for i in scale_Weight:
        try:
            int(i)
        except ValueError:
            print("Please enter numeric values for the Balance Scale (left and right side weights)")
            return
    ## Check Given Weight Inputs
    given_Weight = ast.literal_eval(list_Input[1])
    debug_Print(given_Weight)

    for i in given_Weight:
        try:
            int(i)
        except ValueError:
            print("Please enter numeric values for the Weight Balance")
            return

def main():
    list_Input = input("Input: ") ##"[3, 4]", "[1, 2, 7, 7]"
    checkInput(ast.literal_eval(list_Input))

if __name__ == "__main__":
    main()
