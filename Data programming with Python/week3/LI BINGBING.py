# Assessed exercises 3 
# Notice that there is not an 'Ans:' line in this week's template file.
# Instead, each question has an associated function, with input arguements 
# matching those sqecified in the question. Your functions will be test for a 
# range of different input values, against a model solution, to see if they 
# produce the same answers.

import numpy as np

# Q1 Write a function that takes n, a and b as inputs. The function should
# create a 1D array containing the numbers 0,1,...,n-1 (n elements), multiple 
# every element by a, add b to the 1st element and return the result
def exercise1(n,a,b):
    array1=np.array(range(n))
    array1=array1*a
    array1[0]=array1[0]+b
    return array1
    
# Q2 Write a function that takes n, m, a, b and val as inputs. The function
# should create a n x m matrix (2D array) of zeros, set the entry [a,b] equal
# to val and return this matrix as its output
def exercise2(n,m,a,b,val):
    array2=np.zeros((n,m))
    array2[a][b]=val
    return array2

# Q3 Write a function that takes an array X, and the numbers a and b as inputs, 
# and returns all of the values in X that at greater than a and less than b.
def exercise3(X,a,b):
    array3 =X[np.where((X>a)&(X<b), True, False)]
    return array3

# Q4 Write a function that takes x as an input, converts x from degrees to 
# radians and calculates sin of the x in radians
def exercise4(x):
    x2=np.radians(x)
    print(np.sin(x2)) 