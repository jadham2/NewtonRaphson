'''
===============================================================================
Program Description 
	Create a program to calculate the root of a function given coefficients, a goal value, an initial guess,
    the tolerance, and a maximum amount of iterations. This program should model the Newton-Raphson method.
	
===============================================================================
'''
import numpy as np
import NewtonRaphsonFunctions as func

# User inputs coefficients for the polynomial equation, coefficients are then
# split into a NumPy array to have numerical calculations and NumPy functions to be
# performed upon them.
coef = input("Enter coefficients: ")
coef = coef.split()
for i in range(len(coef)):
    coef[i] = float(coef[i])
coef = np.array(coef)
coef = np.trim_zeros(coef)

# Goal value taken to find the relationship between the x and y value.
# Subtracted from the last value of the array -- the constant.
goalVal = float(input("Enter goal value: "))
coef[-1] = coef[-1] - goalVal

initialGuess = float(input("Enter initial guess: "))

tol = float(input("Enter tolerance: "))

iterate = int(input("Enter maximum allowable interations: "))

# Functions to find initial derivative and value based on the initial guess.
# Functions can be found in the NewtonRaphsonFunctions.py file.
coefOrder = func.findOrder(coef)
deriv = func.findDerivative(coef, initialGuess)
val = func.findValue(coef, initialGuess)

print(f'\nThe polynomial entered is of order: {coefOrder}')

print(f"0: x = {np.format_float_scientific(initialGuess, precision = 4, sign = True, unique = False)} : f(x) = {np.format_float_scientific(val, precision = 4, sign = True, unique = False)} : f\'(x) = {np.format_float_scientific(deriv, precision = 4, sign = True, unique = False)}")

# Root is found by repeating the Newton-Raphson method until it falls below
# a certain tolerance -- indicating that the value the root returns when put
# into the equation is so close to 0 that it can be equated to the true root.
func.findRoot(val, initialGuess, tol, deriv, iterate, coef)
