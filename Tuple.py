#empty tuple
t1 = ()
print(t1)

#create a tuple with a single item
t2 =(2,)
print(t2)
print(type(t2))

#homo tuple
t3 = (1,2,3,4)
print(t3)

#hetro tuple
t4 = (1,'hello',True,2.5,[1,2,3])
print(t4)

#tuple within tuple
t5=(1,2,3,(4,5,6))
print(t5)

#using type conversion
t6 = tuple('hello')
print(t6)

#Accessing items
#indexing 

print(t3)
print(t3[0])
print(t3[-1])

#slicing 
print(t3[0:4])
print(t3[::-1])
print(t3[0:3:2])
print(t3[-1:-4:-1])

#Editing items
# print(t3)
# t3[0]=100
#tuples are immutable just like string 

#Adding items 
# print(t3)
#not possible bcoz immutable nature

#deleting items
# you can delete whole tuple not item
# print(t3)
# del t3
# print(t3)

 #Operation On Tuple 
 # + And *
ta=(1,2,3,4,5)
tb=(6,7,8,9)
print(ta + tb)
print(ta*2)

 #membership
print(1 in ta )
print(1 not in ta) 

 #iteration
for i in ta:
    print(i)
    
#Tuple Functions

# len/sum/min/max/sorted
t=(1,2,3,4)
print(len(t))
print(sum(t))
print(min(t))
print(max(t))
print(sorted(t))
print(sorted(t,reverse=True))

# Count ,it count how many times item present in tuple 
t=(1,2,3,4,5)
print(t.count(50))
print(t.count(5))

#index ,it ptints index
print(t.index(5))

#soecial syntax
#tuple unpacking
a,b,c = (1,2,3)
print(a,b,c)

a=1
b=2
a,b=b,a
print(a,b)

a,b,*others=(1,2,3,4)
print(a,b)
print(others)

#zipping tuples

a=(1,2,3,4)
b=(5,6,7,8)
print(list(zip(a,b)))
print(tuple(zip(a,b)))



     
 