#Numpy tricks

# np.sort
# Return a sorted copy of an array.

# code
import numpy as np
a = np.random.randint(1,100,15)
print(a)

b = np.random.randint(1,100,24).reshape(6,4)
print(b)

print(np.sort(a)[::-1])

print(np.sort(b,axis=0))

# np.append
# The numpy.append() appends values along the mentioned axis at the end of the array

# code
print(np.append(a,200))

print(b)


print(np.append(b,np.random.random((b.shape[0],1)),axis=1))

# np.concatenate
# numpy.concatenate() function concatenate a sequence of arrays along an existing axis.

# code
c = np.arange(6).reshape(2,3)
d = np.arange(6,12).reshape(2,3)

print(c)
print(d)


print(np.concatenate((c,d),axis=0))

print(np.concatenate((c,d),axis=1))

# np.unique
# With the help of np.unique() method, we can get the unique values from an array given as parameter in np.unique() method.

# code
e = np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(np.unique(e))

# np.expand_dims
# With the help of Numpy.expand_dims() method, we can get the expanded dimensions of an array

# code
print(a.shape)


print(np.expand_dims(a,axis=0).shape)

print(np.expand_dims(a,axis=1))

# np.where
# The numpy.where() function returns the indices of elements in an input array where the given condition is satisfied.

print(a)

# find all indices with value greater than 50
print(np.where(a>50))

# replace all values > 50 with 0
print(np.where(a>50,0,a))

#replace all even numbers with 0
print(np.where(a%2 == 0,0,a))

# np.argmax
# The numpy.argmax() function returns indices of the max element of the array in a particular axis.

print(a)

print(np.argmax(a))

print(b)

print(np.argmax(b,axis=0))

np.argmax(b,axis=1)

# np.argmin
print(a)
print(np.argmin(a))