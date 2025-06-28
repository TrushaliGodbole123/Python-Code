# L=[1,2,3]
# len(L) #function ->bcoz it is outside the list class
# L.append() # method -> bcoz it is inside the list

#Magic method -> special type of method ,it has super power 
#constructor is a special method that is trigger automatically
#constructor is used to write configuration related code.
#means things whose control is not in users hand,that automatically trigger
#golden role of oop-> class ke andar ke chijo ko sirf object access kr skta hai
#self is current object 

#creat own data type 
class Fraction:
    #parameterized constructor:-> need input
    def __init__(self,x,y):
        self.num=x
        self.den=y
    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        new_num=self.num*other.den + other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
        
    def __sub__(self,other):
        new_num=self.num*other.den - other.num*self.den
        new_den=self.den*other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __mul__(self,other):
        new_num=self.num* other.num
        new_den=self.den *other.den
        return '{}/{}'.format(new_num,new_den)
    
    def __truediv__(self,other):
        new_num=self.num* other.den
        new_den=self.den *other.num
        return '{}/{}'.format(new_num,new_den)
     
    def convert_to_decimal(self):
        return self.num/self.den

fr1=Fraction(5,4)
fr2=Fraction(1,2)
print(fr1+fr2)
print(fr1-fr2)
print(fr1*fr2)
print(fr1/fr2)
fr1.convert_to_decimal()



 