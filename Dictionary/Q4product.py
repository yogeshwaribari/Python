'''Q.4
Product Price List
Write a Python program to take the names and prices of three products and store them in a 
dictionary. 
Display all product names and their prices.'''
product={}
for i in range(3):
    name=input("Enter product name ")
    prices=int(input("Enter prices "))
    product[name]=prices
    
for k,v in product.items():
    print(k,"\t",v)