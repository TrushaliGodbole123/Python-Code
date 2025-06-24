def is_even(num):
    """
    This function returns if a given number is odd or even
    input - any valid integer
    output - odd/even
    """
    if type(num) == int:
        if num % 2 == 0:
         return 'even'
        else:
         return 'odd'
    else:
        return 'pagal hai kya?'
    
    #function call
    #function_name(input)
for i in range(1,11):
    x = is_even(i)
    print(x)
    #2 point of views
    # print(is_even('hii'))
    
#Type of Argument
#Default Argument,very Important
def power(a=1,b=1):
    return a**b
print(power(3,4))
    
#position Argument
#it means in which order u send output that order the output is print
print(power(2,3))#print 8 not 9 bcoz of positioning of a,b

#keyword Argument,it has higher precedance
print(power(b=3,a=2))#print 8 

#args and **kwargs
#*args and **kwargs are special Python keywords that are used to pass the variable length of arguments to a function.

# *args
# allows us to pass a variable number of non-keyword arguments to a function.

def multiply(*args):
  product = 1

  for i in args:
    product = product * i

  print(args)
  return product
print(multiply(2,4,3,5))

#how to fetch documentation
print(is_even.__doc__)

# **kwargs,keyword args
# **kwargs allows us to pass any number of keyword arguments.
# Keyword arguments mean that they contain a key-value pair, like a Python dictionary.

def display(**salman): #it acts like dictionary

  for (key,value) in salman.items():
    print(key,'->',value)
    
display(india='delhi',srilanka='colombo',nepal='kathmandu')
 
# Points to remember while using *args and **kwargs
# order of the arguments matter(normal -> *args -> **kwargs)
# The words “args” and “kwargs” are only a convention, you can use any name of your choice.

# Without return statement
L = [1,2,3]
print(L.append(4))
print(L)

#Variable Scope
def g(y): #local variable
    print(x) #5
    print(x+1) #6
x = 5 #global variable 
g(x)
print(x)#5

#next
def f(y):
    x = 1
    x += 1
    print(x) #2
x = 5
f(x)
print(x) #5

#next
# def h(y):
#     x += 1 #it gives error
# x = 5
# # h(x)
# print(x) 

def f(x):
   x = x + 1
   print('in f(x): x =', x)#4
   return x

x = 3
z = f(x)
print('in main program scope: z =', z)#4
print('in main program scope: x =', x)#3

#Nested function 
def f():
    def g():
        print('inside function g')
    g()
    print('inside function f')
    
f()
# g(), #this is not possible,bcoz without main function we cannot access inside function

 #next
def g(x):
    def h():
        x = 'abc'
    x = x + 1
    print('in g(x): x =', x)
    h()
    return x

x = 3
z = g(x)

#next
def g(x):
    def h(x):
        x = x+1
        print("in h(x): x = ", x)
    x = x + 1
    print('in g(x): x = ', x)
    h(x)
    return x

x = 3
z = g(x)
print('in main program scope: x = ', x)#3
print('in main program scope: z = ', z)#4

#Functions in python are 1st class citizens
#function is datatype in python
# type and id
def square(num):
  return num**2

type(square)

id(square)

# reassign
x = square
id(x)
x(3) #print 9,it act as square(3)

a = 2
b = a
print(b)

# deleting a function
#del square, this will delete a square function

# storing
L = [1,2,3,4,square]
print(L[-1](3)) #9

#function is immutable 
s = {square}
print(s)

# returning a function
def f():
    def x(a, b):
        return a+b
    return x
    
val = f()(3,4)
print(val) #7

# function as argument
def func_a():
    print('inside func_a')

def func_b(z):
    print('inside func_c')
    return z()

print(func_b(func_a))

# Benefits of using a Function
# Code Modularity
# Code Readibility
# Code Reusabilit
 
# Lambda Function
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression.

# x -> x^2
b=lambda x:x**2
print(b(4))

a = lambda x,y:x+y
print(a(5,2))

# Diff between lambda vs Normal Function
# No name
# lambda has no return value(infact,returns a function)
# lambda is written in 1 line
# not reusable
# Then why use lambda functions?
# They are used with HOF/higher order function

# check if a string has 'a'
a = lambda s:'a' in s
print(a('hello'))

# odd or even
a = lambda x:'even' if x%2 == 0 else 'odd'
print(a(6))

#Higher order function ,function return function 
# Example

def square(x):
  return x**2

def cube(x):
  return x**3

# HOF
def transform(f,L):
  output = []
  for i in L:
    output.append(f(i))

  print(output)

L = [1,2,3,4,5]

print(transform(lambda x:x**3,L))

## Map
# square the items of a list
print(list(map(lambda x:x**2,[1,2,3,4,5])))

# odd/even labelling of list items
L = [1,2,3,4,5]
print(list(map(lambda x:'even' if x%2 == 0 else 'odd',L)))

# fetch names from a list of dict

users = [
    {
        'name':'Rahul',
        'age':45,
        'gender':'male'
    },
    {
        'name':'Nitish',
        'age':33,
        'gender':'male'
    },
    {
        'name':'Ankita',
        'age':50,
        'gender':'female'
    }
]

print(list(map(lambda users:users['gender'],users)))

#filter
# numbers greater than 5
L = [3,4,5,6,7]

print(list(filter(lambda x:x>5,L)))

# fetch fruits starting with 'a'
fruits = ['apple','guava','cherry']

print(list(filter(lambda x:x.startswith('a'),fruits)))

#Reduce
# sum of all item
import functools

print(functools.reduce(lambda x,y:x+y,[1,2,3,4,5]))

# find max
print(functools.reduce(lambda x,y:x if x>y else y,[23,11,45,10,1]))

# find min
print(functools.reduce(lambda x,y:x if x<y else y,[23,11,45,10,1]))
