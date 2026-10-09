'''Q.6
Student Grade Dictionary
Write a Python program to take a student's name and percentage as input. Store the student's name 
and grade in a dictionary based on the following criteria:
75 and above → A
60 to 74     → B
40 to 59     → C
Below 40     → Fail'''
student={}
for i in range(3):
    name=input("Enter name ")
    per=int(input("Enter percentage "))
    if per>75:
        student[name]="A"
    elif per>60 and per<74:
        student[name]="B"
    elif per>40 and per<59:
        student[name]="C"
    else:
        student[name]="Fail"
        
for k,v in student.items():
    print(k,"\t",v)
        
        