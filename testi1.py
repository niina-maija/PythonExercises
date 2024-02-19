# -*- coding: utf-8 -*-

import numpy as np

a1 = np.arange(0, 20, 0.5)

b1 = np.linspace(2,8,10)

c1 = np.array([[1, 3, 5],[5, 8, 3]])

#print(b1)
#print(b1.shape)
#print(b1.size)
#print(type(b1))

x = 2
y = 3
del x

x = 10

u = x+y
v = x*y
w = x / y
z = np.sin(x)
r = 8*np.sin(x)
s = 5 * np.sin(x*y)
p = x**y
#print(z)


# Show all the variables
#print("All the variables:")
#%whos

name = "UC Berkeley"
country = 'USA'
print(f"{name} is a great school in {country}.")

S = str(123)
N = float(S)
#print(type(S), type(N))

s1 = "HELLO"
s2 = "hello"
print(s1 == s2)

print("The world ‘Engineering’ has "+ str(len('Engineering'))+ " letters.")
L1 = len("Book")
print("The word ‘Book’ has "+ str(L1)+ " letters")

L2 = "Python is great!"
L3 = L2.split(" ")
print(L3)
# Check if 'Python' is in list L2
a1 = "Python" in L3
print(a1)

# Last word of list L2
print(L3[-1])

list_a = [1, 8, 9, 15] 
list_a.insert(1,2)
list_a.append(4)
list_a1 = sorted(list_a)
L2_list = list(L2)

tuple_a = ("One", 1)
tuple_a[1]

list_b = [2, 3, 2, 3, 1, 2, 5]
set1 = set(list_b)

set_a = {2,3,2}
set_b = {1,2,4}
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a.difference(set_b))

dict_1 = {'A':'a', 'B':'b', 'C':'c'}
dict_1.keys()
'B' in dict_1

print(type(len))
print(type(np.linspace))



