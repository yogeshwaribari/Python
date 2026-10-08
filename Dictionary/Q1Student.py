'''Q.1
Student Marks Dictionary
Write a Python program to take a student name and marks as input and store them in a dictionary. 
Display the student name and marks.'''
student={}
for i in range(3):   
    name=input("Enter student name ")
    marks=int(input("Enter student Marks "))
    student[name]=marks


for k,v in student.items():
    print(k,"\t",v)