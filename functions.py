# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 18:05:59 2023

@author: niina
"""

import numpy as np

def my_fun(a, b):
    '''
    Descriptive String
    This is best function.
    '''
    # comments about the statements
    
    p1 = a*b
    
    return(p1)

def print_greeting(day = 'Monday', name = 'Qingkai'):
    print(f'Greetings, {name}, today is {day}')
    
    
def my_test(a, b):
    x = a + b
    y = x * b
    z = a + b
    
    m = 2
    
    print(f'Within function: x={x}, y={y}, z={z}')
    return x, y


n = 42

def func():
    global n
    print(f'Within function: n is {n}')
    n = 3
    print(f'Within function: change n to {n}')

func()
print(f'Outside function: Value of n is {n}')


#Distance calculator with a nested function:
def my_dist_xyz(x, y, z):
    """
    x, y, z are 2D coordinates contained in a tuple
    output:
    d - list, where
        d[0] is the distance between x and y
        d[1] is the distance between x and z
        d[2] is the distance between y and z
    """
    
    def my_dist(x, y):
        """
        subfunction for my_dist_xyz
        Output is the distance between x and y, 
        computed using the distance formula
        """
        out = np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
        return out
    
    d0 = my_dist(x, y)
    d1 = my_dist(x, z)
    d2 = my_dist(y, z)
    
    return [d0, d1, d2]

#Distance calculator without a nested function:
def my_dist_xyz_2(x, y, z):
    """
    x, y, z are 2D coordinates contained in a tuple
    output:
    d - list, where
        d[0] is the distance between x and y
        d[1] is the distance between x and z
        d[2] is the distance between y and z
    """
    
    d0 = np.sqrt((x[0]-y[0])**2+(x[1]-y[1])**2)
    d1 = np.sqrt((x[0]-z[0])**2+(x[1]-z[1])**2)
    d2 = np.sqrt((y[0]-z[0])**2+(y[1]-z[1])**2)
    
    return [d0, d1, d2]


# Lambda functions:
    
square = lambda x: x**2

print(square(2))
print(square(5))

# Equivalent normal function:
    
def square_1(x):
    return x**2

# Functions as arguments to functions:
    
f = max

def my_fun_plus_one(f, x):
    return f(x) + 1

print(my_fun_plus_one(np.sqrt, 4))

# Same with lambda function:

print(my_fun_plus_one(lambda x: np.sqrt(x), 4))




# Problems:
    
def my_sinh(x):
    s = ((np.exp(x) - np.exp(-x))/2.0)
    return s

# function to print Checkerboard pattern
def my_checker_board(n):
    # create a n * n matrix
    a = np.ones((n,n), dtype = int)
    
    # fill with 0 the alternate cells in rows and columns
    a[1::2, ::2] = 0
    a[::2, 1::2] = 0
    return a

def my_triangle(b,h):
    a = (b*h)/2.0
    return a

def my_split_matrix(m):
    half = m[0].size//2 + 1
    m1 = m[:,:half]
    m2 = m[:,half:]
    return m1, m2

def my_odds(a: np.array):
    odd_list = []
    for i in a:
        if i%2 == 1:
           #print(i)
           odd_list.append(i)
           #print(odd_list)
    return len(odd_list)


