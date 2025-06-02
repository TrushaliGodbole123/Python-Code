 #creating sets
 #Empty set
 
s=set()
print(s)
print(type(s))

#1d and 2d set
s1={1,2,3}
print(s1) 

#s2={1,2,3,{4,5}} it is not possible 

#homo 
s1={1,2,3,4}
print(s1)

#hetro
s2={1,'hello',4.6,True} #can't print true bcoz duplicate nature 1 and True =1
print(s2)

#using type conversion
s4=set([1,2,3])
print(s4)

#duplicate not allowed
s5={1,1,1,2,3,4,3,2,2}
print(s5)

#set can't have mutable items
#s6={1,2,[3,4]} it is not possible

 #Accessing items
s1={1,2,3,4}
#s1[0:2] it is not possible bcoz set is unordered
#that why accessing item is not possible though indexing and slicing 

#Editing item
#it is also not possible in set 

#Add items
s={1,2,3,4}
#add ,able to add only one item at a time
s.add(5)
print(s)

#update,here we can add multiple items
s.update([8,6,7])
print(s)

#delete items ,it work but not able to delete perticular item
s={1,2,3,4,5}
print(s)
# del s 
# print(s)

#discard, it delete perticular item
s.discard(5)
s.discard(10) # at that time it will not throw an error
print(s)

s.remove(4)
print(s)

#pop, it delete random items
s.pop()
print(s)

#clear 
s.clear()
print(s)

#set Operation
s1={1,2,3,4,5}
s2={4,5,6,7,8}

#Union(|)
print(s1|s2)

#intersection(&),same elements
print(s1 & s2)

#Difference(-)
print(s1 - s2)
print(s2 - s1)

#symmetric Difference(^) ,non same elements
print(s1 ^ s2)

#membership Test
print(1 not in s1)

#iteration
for i in s1:
    print(i)

#set function
#len/sum/min/max/sorted
s1={1,2,3,4,5}
print(len(s1))
print(sum(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
print(sorted(s1,reverse=True))

#union/update
s1={1,2,3,4,5}
s2={4,5,6,7,8}

#union (|)
print(s1.union(s2))

#update
s1.update(s2) 
print(s1)
print(s2)

#intersection /intersection_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}

print(s1.intersection(s2))

print(s1.intersection_update(s2))
print(s1) #intersection result
print(s2) #same s2

#difference /difference update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.difference(s2)) #1,2,3

print(s1.difference_update(s2)) #none
print(s1)
print(s2)

#symmetric_difference /symmetric_difference_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
print(s1.symmetric_difference(s2)) #1,2,3,6,7,8

print(s1.symmetric_difference_update(s2)) #none
print(s1) #1,2,3,6,7,8
print(s2)

#isdisjoint / issubset / issuperset
s1={1,2,3,4}
s2={3,4,5,6}

print(s1.isdisjoint(s2)) #this are set where no one is common element 
#so s1 and s2 is not disjoint ,False

#issubset
s1={1,2,3,4,5}
s2={3,4,5}

print(s2.issubset(s1)) #True bcoz s2 has all element in s1

#issuperset ,True bcoz s1 is superset of s2 
print(s1.issuperset(s2))

#copy
s1={1,2,3}
s2=s1.copy()
print(s1)
print(s2)
