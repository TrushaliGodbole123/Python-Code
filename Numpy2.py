 #Numpy array vs Python lists
  
#speed :- numpy is faster than pyhton list
#list
#without using numpy it is in pyhton
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []
import time 

start = time.time()
for i in range(len(a)):
  c.append(a[i] + b[i])
print(time.time()-start)


# using numpy 
import numpy as np
a = np.arange(10000000)
b = np.arange(10000000,20000000)

start = time.time()
c = a + b
print(time.time()-start)

print(4.5/0.35)

# memory in python 
a = [i for i in range(10000000)]
import sys

print(sys.getsizeof(a))

#numpy 
a = np.arange(10000000)
print(sys.getsizeof(a))

a = np.arange(10000000,dtype=np.int8)
print(sys.getsizeof(a))    #occupy less memoery

a = np.arange(10000000,dtype=np.int32)
print(sys.getsizeof(a)) #this will occupy less memory as it is 32 bit

#convenience
#numpy is better than python list as it take less time,memory and convenient

#Advanced Indexing

#Normal Indexing and slicing

a = np.arange(24).reshape(6,4)
print(a)

print(a[1,2])

print(a[1:3,1:3])

#Fancy indexing

print(a[[0,2,3]]) #row no.

print(a[:,[0,2,3]]) #print col no.


#boolean Indexing
a = np.random.randint(1,100,24).reshape(6,4)
print(a)

#find all numbers greater than 50

print(a>50)
print(a[a>50]) #print only numbers greater than 50

#find out even numbers
print(a[a%2 == 0])

# find all numbers greater than 50 and are even
print(a[(a > 50) & (a % 2 == 0)])

# find all numbers not divisible by 7
print(a[~(a % 7 == 0)])

# Broadcasting
# The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations.

# The smaller array is “broadcast” across the larger array so that they have compatible shapes.


# same shape
a = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)

print(a)
print(b)

print(a+b)


# diff shape
a = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)

print(a)
print(b)

print(a+b)

# Broadcasting Rules
# 1. Make the two arrays have the same number of dimensions.

# If the numbers of dimensions of the two arrays are different, add new dimensions with size 1 to the head of the array with the smaller dimension.


# 2. Make each dimension of the two arrays the same size.

# If the sizes of each dimension of the two arrays do not match, dimensions with size 1 are stretched to the size of the other array.
# If there is a dimension whose size is not 1 in either of the two arrays, it cannot be broadcasted, and an error is raised.

# More examples

a = np.arange(12).reshape(4,3)
b = np.arange(3)

print(a)
print(b)

print(a+b)

#next
# a = np.arange(12).reshape(3,4)
# b = np.arange(3)
#this will show an error
print(a)
print(b)

print(a+b)

#next
a = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)

print(a)
print(b)

print(a+b)

a = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)

print(a)
print(b)

print(a + b)


#next
a = np.array([1])
# shape -> (1,1)
b = np.arange(4).reshape(2,2)
# shape -> (2,2)

print(a)
print(b)

print(a+b)


# Working with mathematical formulas
a = np.arange(10)
print(np.sin(a))

# sigmoid
def sigmoid(array):
  return 1/(1 + np.exp(-(array)))


a = np.arange(100)

print(sigmoid(a))

# mean squared error
 
actual = np.random.randint(1,50,25) #25bis items
predicted = np.random.randint(1,50,25)

#categorial cross entropy
print(actual)
print(predicted)

#next
def mse(actual,predicted):
  return np.mean((actual - predicted)**2)

print(mse(actual,predicted))


# binary cross entropy HW
np.mean((actual - predicted)**2)

print(actual)

# Working with missing values

# Working with missing values -> np.nan -missing value
a = np.array([1,2,3,4,np.nan,6])
print(a)

print(a[~np.isnan(a)]) #isnan used to ask it is a missing value 
#it is remove missing value


# plotting a 2D plot
# x = y
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100)
y = x

print(plt.plot(x,y))
plt.show()


# y = x^2
x = np.linspace(-10,10,100)
y = x**2

print(plt.plot(x,y))
plt.show()

# y = sin(x)
x = np.linspace(-10,10,100)
y = np.sin(x)

plt.plot(x,y)
plt.show()


# y = xlog(x)
x = np.linspace(0.1,10,100)
y = x * np.log(x)

plt.plot(x,y)
plt.show()


# sigmoid
x = np.linspace(-10,10,100)
y = 1/(1+np.exp(-x))

plt.plot(x,y)
plt.show()


