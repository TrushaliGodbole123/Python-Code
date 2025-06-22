#len / Min / max / sorted
L=[2,1,5,7,0]

print(len(L))
print(max(L))
print(min(L))
print(sorted(L))
print(sorted(L,reverse=True)) #this is not permanent

#count
L = [1,2,1,3,4,1,5]
L.count(1)

#index
L = [1,2,1,3,4,1,5]
L.index(1)

# reverse
L = [1,2,1,3,4,1,5]
#permanently reverse the list
L.reverse()
print(L)

#sort (vs sorted) sort in permanent
L=[2,1,5,7,0]
print(L)
print(sorted(L))
print(L)
L.sort()
print(L)

#copy ->shallow
L = [2,1,5,7,0]
print(L)
print(id(L))
L1 = L.copy()
print(L1)
print(id(L1))

# List Comprehension
#Add 1 to 10 numbers to a list
L=[]
for i in range(1,11):

    L.append(i)
print(L)

# newList = [expression for item in iterable if condition == True ]
L = [i for i in range(1,11)]
print(L)

#scalar Multiplication on a vector
v=[2,3,4]
s=-3
#[-6,-9,-12]

x=[]

for i in v:
    x.append(i*s)
print(x)

v=[2,3,4]
s=-3
[s*i for i in v]

#add Squares
L = [1,2,3,4,5]

[i**2 for i in L]

#print all number divisible by 5 in the range of 1 to 50
L=[i for i in range(1,51) if  i%5==0]
print(L)

#find languages which start with letter p 
languages = ['java','python','php','c','javascript']
[language for language in languages if language.startswith("p")]

#Nested if with list comprehension
basket = ['apple','guava','cherry','banana']
my_fruits = ['apple','kiwi','grapes','banana']

#add new list from my_fruits and item if the fruits exists in basket and also starts with "a"

[i for i in my_fruits if i in basket if i.startswith('a')]

#print a(3,3) matrix using list comprehension -> nested list comprehension
[[i*j for i in range(1,4)] for j in range(1,4)]

#cartesian product -> List comprehension on 2 lists together
L1=[1,2,3,4]
L2=[5,6,7,8]

[i*j for i in L1 for j in L2]

#2 ways to traverse a list

#itemwise
L=[1,2,3,4]
for i in L:
    print(i)
    
#indexwise
L=[1,2,3,4]
for i in range(0,len(L)):
    print(i)# it print index
    print(L[i])  #print value under list