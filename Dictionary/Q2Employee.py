'''Q.2
Employee Salary Record
Write a Python program to take an employee ID and salary as input and store them in a dictionary. 
Display the employee ID and salary.
'''
employee={}
for i in range(3):
    eid=int(input("Enter employee id "))
    salary=int(input("Enter salary "))
    employee[eid]=salary
    

for k,v in employee.items():
    print(k,"\t",v)
