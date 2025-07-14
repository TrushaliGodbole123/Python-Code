# What is a Generator

# Python generators are a simple way of creating iterators.

# iterable
class mera_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_iterator(self)
    

# iterator
class mera_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start+=1
        return current
    
# The Why

L = [x for x in range(100000)]

#for i in L:
    #print(i**2)
    
import sys
sys.getsizeof(L)

x = range(10000000)

#for i in x:
    #print(i**2)
sys.getsizeof(x)

# A Simple Example of generators

def gen_demo():
    
    yield "first statement"
    yield "second statement"
    yield "third statement"
    
gen = gen_demo()

for i in gen:
    print(i)
    
# Example 2
def square(num):
    for i in range(1,num+1):
        yield i**2

gen = square(10)

print(next(gen))
print(next(gen))
print(next(gen))

for i in gen:
    print(i)
    
    
# Range Function using Generator

def mera_range(start,end):
    
    for i in range(start,end):
        yield i
        
for i in mera_range(15,26):
    print(i)
    
# Generator Expression
# list comprehension
L = [i**2 for i in range(1,101)]

gen = (i**2 for i in range(1,101))

for i in gen:
    print(i)


# Practical Example
# import os
# import cv2

# def image_data_reader(folder_path):

#     for file in os.listdir(folder_path):
#         f_array = cv2.imread(os.path.join(folder_path,file))
#         yield f_array

# gen = image_data_reader('C:/Users/91842/emotion-detector/train/Sad')

# next(gen)
# next(gen)

# next(gen)
# next(gen)

# Benefits of using a Generator
# 1. Ease of Implementation

class mera_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_iterator(self)
    
# iterator
class mera_iterator:
    
    def __init__(self,iterable_obj):
        self.iterable = iterable_obj
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        
        current = self.iterable.start
        self.iterable.start+=1
        return current
    
def mera_range(start,end):
    
    for i in range(start,end):
        yield i
        
# 2. Memory Efficient

L = [x for x in range(100000)]
gen = (x for x in range(100000))

import sys

print('Size of L in memory',sys.getsizeof(L))
print('Size of gen in memory',sys.getsizeof(gen))

# 3. Representing Infinite Streams

def all_even():
    n = 0
    while True:
        yield n
        n += 2
        
even_num_gen = all_even()
next(even_num_gen)
next(even_num_gen)


#chaining generators
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))


