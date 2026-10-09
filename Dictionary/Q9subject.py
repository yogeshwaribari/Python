'''
Q.9
Subject Marks
Write a Python program to take subject names and marks for three subjects and store them in a 
dictionary Display all subjects and marks and calculate the average marks.'''
subject={}
for i in range(3):
    subname=input("Enter subject name ")
    marks=int(input("Enter marks "))
    subject[subname]=marks
    
for k,v in subject.items():
    print(k,"\t",v)
    
sum=0
val=subject.values()
for v in val:
    sum+=v
    
print("Total marks = ",sum)
avg=sum/3
print("Avg = ",avg)