 # WAP to print the reverse of number pattern .
rows = int(input('enter the rows'))
for i in range(0,rows):
    for j in range(rows-i,0,-1):
        print(j,end=' ')
    print()
    
#next Que 
rows = int(input('enter the rows'))
for i in range(1,rows+1):
    for j in range(0,i):
        print('*',end='')
    print()
    
for i in range(1,rows):
    for j in range(rows-i,0,-1):
        print('*',end='')
    print()
   
    
#next
rows=6
for i in range(1,rows+1):
    print(" "*rows,end=" ")
    print('* '*i)
    rows=rows-1
    
#next
rows=int(input('enter the no.'))
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(j,end='')
    print()
    
#wAP to find the sum of the series of nth term 

x= int(input('enter the x '))
n= int(input('enter the n '))

sum =1
s=' '
for i in range(2,n+1):
    sum=sum+x**i/i
    s=s+'x^{}/{} +'.format(i,i)
print(s[:-1])
print(sum)




#find the sum of series upto n terms.
# write a program to calculate the sum of series upto n term.
# for example , if n=5 the series will become 2+22+222+2222+22222=24690.
# Take the user input and then calculate the output style should 
# match which is given in the example.

start=2 
n= int(input('enter the of terms'))
start = 2
sum=0

for i in range(0,n):
     if i<n-1:
         print(start,end='+')
     else:
        print(start)
    
     sum=sum+start
     start=start*10+2
print(sum)
    
#next
#WAP to print all the unique combination of 1,2,3 and 4
for i in range(1,5):
    for j in range(1,5):
        if j != i:
           for k in range(1,5):
               if k != i and k != j:
                    for l in range(1,5):
                         if l != i and l != j and l != k:
                             print(i,j,k,l)
                             
                             
                             