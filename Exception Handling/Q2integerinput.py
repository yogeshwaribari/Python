'''Q2. Integer Input
Write a Python program to accept an integer from the user. Handle the exception if the
 user enters a non-numeric value.
'''

try:
    n=int(input("Enter Integer value "))
    print(n)
except ValueError as e:
    print("Value not integer")
    
