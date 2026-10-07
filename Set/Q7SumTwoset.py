'''7.Add Corresponding Elements from Two Sets
Write a Python program to create two sets containing the same number of elements.
 Convert them into 
lists and calculate the sum of corresponding elements.
Sample Input:
Set 1 = {10, 20, 30}
Set 2 = {1, 2, 3}
Sample Output:
11
22
33'''
'''
s1={10,20,30}
s2={1,2,3}
'''
n=int(input("Enter values size "))
s1=set()
s2=set()
print("Enter values s1")
for i in range(n):
    a=int(input())
    s1.add(a)

print("Enter values s2")
for i in range(n):
    a1=int(input())
    s2.add(a1)
    
l1=list(s1)
l2=list(s2)
print("Output :")
for i in range(len(l1)):
    print(l1[i]+l2[i])


