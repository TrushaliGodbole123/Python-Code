# Some Theory
# Types of data used for I/O:
# Text - '12345' as a sequence of unicode chars
# Binary - 12345 as a sequence of bytes of its binary equivalent
# Hence there are 2 file types to deal with
# Text files - All program files are text files
# Binary Files - Images,music,video,exe files

# How File I/O is done in most programming languages
# Open a file
# Read/Write data
# Close the file

#writing to a file 
# case 1 - if the file is not present
f = open('sample.txt','w')
f.write('Hello world')
f.close()
# since file is closed hence this will not work
# f.write('hello')

# write multiline strings
f = open('sample1.txt','w')
f.write('hello world')
f.write('\nhow are you?')
f.close()


# case 2 - if the file is already present
f = open('sample.txt','w')
f.write('salman khan')
f.close()

# Problem with w mode
# introducing append mode
f = open('sample1.txt','a') # a;- append mode
f.write('\nI am fine')
f.close()

# write multiple lines
L = ['hello\n','hi\n','how are you\n','I am fine']

f = open('sample.txt','w')
f.writelines(L)
f.close()

# reading from files
# -> using read()
f = open('sample.txt','r')
s = f.read()
print(s)
f.close()

# reading upto n chars
f = open('sample.txt','r')
s = f.read(10)
print(s)
f.close()

# readline() -> to read line by line
f = open('sample.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')
f.close()

# reading entire using readline
f = open('sample.txt','r')

while True:

  data = f.readline()

  if data == '':
    break
  else:
    print(data,end='')

f.close()

# Using Context Manager (With)
# It's a good idea to close a file after usage as it will free up the resources
# If we dont close it, garbage collector would close it
# with keyword closes the file as soon as the usage is over

# with
with open('sample1.txt','w') as f:
  f.write('selmon bhai')
  

# try f.read() now
#read using with
with open('sample.txt','r') as f:
  print(f.readline())
  
# moving within a file -> 10 char then 10 char
with open('sample.txt','r') as f:
  print(f.read(10))
  print(f.read(10))
  print(f.read(10))
  print(f.read(10))
  
# benefit? -> to load a big file in memory
big_L = ['hello world ' for i in range(100)]

with open('big.txt','w') as f:
  f.writelines(big_L)
  
  
with open('big.txt','r') as f:

  chunk_size = 10

  while len(f.read(chunk_size)) > 0:
    print(f.read(chunk_size),end='***')
    f.read(chunk_size)
    

# seek and tell function
with open('sample.txt','r') as f:
  f.seek(15) #start from 15 
  print(f.read(10))
  print(f.tell())
  
  print(f.read(10))
  print(f.tell())
  
# seek during write
with open('sample.txt','w') as f:
  f.write('Hello')
  f.seek(0)
  f.write('X')
  
  
# Problems with working in text mode
# can't work with binary files like images
# not good for other data types like int/float/list/tuples

# working with binary file
# with open('screenshot1.png','r') as f:
#   f.read() 
  
# working with binary file
with open('screenshot1.png','rb') as f:
  with open('screenshot_copy.png','wb') as wf: #this make copy
    wf.write(f.read())
    

# working with other data types
# with open('sample.txt','w') as f:
#   f.write(5) ,accept only str
  
with open('sample.txt','w') as f:
  f.write('5')
  
with open ('sample.txt','r') as f:
  print(int(f.read()) + 5)
  

# more complex data
d = {
    'name':'trushu',
     'age':21,
     'gender':'female'
}

with open('sample.txt','w') as f:
  f.write(str(d))
  
  #you cannot convert str to dictionary
with open('sample.txt','r') as f:
  print(f.read())
  print(type(f.read()))
  

