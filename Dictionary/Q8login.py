'''Q.8
Simple Login System
Write a Python program to create a ictionary containing usernames and passwords. 
Ask the user to enter a username and password and check whether the login details are correct.'''
login={}

for i in range(2):
    username=input("Enter username ")
    password=input("Enter Password ")
    login[username]=password
    
user=input("Please enter your username for login ")
passw=input("Enter password ")

for k,v in login.items():
    if user==k and v==passw:
        print("Login successful")
        break
else:
    print("Login details incorrect")
    