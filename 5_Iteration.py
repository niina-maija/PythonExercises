# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:35:42 2023

@author: niina
"""

import numpy as np

# -----------
n = 0
for i in range(1, 4):
    n = n + i
    
#print(n)
# -----------
s = 0
a = [2, 3, 1, 3, 3]
for i in a:
    s += i # note this is equivalent to s = s + i
    
#print(s)
# -----------
'''
dict_a = {"One":1, "Two":2, "Three":3}

for key in dict_a.keys():
    print(key, dict_a[key])
    
for key, value in dict_a.items():
    print(key, value)
'''
# -----------
# Assigning two looping variables:
a = ["One", "Two", "Three"]
b = [1, 2, 3]

#for i, j in zip(a, b):
#    print(i, j)

# -----------    
def have_digits(s):
    
    out = 0
    
    # loop through the string
    for c in s:
        # check if the character is a digit
        if c.isdigit():
            out = 1
            break
            
    return out    

out = have_digits('only4you')
#print(out)
out = have_digits('only for you')
#print(out)

# -----------
# Using the keyword "continue" to skip the print function to print 2
for i in range(5):
    
    if i == 2:
        continue
        
   # print(i)
   
# ----------- 
    
import math

def my_dist_2_points(xy_points, xy):
    """
    Returns an array of distances between xy and the points 
    contained in the rows of xy_points
    
    author
    date
    """
    d = []
    for xy_point in xy_points:
        dist = math.sqrt(\
            (xy_point[0] - xy[0])**2 + (xy_point[1] - xy[1])**2)
        
        d.append(dist)
        
    return d

xy_points = [[3,2], [2, 3], [2, 2]]
xy = [1, 2]
dist = my_dist_2_points(xy_points, xy)
#print(dist)

# -----------

x = np.array([[5, 6], [7, 8]])
n, m = x.shape
s = 0
for i in range(n):
    for j in range(m):
        s += x[i, j]
        
#print(s)

# -----------

i = 0
n = 8

while n >= 1:
    n /= 2
    i += 1
    
#print(f'n = {n}, i = {i}')

# -----------


x = range(5)
y = []

# For-loop:
for i in x:
    y.append(i**2)
print(y)

# List comprehension:
y = [i**2 for i in x]
print(y)

y = [i**2 for i in x if i%2 == 0]
print(y)


# -----------

y = []
for i in range(5):
    for j in range(2):
        y.append(i + j)
print(y)

y = [i + j for i in range(5) for j in range(2)]
print(y)

# -----------
# Dictionary comprehension:
x = {'a': 1, 'b': 2, 'c': 3}

{key:v**3 for (key, v) in x.items()}

print(x)
# -----------






# ------ PROBLEMS---------


y = 0
for i in range(1000):
    for j in range(1000):
        if i == j:
            y += 1

#print(y)

# -----------

def my_max(x):
    m = x[0]
    for i in x:
        if i > m:
            m = i
            
    return m

a = [2, -5, 8, -9, 19, 4]
b = my_max(a)
#print(b)

# -----------

def my_n_max(x, n):
    '''
    Return a list consisting of the n largest 
    elements of x.
    '''
    
    out = []
    x2 = x[:]
    for i in range(n):
        out.append(max(x2))
        x2.remove(max(x2))
        n = n+1
    return out

b = my_n_max(a,4)
print(b)

# -----------

def my_trig_odd_even(m):
    m = np.array(m)
    a,b = m.shape
    q = np.zeros((a,b))
    for i in range(a):
        for j in range(b):
            if m[i,j] %2 == 1: # is odd
                q[i,j] = np.sin(m[i,j])
            elif m[i,j] %2 == 0: # is even
                q[i,j] = np.cos(m[i,j])
    return q

m1 = [[2, 5],[6, 3]]

m2 = my_trig_odd_even(m1)

# -----------

import numpy as np

def my_mat_mult(P, Q):
    a,b = P.shape 
    c,d = Q.shape
    M = np.zeros((a,d))
    
    if b == c:
        for row in range(a):
            for col in range(d):
                for k in range(b):
                    M[row,col] += P[row,k]*Q[k,col]

        # Check
        M1 = np.dot(P,Q)
       # print(M1)
        
        return M
    else:
        print('Matrice multiplication not possible.')
        
P = np.ones((3, 3))
R = my_mat_mult(P, P)
#print(R)

P1 = np.array([[3, -1], [5, 2]])
Q1 = np.array([[1, 4, -3], [0, -2, 6]])
R1 = my_mat_mult(P1, Q1)
#print(R1)

# -----------

def my_saving_plan(P0, i, goal):
    P_n = P0
    years = 0
    while P_n < goal:
        P_new = (1+i)*P_n
        P_n = P_new
        years += 1
    return years

n_years = my_saving_plan(1000, 0.05, 2000)
#print(n_years)

# -----------

def my_find(M):
    ind_list = []
    for i in range(len(M)):
        if M[i] == 1:
            ind_list.append(i)            
        
    return ind_list

M = [1, 0, 1, 1, 0]
q = my_find(M)
#print(q)

# -----------

def my_monopoly_dice():
    
    if 
        n = random.randint(1,6)
        m = random.randint(1,6)
        output = n + m
        
    return output
# -----------






















