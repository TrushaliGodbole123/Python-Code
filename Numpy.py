# What is numpy?
# NumPy is the fundamental package for scientific computing in Python.it is a python library.

# At the core of the NumPy package, is the ndarray object. This encapsulates n-dimensional arrays of homogeneous data types.

# Numpy Arrays Vs Python Sequences
# NumPy arrays have a fixed size at creation, unlike Python lists (which can grow dynamically). Changing the size of an ndarray will create a new array and delete the original.

# The elements in a NumPy array are all required to be of the same data type, and thus will be the same size in memory.


# Creating Numpy Arrays

# np.array
import numpy as np

a = np.array([1,2,3])
print(a)

# 2D 
b = np.array([[1,2,3],[4,5,6]])
print(b)

# 3D
c = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)

#use of dtype
np.array([1,2,3],dtype=float)

# np.arange
np.arange(1,11,2) #1 for start , 11 for end ,2 is diff

# with reshape
np.arange(16).reshape(2,2,2,2)

# np.ones and np.zeros
np.ones((3,4))

np.zeros((3,4))


# np.random
np.random.random((3,4))

# np.linspace
np.linspace(-10,10,10,dtype=int)

# np.identity
np.identity(3)

# Array Attributes

a1 = np.arange(10,dtype=np.int32)
a2 = np.arange(12,dtype=float).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

a3

# ndim (dimention)
a3.ndim

# shape
print(a3.shape)
print(a3)


# size
print(a2.size)
print(a2)

# itemsize
a3.itemsize

# dtype
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)


# Changing Datatype

# astype
a3.astype(np.int32)
print(a3)

# Array Operations

a1 = np.arange(12).reshape(3,4)
a2 = np.arange(12,24).reshape(3,4)

print(a2)

# scalar operations

# arithmetic
print(a1 ** 2)


# relational
print(a2 == 15)

# vector operations
# arithmetic
print(a1 ** a2)

# Array Functions

a1 = np.random.random((3,3))
a1 = np.round(a1*100)
print(a1)

# max/min/sum/prod
# 0 -> col and 1 -> row
print(np.prod(a1,axis=0))

# mean/median/std/var
np.var(a1,axis=1)

# trigonomoetric functions
np.sin(a1)


# dot product
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(12,24).reshape(4,3)

print(np.dot(a2,a3))


# log and exponents
print(np.exp(a1))

# round/floor/ceil

np.ceil(np.random.random((2,3))*100)

# Indexing and Slicing

a1 = np.arange(10)
a2 = np.arange(12).reshape(3,4)
a3 = np.arange(8).reshape(2,2,2)

print(a3)

print(a1)
print(a2)

print(a2[1,0])

print(a3[1,0,1])

#slicing
print(a1[2:5:2])

a2[0:2,1::2]

a2[::2,1::2]

a2[1:,1:3]

#slicing on 3d array
a3 = np.arange(27).reshape(3,3,3)
print(a3)

print(a3[::2,0,::2])

print(a3[0,1,:])

# Iterating

a1

for i in a1:
  print(i)
  
  #next
for i in a2:
  print(i)
  
print(a3)


for i in a3:
  print(i)
  
for i in np.nditer(a3):
   print(i)
   
   
# Reshaping

# reshape

# Transpose
np.transpose(a2)
print(a2.T)

# ravel
print(a3.ravel())

#some Practice question using Numpy 
#1. Create a full vector of size 10 but the fifth value which is 1.

import numpy as np 
a =np.nan * np.empty(10)
a[4]=1
print(a)

#2. Ask User to input two numbers a, b . write a program to generate a random array of shape (a,b) and print the array and avg of the array.
a,b = map(int ,input("Enter two numbers:").split())
x = np.random.random((a,b))
print(x)
print(x.mean())

#3. write a function to create a 2d array with 1 on the border and 0 inside.
#take 2-d array shape as (a,b) as parameter to function.

a= np.ones((4,5))
a[1:-1,1:-1]=0
print(a)

#OR

def borderArray(a,b):
  x=np.ones((a,b))
  x[1:-1,1:-1]=0
  return x
borderArray(3,4)

#4. create a vector of size 10 with value ranging from 0 to 1, both excluded.
print(np.linspace(0,1,12)[1:-1])

#5. can you create a identity matrix of shape (3,4). if yes write code for it.
#No. but it can look like this (3,3)

print(np.eye(3))
print(np.identity(4))

#6. create a 5x5 matrix with row value ranging from 0 to 4.
z= np.zeros((5,5))
z+= np.arange(5)
print(z)

#7.considet a random integer (in range 1 to 100) vector with shape (10,2) representing 
# coordinates,and coordinates of a point as array is given. create an array of distance of each 
# point in the random vectors from the given point. distance array should be integer type.
# point = np.array([2,3])

a= np.random.randint(1,100,(10,2))
p= np.array([2,3])
print(a)
print(np.sqrt(np.sum((a-p)**2,axis=1)).astype(int))

#8. consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th elements?

# a=np.zeros((6,7,8))
# print(a)
print(np.unravel_index(100,(6,7,8)))


#9. Arrays : you are given a space separated list of numbers . your task is to print a reversed numpy array with the element type float.

a=input("enter number:").strip().split()
print(np.array(a[::-1],dtype=np.float32))

#10. Element count  : count the number of a numpy array.

a = np.array([3,4])
b = np.array((2,3,4))
print(a.size)
print(b.size)

#11. softmax Function :Create a python function to calculate the softmax of the given numpy 1D araay.
# the Function only accepts the numpy 1D array. otherwise raise error.

def softmax(arr):
  if type(arr) != np.ndarray:
    raise TypeError("Requires Numpy Array")
  elif arr.ndim>1:
    raise TypeError("Requires 1D Array")
  s = np.sum(np.exp(arr))
  return np.exp(arr)/s
print(softmax (np.arange(5)))

#12. Vertical stack 
# write a python function that accepts infinite number of numpy array and do the vertical stack to them .
# then return that new array as result .The function only accepts the numpy array,otherwise raise error.

def vertical_stack(*args):
  return np.vstack(args)

a = np.arange(10).reshape(2,-1)
print("a=",a)
b = np.repeat(1,10).reshape(2,-1)
print("b=",b)
print(vertical_stack(a,b))
c = np.random.random((2,5))
print("c=",c)
vertical_stack(a,b,c)

