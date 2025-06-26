# Dictionary in Python is a collection of keys values, used to store data values like a map, 
# which, unlike other data types which hold only a single value as an element.

# In some languages it is known as map or assosiative arrays.

# dict = { 'name' : 'trushu' , 'age' : 21 , 'gender' : 'female' }

# Characterstics:

# Mutable
# Indexing has no meaning
# keys can't be duplicated
# keys can't be mutable items

# empty dictionary
d = {}
print(d)

# 1D dictionary ,homo
d1 = { 'name' : 'Trushu' ,'gender' : 'female' }
print(d1)

# with mixed keys
d2 = {(1,2,3):1,'hello':'world'}
print(d2)

# 2D dictionary -> JSON
s = {
    'name':'Trushu',
     'college':'kdk',
     'sem':4,
     'subjects':{
         'dsa':50,
         'maths':67,
         'english':34
     }
}
print(s)

# using sequence and dict function
d4 = dict([('name','nitish'),('age',32),(3,3)])
print(d4)

# duplicate keys , duplicate keys not allowed 
d5 = {'name':'trushu','name':'gauri'}
print(d5) #prints only name gauri which is updated

# mutable items as keys
d6 = {'name':'trushu',(1,2,3):2} #list is not work here bcoz muatble nature
print(d6)

#Accessing items 
my_dict = {'name': 'Jack', 'age': 26}

# by using []
print(my_dict['age'])

#by using get function
print(my_dict.get('age'))


#Adding key-Value Pair
d4['gender']='female'
d4['weight']=40
print(d4)
s['subjects']['ds']=75
print(s)
# s['subjects']=['maths']
# print(s)

#Remove key-value pair
d = {'name': 'trushu', 'age': 21, 3: 3, 'gender': 'female', 'weight': 40}

#pop
d.pop(3) #it delete key value pair of provided key
print(d)

#popitem , it delete last value pair
d.popitem()
print(d)

#del
del d['age']
print(d)

print(s['subjects']['dsa'])


#Editing key-value pair
print(s)
s['subjects']['dsa']=80
print(s)

#Dictionary Operations
#membership
print('t' in s)
print('name' in s)

#iteration
d={'name':'trushu','gender':'female','age':21}
for i in d:
    print(i,d[i])
    print(i)
    
#dictionary function
#len/sorted
print(len(d))
print(sorted(d))
print(sorted(d,reverse=True))
print(min(d))
print(max(d))

#items/keys/values

print(d)
print(d.items()) #it ptints tuple inside list
print(d.keys())
print(d.values())

#update
d1={1:2,3:4,4:5}
d2={4:7,6:8}
d1.update(d2)
print(d1)

#Dictionary Comprehension
# {key:value for vars in iterable}

#print 1st 10 numbers and their squares
print({i:i**2 for i in range(1,11)})

#using existing dict
distances = {'delhi':1000,'mumbai':2000,'banglore':3000}
print({key:value*0.62 for (key,value) in distances.items()})

#using zip
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp_C = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

print({i:j for (i,j) in zip(days,temp_C)})

# using if condition
products = {'phone':10,'laptop':0,'charger':32,'tablet':0}

print({key:value for (key,value) in products.items() if value>0})

#nested comprehension
#print table of number from 2 to 4
print({i:{j:i*j for j in range(1,11)} for i in range(2,5)})
 
