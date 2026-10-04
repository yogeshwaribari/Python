'''Question 1: Write a Java program to input an array & display it.
Asked In Practice assignment
Input:
Array Size = 5
Array Elements = 10 20 30 40 50
Output:
10 20 30 40 50
Explanation:
? First, we take the size of the array from the user.
? Then, elements are entered one by one into the array.
? Finally, using a loop, we display all elements in the same order they were entered.'''
n=int(input("Enter Array Size \n"))
list=[0]*n
'''
print("Enter Array Elements")
for i in range(n):
    x=input()
    list.append(x)
i=0
print("Output")
while i<n:
    print(list[i],end=" ")
    i=i+1
'''
print("Enter Array Elements")
for i in range(n):
    list[i]=int(input())
  
i=0  
print("Output")
while i<n:
    print(list[i],end=" ")
    i=i+1
    