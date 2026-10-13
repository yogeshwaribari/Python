'''Q4. Multiple Exceptions
Write a Python program to accept two numbers and divide them. Handle both ValueError 
and ZeroDivisionError.
'''
try:
    a=int(input("Enter number 1 "))
    b=int(input("Enter number 2 "))
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("Not divisible by zero")
except ValueError as v:
    print("Value not correct")
