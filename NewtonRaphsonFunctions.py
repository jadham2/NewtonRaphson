'''
===============================================================================
Program Description 
	Create a program to calculate the root of a function given coefficients, a goal value, an initial guess,
    the tolerance, and a maximum amount of iterations.

===============================================================================
'''
import numpy as np

# Finds the order of the function and returns it. Size of coefficient list minus one.
def findOrder(coefList):
    order = np.size(coefList) - 1
    return order

# Function to find the derivative given the coefficient list and x value.
def findDerivative(coefList, xVal):
    derivative = 0
    # Adds value of derivative for every number in the coefficient list.
    for i in range(np.size(coefList)):
        derivative += (np.size(coefList) - i - 1) * coefList[i] *  pow(xVal, (np.size(coefList) - 2 - i))
    return derivative

# Function to find the value given the coefficient list and the x value.
def findValue(coefList, xVal):
    value = 0
    # Adds value of each coefficient-xvalue-exponent combo to the total value.
    for i in range(np.size(coefList)):
        value += coefList[i] * pow(xVal, (np.size(coefList) - 1 - i))
    return value

# Function to find the root given the parameters.
def findRoot(value, xVal, tolerance, derivative, iterations, coefList):
    iter = 0
    # function repeats while the absolute value of the value is
    # greater than / equal to the tolerance.
    while abs(value) >= tolerance:
        if derivative == 0: # Avoids divide by zero errors.
            break
        iter += 1
        if iter > iterations: # Breaks once the user reaches the maximum amount of specified iterations.
            break
        xVal = xVal - (value/derivative) # Root finding formula -- Newton-Raphson method.
        # Calls value and derivative function to compute values for the next iteration.
        value = findValue(coefList, xVal)
        derivative = findDerivative(coefList, xVal)
        print(f"{iter}: x = {np.format_float_scientific(xVal, precision = 4, sign = True, unique = False)} : f(x) = {np.format_float_scientific(value, precision = 4, sign = True, unique = False)} : f\'(x) = {np.format_float_scientific(derivative, precision = 4, sign = True, unique = False)}")
    if iter > iterations:
        print("Error 1. Maximum iterations reached.")
    elif derivative == 0:
        print("Error 2. Derivative is zero: divide by zero error.")
    else:
        print(f'A solution was estimated to be {np.format_float_scientific(xVal, precision = 4, sign = True, unique = False)}')
        print(f'Total number of iterations: {iter}')
    return
