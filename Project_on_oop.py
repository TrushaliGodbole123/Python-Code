#NLP Cloud
#here dictionary is used as database 
import nlpcloud


class NLPApp:
    def __init__(self):
        
        self.__database={}
        self.__first_menu()
        
    def __first_menu(self):
        first_input = input(""""
        Hi! How would you like to proceed?
        1. Not a Member? Register
        2. Already a member? Login
        3. Shit! chukun aalo? Exit
        """)
        
        if first_input =='1':
            self.__register()
            
        elif first_input =='2':
            self.__login()
            
        else:
            exit()
            
    def __second_menu(self):
        
        second_input = input(""""
        Hi! How would you like to proceed?
        1. NER
        2. Language Detection
        3. Sentiment Analysis
        4. Logout
        """)
        
        if second_input =='1':
            self.__ner()
            
        elif second_input =='2':
            self.__language_detection()
         
        elif second_input == '3':
            self.__sentiment_analysis()
             
        else:
            exit()
            
        
    
    def __register(self):
        name = input('enter name')
        email = input('enter email')
        password = input('enter password')
        
        if email in self.__database:
            print('email already exist')
        else:
            self.__database[email] = [name,password]
            print('registration Successful.Now login')
            print(self.__database)
            self.__login()
    
    def __login(self):
        email = input('Enter email')
        password = input('Enter password')
        
        if email in self.__database:
            
            if self.__database[email][1] == password:
                print("Login Successful")
                self.__second_menu()
            else:
                print('wrong password.Try again')
                self.__login()
                
        else:
            print('This email is not registered')
            self.__first_menu()
            
    def __ner(self):
        para = input('enter the paragraph')
        search_term = input('what would you like to search ?  ')
        

        client = nlpcloud.Client("finetuned-llama-3-70b", "aedbd3dd9f569d15ec5ffe69d0a1a2574a07564f", gpu=True)
        response = client.entities(para ,searched_entity= search_term)
        print(response)
        
    def __language_detection(self):
        para = input('enter the paragraph')
        
       
        client = nlpcloud.Client("python-langdetect", "aedbd3dd9f569d15ec5ffe69d0a1a2574a07564f", gpu=False)
        response =  client.langdetection(para)
        print(response)
        
        self.__second_menu()
    
        
        
    def __sentiment_analysis(self):
        para = input('enter the paragraph')
        
        
        client = nlpcloud.Client("finetuned-llama-3-70b", "aedbd3dd9f569d15ec5ffe69d0a1a2574a07564f", gpu=True)
        response = client.sentiment(para)
        
        L=[]
        for i in response['scored_labels']:
            L.append(i['score'])
            
        index = sorted(list(enumerate(L)),key=lambda x:x[1],reverse=True)[0][0]
        
        print(response['scored_labels'][index]['label'])
        print(response)
        self.__second_menu()
        
        
        
        
obj =NLPApp()
