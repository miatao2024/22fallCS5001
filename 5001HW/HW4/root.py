'''
    CS5001, Mohammad Toutiaee
    Homework 4, 11/29/2022
    Fall 2022
    Minjia Tao
'''
#1.


def root(n, number, accuracy = 0.001) :
    """
    2 required parameters and one optional1 parameter
    Arguments:
        • n, an integer > 1 representing which root to calculate;
        • number, an integer or float >= 1 whose root is to be calculated;
        • (optional) accuracy, a float between 0.0 and 1.0, defaulting to 0.001.
    return:
        the nth root of a number that falls within the range of abs(targeted number - accuracy). 
        If any of the actual parameters provided by the caller violate these constraints, 
        the function should simply return -1.
    """
    if not(n > 1 and isinstance(n, int)) or \
        not(number >= 1 and (isinstance(number, int) or isinstance(number, float))) \
        or not(0.0 <= accuracy <= 1.0 and isinstance(accuracy, float)): #check the validity of parameters
        return -1                    #if any violates, return -1
    left = 1                     #binary search method, initialize lower bound = 1
    right = number               #initialize higher bound = number
    while left <= right:         #set the valid condition to do binary search thoroughly
        mid = (left + right) / 2 #initialize mid as the average of left and right
        guess = mid ** n         #initialize the guess 
        if -accuracy <= guess - number <= accuracy:  #if the guess meet the required accuracy
            return mid           #then we find our answer
        if guess < number:       # if the guess smaller than the number
            left = mid           # then we increase our lower bound
        else:                    # if the guess greater than the number
            right = mid          # then we decrease our higher bound

