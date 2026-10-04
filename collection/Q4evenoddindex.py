'''Question 4: Write a Java program to display even & odd index values from an array.
Asked In Practice assignment
Input:
Array Size = 6
Array Elements = 5 10 15 20 25 30
Output:
Values at Even Index = 5 15 25
Values at Odd Index = 10 20 30
Explanation:
? Index starts from 0.
? Even index positions are 0, 2, 4, ….
? Odd index positions are 1, 3, 5, ….
? We print the values according to their index category.'''
n=int(input("Enter Array Size\n"))

list=[0]*n
print("Enter Array Elements")
for i in range(n):
    list[i]=int(input())

print("Values at Even Index = ",end="")
for i in range(n):
    if i%2==0:
        print(list[i],end=" ")
print("\nValues at Odd Index = ",end="")
for i in range(n):
    if i%2!=0:
        print(list[i],end=" ")