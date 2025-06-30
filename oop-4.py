#How object access attributes 

class person:
    def __init__(self,name_input,country_input):
        self.name = name_input
        self.country = country_input
        
    def greet(self): #method inside class 
        if self.country == 'india':
            print('Namaste',self.name)
        else:
            print('Hello',self.name)
            
        
#next topic
#Reference Variable 
#object without reference 
# refrence variable holds the object
# we can create objects without reference variable as well.
# An object can have multiple reference variables.
# Assigning a new reference variable to an existing object does not create a new object
#user defined objects are mutable

class person:
    def __init__(self):
        self.name = 'trushali'
        self.gender = 'female'
        
p= person()
#here p contain the reference/adress of the object
# p is a reference variable which has adress of object
q = p 

print(id(p))
print(id(q))
 
 
#pass by reference
class person:
    def __init__(self,name,gender):
        self.name = name 
        self.gender = gender

#outside the clas  -> function 
def greet(person):
    print('hi my name is ',person.name, 'and I am a', person.gender)
    p1 = person('Akshu','female')
    return p1

p= person('trushu','female')
x = greet(p)
print(x.name)
print(x.gender)


