# Serialization and Deserialization
# Serialization - process of converting python data types to JSON format
# Deserialization - process of converting JSON to python data types
# What is JSON?


# serialization using json module
# list
import json

L = [1,2,3,4]

with open('demo.json','w') as f:
  json.dump(L,f)


# dict
d = {
    'name':'trushu',
     'age':21,
     'gender':'female'
}

with open('demo.json','w') as f:
  json.dump(d,f,indent=4)
  

# deserialization
import json

with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))
  
# serialize and deserialize tuple
import json

t = (1,2,3,4,5)

with open('demo.json','w') as f:
  json.dump(t,f)
  
# serialize and deserialize a nested dict

d = {
    'student':'Trushu',
     'marks':[23,14,34,45,56]
}

with open('demo.json','w') as f:
  json.dump(d,f)
  
# Serializing and Deserializing custom objects

class Person:

  def __init__(self,fname,lname,age,gender):
    self.fname = fname
    self.lname = lname
    self.age = age
    self.gender = gender

# format to printed in
# -> Nitish Singh age -> 33 gender -> male

person = Person('Trushu','godbole',21,'female')

# As a string
import json

def show_object(person):
  if isinstance(person,Person):
    return "{} {} age -> {} gender -> {}".format(person.fname,person.lname,person.age,person.gender)

with open('demo.json','w') as f:
  json.dump(person,f,default=show_object)
  
  
# As a dict
import json

def show_object(person):
  if isinstance(person,Person):
    return {'name':person.fname + ' ' + person.lname,'age':person.age,'gender':person.gender}

with open('demo.json','w') as f:
  json.dump(person,f,default=show_object,indent=4)
  
# indent arrtribute
# As a dict

# deserializing
import json

with open('demo.json','r') as f:
  d = json.load(f)
  print(d)
  print(type(d))
  
# Pickling
# Pickling is the process whereby a Python object hierarchy is converted into a byte stream, and unpickling is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

class Person:

  def __init__(self,name,age):
    self.name = name
    self.age = age

  def display_info(self):
    print('Hi my name is',self.name,'and I am ',self.age,'years old')
    
p = Person('nitish',33)

# pickle dump
import pickle
with open('person.pkl','wb') as f:
  pickle.dump(p,f)
  
# pickle load
import pickle
with open('person.pkl','rb') as f:
  p = pickle.load(f)

p.display_info()


# Pickle Vs Json
# Pickle lets the user to store data in binary format. JSON lets the user store data in a human-readable text format.