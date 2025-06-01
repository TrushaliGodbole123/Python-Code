#Given the first 2 terms of an arithmatic series.Find the Nth term of the series.Assume all inputs are provided by the user.
#hint: an=a+(n-1)d

first=int(input('enter 1st term'))
second=int(input('enter 2nd term'))
n = int(input('enter the value of n'))

d = second - first
an = first +(n-1)*d
print(an)
