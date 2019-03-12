import ast

debug_Mode = True

def debug_Print(msg):
    if debug_Mode == True:
        print(msg)

def requestInput():
    list_Input = input("Input: ") ##"[3, 5, 4]", "[1, 2, 7, 7]"
    list_Input = ast.literal_eval(list_Input)
    
    ## Check Scale Weight Inputs
    scale_Weight = ast.literal_eval(list_Input[0])
    debug_Print(scale_Weight)
    
    ## Check Given Weight Inputs
    given_Weight = ast.literal_eval(list_Input[1])
    debug_Print(given_Weight)

def main():
    ## Requesting Input
    requestInput()

main()
