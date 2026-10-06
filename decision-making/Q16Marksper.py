'''Question 27: Write a Java program to input marks of five subjects: Physics, Chemistry, Biology,
 Mathematics, and Computer. Calculate the percentage and display the grade according to the 
 following rules.
Grading Rules:
percentage >= 90: Grade A
percentage >= 80: Grade B
percentage >= 70: Grade C
percentage >= 60: Grade D
percentage >= 40: Grade E
percentage < 40: Grade F

Input:
Physics = 85
Chemistry = 80
Biology = 75
Mathematics = 90
Computer = 70

Output:
Percentage = 80 percent
Grade = B

Explanation:
Total Marks = 85 + 80 + 75 + 90 + 70 = 400

Percentage = Total Marks / 5 = 80 percent

Since the percentage is 80, Grade B is assigned.'''
print("Enter Marks")
p=int(input("Physics = "))
c=int(input("Chemistry = "))
b=int(input("Biology = "))
m=int(input("Mathematics = "))
com=int(input("Computer = "))
total=p+c+b+m+com
per=total//5
print("Percentage = ",per)
if per >=90 :
    print("Grade = A")
elif per>=80:
    print("Grade = B")
elif per>=70:
    print("Grade = C")
elif per>=60:
    print("Grade = D")
elif per>=40:
    print("Grade E")
else :
    print("Grade F")
            
            
            
            
          
    