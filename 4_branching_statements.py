# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:12:07 2023

@author: niina
"""

import numpy as np

def my_thermo_stat(temp, desired_temp):
    """
    Changes the status of the thermostat based on 
    temperature and desired temperature
    author
    date
    :type temp: Int
    :type desiredTemp: Int
    :rtype: String
    """
    if temp < desired_temp - 5:
        status = 'Heat'
    elif temp > desired_temp + 5:
        status = 'AC'
    else:
        status = 'off'
    return status


def my_circ_calc(r, calc):
    """
    Calculate various circle measurements
    author
    date
    :type r: Int or Float
    :type calc: String
    :rtype: Int or Float
    """
    if calc == 'area':
        return np.pi*r**2
    elif calc == 'circumference':
        return 2*np.pi*r
    


# Problems

def my_tip_calc(bill, party):
    if party < 6:
        tips = bill * 0.15
    elif 6 < party < 8:
        tips: bill * 0.18
    elif 8 < party < 11:
        tips = bill * 0.2
    else:
        tips = bill * 0.25
    
    return tips

t1 = my_tip_calc(109.29,3) 
print(t1)

t = my_tip_calc(109.29,12)
print(t)

def my_mult_operation(a,b,operation):
    
    if operation == "plus":
        out = a + b
    elif operation == "minus":
        out = a - b
    elif operation == "mult":
        out = a * b
    elif operation == "div":
        out = a / b
    elif operation == "pow":
        out = a ** b
    return out


def my_inside_triangle(x,y):
    '''
    Consider a triangle with vertices at (0,0)
, (1,0)
, and (0,1)
. Write a function my_inside_triangle(x,y) where the output 
is the string ‘outside’ if the point (x,y)
 is outside of the triangle, ‘border’ if the point is 
 exactly on the border of the triangle, and ‘inside’ if 
 the point is on the inside of the triangle.
    '''
    if x < 0 or y < 0 or y > 1-x:
        position = "outside"
    elif x == 0 or y == 0 or y == 1-x:
        position = "border"
    elif x > 0 and y > 0 and y < 1-x:
        position = "inside"
    return position


def my_make_size10(x):
    '''
    Write a function my_make_size10(x), where x is an array 
    and output is the first 10 elements of x if x has more 
    than 10 elements, and output is the array x padded with 
    enough zeros to make it length 10 if x has less than 
    10 elements.
    '''
    # Convert input to list
    x = list(x)
    if (len(x)) >= 10:
        size10 = x[:10]
    elif (len(x)) < 10:
        n = 10 - len(x)
        rest = np.zeros(n-1)
        size10 = np.append(x, rest)
    return size10


def my_letter_grader(percent):
    if percent >= 97:
        grade = "A+"
    elif percent >= 93:
        grade = "A"    
    elif percent >= 90:
        grade = "A-"
    elif percent >= 87:
        grade = "B+"
    elif percent >= 83:
        grade = "B"
    elif 60 < percent < 83:
        grade = "B-"
    elif percent < 60:
        grade = "F"
    return grade


def my_nuke_alarm(s1,s2,s3):
    '''
    Consider a nuclear reactor whose temperature is monitored
    by three sensors. An alarm should go off if any two of 
    the sensor readings disagree. Write a function 
    my_nuke_alarm(s1,s2,s3) where s1, s2, and s3 are the 
    temperature readings for sensor 1, sensor 2, and sensor 3, 
    respectively. The output should be the string ‘alarm!’ if 
    any two of the temperature readings disagree by strictly 
    more than 10 degrees and ‘normal’ otherwise.
    '''
    def difference(a,b):
        d = abs(a-b)
        return d
    
    d0 = difference(s1,s2)
    d1 = difference(s1,s3)
    d2 = difference(s2,s3)
    
    if d0 >= 10 and d1 >= 10:
        reelsponse = "alarm!"
    elif d0 >= 10 and d2 >= 10:
        response = "alarm!"
    elif d1 >= 10 and d2 >= 10:
        response = "alarm!"    
    else:
        response = "normal"
    
    return response
import cmath

def my_n_roots(a,b,c):
    
    if b**2 > 4*a*c:
        n_roots = 2
        r1 = (-b + np.sqrt(b**2 - 4*a*c))/(2*a)
        r2 = (-b - np.sqrt(b**2 - 4*a*c))/(2*a)
        r= [r1, r2]
    elif b**2 < 4*a*c:
        n_roots = -2
        r1 = (-b + cmath.sqrt(b**2 - 4*a*c))/(2*a)
        r2 = (-b - cmath.sqrt(b**2 - 4*a*c))/(2*a)
        r= [r1, r2]
    elif b**2 == 4*a*c:
        n_roots = 1
        r1 = -b / (2*a)
        r= [r1]
        
    return n_roots,r


def my_split_function(f,g,a,b,x):
    #Functions as arguments:
    if x<=a:
        return f(x)
    elif x>=b:
        return g(x)
    else:
        return 0

print(my_split_function(np.exp,np.sin,2,4,5))

def my_fun_plus_one(f, x):
    return f(x) + 1