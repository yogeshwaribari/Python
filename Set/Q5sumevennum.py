'''5.Find the Sum of Even Numbers
Write a Python program to create a set of integers and calculate the sum of only the even numbers.
'''
n=int(input("Enter values size"))
s=set()
print("Enter values")
for i in range(n):
    a=int(input())
    s.add(a)
esum=0
for val in s:
    if val%2==0:
        esum+=val
        
print("Even number sum = ",esum)        