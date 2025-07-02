#Class relationships
#Aggregation :- Has a relationship(one class owns the other class)(<> symbol,diamond)
#Inheritance (<| symbol ,triangle)

class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
        
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)
        
    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)
        
        
class Address:
    def __init__(self,city,pin,state):
        self.__city = city
        self.pin = pin
        self.state = state
        
    def get_city(self):
        return self.__city
    
    def edit_address(self,new_city,new_pin,new_state):
        self.__city =new_city
        self.pin=new_pin
        self.state=new_state
   
add1 = Address('nagpur','441302','maharashtra')     
cust = customer('trushu','female',add1)
        
cust.print_address()

cust.edit_profile('Trushu','pune','440002','maharashtra')
cust.print_address()

#Aggregation and class diagram 

#Inheritance
#example 

#parent
class user:
    def __init__(self):
        self.name = 'trushu'
        
    def login(self):
        print('login')
        
#child
class student(user):  #here inheritance happen
    # def __init__(self): #1stly child constructor call
        # self.rollno = 100 #if it is not present then parent constructor call(execute)
        
    def enroll(self):
        print('enroll into the course')
        
        
u = user()
s=student()

print(s.name)
# print(s.rollno)
s.login()
s.enroll()

# what gets inherited?
# 1. constructor 
# 2. Non private Attributes
# 3.Non private Methods

class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ')
        self.price = price 
        self.brand = brand 
        self.camera = camera 
        
    
        
class smartPhone(phone):
    def __init__(self,os,ram):
        self.os = os
        self.ram = ram
        print('Inside phone constructor ')
        
        
s=smartPhone('android',3)


#child can't access private member of the class 

class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ')
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
        
    #getter    
    def show(self):
        print(self.__price)
        
# class SmartPhone(phone):
#     def check(self):
#         print(self.__price) 
        
# s=SmartPhone(20000,'apple',13)
# print(s.brand)
# s.show()
# s.check() #this gives error bcoz the price is private member  


class parent:
    def __init__(self,num):
        self.__num = num
        
    #using getter method able to access private member 
    def get_num(self):
        return self.__num
    
class child(parent):
    def show(self):
        print('This is in child class')
        
son = child(100)
print(son.get_num())
son.show()

#next example
class parent:
    def __init__(self,num):
        self.__num = num
        
    def get_num(self):
        return self.__num
    
class child(parent):
    def __init__(self, val,num):
        self.__val=val
        
    def get_val(self):
        return self.__val
    
son = child(100,10)
# print("parent: Num:", son.get_num()) #this will thro an error 
print("Child: val:", son.get_val()) 

#method Overriding 
class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ')
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
    def buy(self):
        print("Buying a phone")
        
class SmartPhone(phone):
    def buy(self):
        print("Buying a smartPhone") #this print bcoz child method is execute
        
s = SmartPhone(20000,'apple',13)
s.buy()

#Super Keyword
#super is a way to access parent ke methods

class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ')  #1stly print this
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
    def buy(self):
        print("Buying a phone") #3rdly this executes
        
class SmartPhone(phone):
    def buy(self):
        print("Buying a smartPhone") #2nd print this
        #syntax to call parent ka buy method 
        super().buy() #due to this super keyword
        
s = SmartPhone(20000,'apple',13)

s.buy()

#super -> constructor 
class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ')  #1stly print this
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
class smartPhone(phone):
    def __init__(self, price, brand, camera,os,ram):
        print('inside smartphone constructor')
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("Inside smartphone constructor")
        
s = smartPhone(20000,"samsung",12,'android',2)

print(s.os)
print(s.brand)

#using super outside the class can't work 
#super cannot access variables 
#super cannot be used outside the class 
#super is used inside the child class.

#Type of Inheritance 
#1. Single Inheritance (1 p and 1 C)
#2. Multilevel Inheritance 
#3. Hierarchical Inheritance (like 1 parent and multiple child)
#4. Multiple Inheritance(Diamond problem)
#5. Hybrid Inheritance 

#single Inheritance 
class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ') 
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
    def buy(self):
        print("Buying a phone") 
        
class SmartPhone(phone):
    pass
SmartPhone(10000,'redmi','13px').buy()


#multilevel
class product:
    def review(slef):
        print('product customer review')
        
class phone(product):
    def __init__(self,price,brand,camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
        
    def buy(Self):
        print('buying a phone')
        
class smartphone(phone):
    pass

s=smartphone(20000,'apple',12)
s.buy()
s.review()      

#heirarchical 
class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ') #1st,3
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
    def buy(self):
        print("Buying a phone") #2nd,4
        
class SmartPhone(phone):
    pass

class FeaturePhone(phone):
    pass

SmartPhone(10000,'redmi','13px').buy()
FeaturePhone(20000,'realme','1px').buy()


#Multiple 
class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ') 
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
    def buy(self):
        print("Buying a phone") 
    
class product:
    def review(self):
        print('customer review')
        
class smartphone(phone,product):
    pass

s=smartphone(2000,'oneplus',12)
s.buy()
s.review()

#The diamond problem 

class phone:
    def __init__(self,price,brand,camera):
        print('Inside phone constructor ') 
        self.__price = price 
        self.brand = brand 
        self.camera = camera 
           
    def buy(self):
        print("Buying a phone") 
    
class product:
    def buy(self):
        print('product buy method')
        
#method resolution order
class smartphone(product,phone): #due to product is 1st the buy method of product class call.
    pass

s=smartphone(200,'apple',13)
s.buy()
