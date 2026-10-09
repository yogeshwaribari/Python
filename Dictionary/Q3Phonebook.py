'''Q.3
Phone Book
Write a Python program to take a person's name and phone number as input and store them in a 
dictionary.
Ask the user for a name and display the corresponding phone number.'''
book={}

for i in range(3):
    name=input("Enter name ")
    phone=input("Enter phone number ")
    book[name]=phone
sname=input("Enter search name ")
for k,v in book.items():
    if k==sname:
        print(k,"\t",v)