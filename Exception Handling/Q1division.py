'''Q1. Division of Two Numbers
Write a Python program to divide two numbers. Handle the exception that occurs when the 
denominator is zero.'''
n=int(input("Enter value "))
try:
    a=n/0
    print(a)
except ZeroDivisionError as e:
    print("Not division by 0")
    