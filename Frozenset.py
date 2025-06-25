#Frozen set is just an immutable version of a python set object
#notchangable
fs1 = frozenset([1,2,3])
fs2 = frozenset([3,4,5])

print(fs1 | fs2)

#what works and what does not
#works-> all read functions
#does'n work -> write operations


# When to use,read only operation
# 2D sets
fs = frozenset([1,2,frozenset([3,4])])
print(fs)

#set comprehension
print({i for i in range(1,11)})
print({i for i in range(1,11) if i>5})
print({i*i for i in range(1,11)})

