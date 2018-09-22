################################################################################
################################################################################
## Template file for problem 1. You have to fill in the function buyCondition ##
## and expectedValue defined below.                                           ##
## buyCondition takes in three input numbers and returns a boolean            ##
## expectedValue taken in 1 input number and returns a list of floats that    ##
## satisfy the problem statement.                                             ##
## Please ensure you return value is correct as the submission will be        ##
## auto evaluated. We have provided a little helper to ensure that the return ##
## value is correct.                                                          ##
##                                                                            ##
## You can run this template file to see the output of your function.         ##
## First replace the TOTAL_T, CURRENT_T, INPUT_P with correct numbers.        ##
## Then simply run: `python problem1_template.py`                             ##
## You should see the output printed once your program runs.                  ##
##                                                                            ##
## DO NOT CHANGE THE NAME OF THE FUNCTION BELOW. ONLY FILL IN THE LOGIC.      ##
## DONT FORGET TO RETURN THE VALUES CORRECTLY                                 ##
## IF YOU MAKE ANY IMPORTS PUT THEM IN THE BODY OF THE FUNCTION               ##
##                                                                            ##
## You are free to write additional helper functions but ensure they are all  ##
## in this file else your submission wont work.                               ##
##                                                                            ##
## Good Luck!                                                                 ##
################################################################################
################################################################################

TOTAL_T = 0
CURRENT_T = 0
INPUT_P = 0

def buyCondition(total_t, current_t, input_p):
    ##################################
    ##          FILL ME IN          ##
    ##################################

    ## IF YOU WISH TO MAKE ANY SPECIFIC LIBRARY IMPORTS ##
    ## PLEASE PUT THEM IN THE BODY OF THE FUNCTION ##
    ## LIKE SO: import pdb; pdb.set_trace()

    # return a boolean
    return True

def expectedValue(total_t):
    ##################################
    ##          FILL ME IN          ##
    ##################################

    ## IF YOU WISH TO MAKE ANY SPECIFIC LIBRARY IMPORTS ##
    ## PLEASE PUT THEM IN THE BODY OF THE FUNCTION ##
    ## LIKE SO: import pdb; pdb.set_trace()

    # return a list of floats
    return [0.0, 1.0]

def ensureFloat(returnList):
    for num in returnList:
        if type(num) is float:
            continue
        else:
            print(num, ' is not a float.')
            raise TypeError('The return value is not a list of floats')
    return returnList

def ensureListOfFloat(returnList):
    if type(returnList) is list:
        return ensureFloat(returnList)
    else:
        print('Return value is not a list. Please ensure you return a list.')
        raise TypeError('The return value is not a list')

def ensureBoolean(returnValue):
    if type(returnValue) is bool:
        return returnValue
    else:
        print('Return value is not a boolean. Please ensure you return a boolean.')
        raise TypeError('The return value is not a boolean')

if __name__ == "__main__":
    print(ensureBoolean(buyCondition(TOTAL_T, CURRENT_T, INPUT_P)), ensureListOfFloat(expectedValue(TOTAL_T)))
