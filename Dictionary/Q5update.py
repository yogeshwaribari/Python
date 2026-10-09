'''Q.5
Dictionary Update
Write a Python program to create a dictionary containing three key-value pairs. 
Ask the user for a key and a new value, then update the dictionary with the new value. 
Display the updated dictionary.'''
update={}
for i in range(3):
    eid=int(input("Enter id "))
    name=input("Enter name ")
    update[eid]=name
    
print("before update")
for k,v in update.items():
    print(k,"\t",v)
    
uid=int(input("Enter new id "))
uname=input("Enter new name ")
update[uid]=uname

print("After update")
for k,v in update.items():
    print(k,"\t",v)