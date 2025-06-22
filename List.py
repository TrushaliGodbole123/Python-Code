#Empty List
print([])

#1d->Homo
print([1,2,3,4,5])

#2D ->hetrogenes as list and int
print([1,2,3,[4,5]])

#3d->homo
print([[[1,2],[3,4]],[[5,6],[7,8]]])

#heterogenes
print([1,True,5.6,5+6j,"hii"])
#using Type Conversion
print(list('hello'))


#Accessing item from a list
#Indexing 
L=[1,2,3,4,5]
#positive
print(L[3])
#negative
print(L[-1])

L=[[[1,2],[3,4]],[[5,6],[7,8]]]
print(L[0][0][1])

#slicing
L=[1,2,3,4,5,6]
print(L[-3:])
print(L[0::2])#here 2 means deference print one after
print(L[::-1]) #reverse the string
print(L[-5:-2:2]) # here -5 to -2 by difference of two 

# Adding Items to a List
#append 
L=[1,2,3,4,5]
L.append(True)
L.append([6,7,8])
print(L)


#extend ,use for to add multiple item at a time
L=[1,2,3,4,5]
L.extend([6,7,8])
print(L)

#insert
L=[1,2,3,4,5,6]
L.insert(1,100)
print(L)

#Editing item in a list
#editing with indexing
L=[1,2,3,4,5]
L[-1]=500
print(L)

#editing with slicing
L=[1,2,3,4,5]
L[1:4]=[200,300,400]
print(L)

#Deleting items from a list 
#del
L=[1,2,3,4,5]
print(L)
# del L
# print(L)

#del one item by indexing
L=[1,2,3,4,5]
print(L)
del L[-1]
print(L)

#del mone item by slicing
L=[1,2,3,4,5]
print(L)
del L[1:3]
print(L)

#remove
#item ko value ke hisab se delete krna
L=[1,2,3,4,5]
L.remove(5)
print(L)

#pop
L=[1,2,3,4,5]
L.pop(0)
print(L)
L.pop() #it delete last index
print(L)


#clear
L=[1,2,3,4,5]
L.clear()
print(L)

#Operation on list

#Arithmatic (+,*)
L1 = [1,2,3,4]
L2 = [5,6,7,8]

#concatanation/Merge
print(L1 + L2)

print(L1*3)

#Membership Operator
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

print(5 in L1)

L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

print(5 not in L1)

L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

print(5 in L2)
print([5,6] in L2)

#Loops
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

for i in L1:
    print(i)
    
#Loops
L1 = [1,2,3,4,5]
L2 = [1,2,3,4,[5,6]]

for i in L2:
    print(i)
    
L=[[[1,2],[3,4]],[[5,6],[7,8]]]
for i in L:
    print(i)