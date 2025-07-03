#polymorphism 
#method overriding 
#method overloading 
#operator overloading

#method overloading 
#In this the method name is same inside the same class but behaviour is different 
#example

class shape:
    def area(self,radius):
        return 3.14*radius*radius
    
    # def area(self,1,b):
    #     return 1*b
    
s=shape()
s.area(2)
# s.area(3,4)

#next how to overcome upper error
class shape:
    def area(self,a,b=0):
        if b ==0:
            return 3.14*a*a
        else:
            return a*b
        
s=shape()
print(s.area(2))
print(s.area(3,4))

#operator overloading 
#same operator has different behaviour here 
print('hello '+'sister')
print(2+3)
print([1,2,3]+[4,5,6])


#Abstraction (hidden)
#In abstract class at least 1 abstract method should be present
#Example 

from abc import ABC,abstractmethod
class BankApp:
    def database(self):
        print('connected to database')
        
    @abstractmethod
    def security(self):
        pass
    
class MobileApp(BankApp):
    
    def mobile_login(self):
        print('Login into mobile')
        
    def security(self):
        print('Mobile security')
        
m=MobileApp()
m.database()
m.security()
m.mobile_login()