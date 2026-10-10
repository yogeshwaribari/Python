'''1. Create a tuple with 5 integer values and print it.'''
n=int(input("Enter values size "))
a=()
for i in range(n):
    x=int(input("Enter number "))
    a=a+(x,)
    
print(a)
    