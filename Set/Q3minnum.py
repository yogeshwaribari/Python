'''3. Find the Minimum Element
Write a Python program to create a set of integers and find the smallest element in the set.'''
n=int(input("Enter your values size "))

s=set()
print("Enter values")
for i in range(n):
    a=int(input())
    s.add(a)
#nmin=999
nmin=None
for val in s:
   # if val<nmin:
    if nmin is None or val<nmin:
        nmin=val


print("Minimum number = ",nmin)