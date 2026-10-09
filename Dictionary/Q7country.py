'''Q.7
Display the dictionary.
Country and Capital
Write a Python program to take the names of three countries and their capitals from the user 
and store them in a dictionary. Display all country-capital pairs.
'''
country={}
for i in range(3):
    cname=input("Enter country name")
    capname=input("Enter capital name")
    country[cname]=capname
for k,v in country.items():
    print(k,"\t",v)
    
