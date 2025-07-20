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

