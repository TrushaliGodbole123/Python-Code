#getter -> private ka value bahar dikhana
#setter -> private ka value bahar se chsnge krna

#colllection of objects 

#dictionar of object
# list of object

class person:
    def __init__(self,name,gender):
        self.name =  name
        self.gender =  gender
        
p1 = person('Trushu','Female')
p2 = person('Akshu','Female')
p3 = person('Gauri','Female')

L=[p1,p2,p3]
d= {'p1':p1, 'p2':p2, 'p3':p3}

for i in L:
    print(i.name,i.gender)
for i in d:
    print(d[i].gender)

#static variable (vs Instance variable  )
#the value of instance variable is different for every object
# instance variable is object's variable
#the value of static variable is same for every object
# static variable is class's variable 
#how to identify
#if in front of variable name their is self then it is  IV.
#if in front of variable name their is class name then it is  SV.




        