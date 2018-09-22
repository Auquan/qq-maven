################################################################################
################################################################################
## Template file for problem 2. You have to fill in the function findNumbers  ##
## defined below. The function takes in two input numbers and returns a tuple ##
## of number and a list that satisfy the problem statement.                   ##
## Please ensure you return value is correct as the submission will be        ##
## auto evaluated. We have provided a little helper to ensure that the return ##
## value is correct.                                                          ##
##                                                                            ##
## You can run this template file to see the output of your function.         ##
## First replace the NUM_W and NUM_F with correct numbers.                    ##
## Then simply run: `python problem2_template.py`                             ##
## You should see the output printed once your program runs.                  ##
##                                                                            ##
## DO NOT CHANGE THE NAME OF THE FUNCTION BELOW. ONLY FILL IN THE LOGIC.      ##
## DONT FORGET TO RETURN THE VALUES AS A TUPLE                                ##
## IF YOU MAKE ANY IMPORTS PUT THEM IN THE BODY OF THE FUNCTION               ##
##                                                                            ##
## You are free to write additional helper functions but ensure they are all  ##
## in this file else your submission wont work.                               ##
##                                                                            ##
## Good Luck!                                                                 ##
################################################################################
################################################################################

NUM_W = 0
NUM_F = 0

def findDistribution(num_w, num_f):
    ##################################
    ##          FILL ME IN          ##
    ##################################

    ## IF YOU WISH TO MAKE ANY SPECIFIC LIBRARY IMPORTS ##
    ## PLEASE PUT THEM IN THE BODY OF THE FUNCTION ##
    ## LIKE SO: import pdb; pdb.set_trace()

    # return a tuple, for details of the return value please refer
    # to the problem statement.
    return (2, [-1,2,0])

def ensureNumbers(returnTuple):
    if type(returnTuple[0]) is int:
        for num in returnTuple[1]:
            if type(num) is int:
                continue
            else:
                print(num, ' is not an integer.')
                raise TypeError('The returned tuple does not contain a list of integers')
    else:
        print('Returned tuple does not contain int as first value')
        raise TypeError('The returned tuple does not contain int as first value')
    return returnTuple


def ensureTuple(returnTuple):
    if type(returnTuple) is tuple:
        return ensureNumbers(returnTuple)
    else:
        print('Return value is not a tuple. Please ensure you return a tuple.')
        raise TypeError('The return value is not a tuple.')


if __name__ == "__main__":
    print(ensureTuple(findDistribution(NUM_W, NUM_F)))
