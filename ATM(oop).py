#Object oriented programming 
#every thing in python is object 
#L=[1,2,3] here L is object and [1,2,3] is class  
#class is a blueprint 
#classes are set of rules ,blueprint that object follow
#cars are class and marutisuzuki is an object
#class is data ,property,function or behavior
#python has 2 type of claase 1st are build in classes and use defined classes
#object is an instance of class 
#syntax to create an object 
# + -> public  , - -> private 
# objectname = classname ()

#small Banking application ,ATM machine code 
#pascal case = HelloWorld ,MyAtm 
class Atm:
     #constructor - (function (special)) inside class ->superpower
     def __init__(self):
          self.pin=''
          self.balance = 0
          self.menu()
          
     def menu(self):
        user_input = input("""
          Hi How can i help you?
          1. press 1 to create pin
          2. press 2 to change pin
          3. press 3 to check balance 
          4. press 4 to withdraw
          5. Anything else to exit 
              """)
        if user_input=='1':
            self.create_pin()
            #create pin
        elif user_input =='2':
            self.change_pin()
            #change pin
            pass
        elif user_input =='3':
            self.check_balance()
            #check balance 
            pass
        elif user_input =='4':
            self.withdraw()
            #withdraw
            pass
        else:
            exit()
            
     def create_pin(self):
         user_pin = input('enter your pin ')   
         self.pin = user_pin
         
         user_balance = int(input('enter balance '))
         self.balance = user_balance
               
         print('pin created successfully')
         self.menu()
         
     def change_pin(self):
         old_pin = input('enter old pin')
         
         if old_pin == self.pin:
             #let him change the pin 
            new_pin =  input('enter new pin')
            self.pin= new_pin
            print('pin changed successfully!!')
            self.menu()
         else:
             print('nai karne de sakta re baba ')
             self.menu()
             
     def check_balance(self):
         user_pin = input('enter your pin')
         if user_pin == self.pin:
             print('your balance is',self.balance)
         else:
             print('chal nikal yahan se ')
             self.menu()
             
     def withdraw(self):
          user_pin = input('enter your pin')
          if user_pin == self.pin:
              #allow to withdraw
              amount = int(input('enter the amount'))
              if amount <= self.balance:
                  self.balance = self.balance - amount
                  print('withdrawl successful.balance is',self.balance)
              else:
                 print('abe garib')
          else:
            print('chor')
          self.menu()
         
             
obj = Atm()   
obj2 = Atm()
    
 