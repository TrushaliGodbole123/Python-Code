#write a program to find the sum of sequences of first n naturak numbers where n will be provided by the user.
#hint- thus, the sum of the squares of first n natural numbers=n(n+1)(2n+1)/6

n = int(input('enter the number'))

result = (n*(n+1)*(2*n+1))/6
print(result)