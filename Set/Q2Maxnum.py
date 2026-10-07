'''2.Find the Maximum Element
Write a Python program to create a set of integers and find the largest element in the set.'''
'''
a={12,65,22,18,6}
nmax=0
for val in a:
    if val>nmax:
        nmax=val
print("Maximum element = ",nmax)
'''

#user input
a=set(input("Enter elements = ").split())
nmax=0
for val in a:
    if int(val)>nmax:
        nmax=int(val)
print("Maximum element = ",nmax)