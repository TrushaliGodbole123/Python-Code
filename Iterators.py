#what is an Iteration 
# Iteration is a general term of taking each item of something , one after another.
# Any time you use a loop, explicit or implicit, to go over a group of items , that is iteration.

#Example
num =[1,2,3]

for i in num:
    print(i)
    
#What is Iterator 
#An iterator is an object that allows the programmer to traverse through a sequence of data 
#without having to store the entire data in the memory.
#bcoz of Iterator ,Iteration can occur or possible.

#Example
L=[x for x in range (1,100000)]
# takes too much space in memory 
#for i in L:
     #print (i*2)
     
import sys 
print(sys.getsizeof(L)/1024)

x= range(1,1000000)
# for i in x:
#     print(i*2)
    
print(sys.getsizeof(x)/1024)

#what is ietrable 
#Iterable is an object , which one can iterate over 
#it generate an iterator when passes to iter() method.

#example
L=[1,2,3]
type(L)
#to check object is iterable or not run
#dir(L) ,if iter seen then iterable
#and if iter and next seen then iterator

#L is an iterable
type(iter(L))

#iter(L)-->iterator

#point to remember
#Every iterator is also and ietrable
#Not all iterables are iterators

#Trick 
#Every iterable has an iter function 
#Every iterator has both iter function as well as a next function

L=[1,2,3]
#L is not an iterator 
iter_L=iter(L)

#iter_L is an iterator

# Understanding how for loop works

num = [1,2,3]

for i in num:
    print(i)
    
num = [1,2,3]

# fetch the iterator
iter_num = iter(num)

# step2 --> next
next(iter_num)
next(iter_num)
next(iter_num)
# next(iter_num)

# Making our own for loop
def mera_khudka_for_loop(iterable):
    
    iterator = iter(iterable)
    
    while True:
        
        try:
            print(next(iterator))
        except StopIteration:
            break  

a = [1,2,3]
b = range(1,11)
c = (1,2,3)
d = {1,2,3}
e = {0:1,1:1}

mera_khudka_for_loop(e)

# A confusing point
num = [1,2,3]
iter_obj = iter(num)

print(id(iter_obj),'Address of iterator 1')

iter_obj2 = iter(iter_obj)
print(id(iter_obj2),'Address of iterator 2')

# Let's create our own range() function
class mera_range:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def __iter__(self):
        return mera_range_iterator(self)
    
class mera_range_iterator:
    
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
    
for i in mera_range(1,11):
    print (i)
    
x = mera_range(1,11)
print(type(x))

print(iter(x))