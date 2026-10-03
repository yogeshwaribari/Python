'''Question 6: Write a Java program to convert length from centimeter into meter and kilometer.'
Asked In Basic program
Input:
Centimeter = 150
Output:
Meter = 1.5
Kilometer = 0.0015
Explanation:
1 meter = 100 centimeters
1 kilometer = 100000 centimeters
The given value is converted using standard unit conversion formulas.'''
centimeter=input("Enter Centimeter\n")
meter=int(centimeter)/100
kilometer=int(centimeter)/100000

print("Meter =",meter)
print("Kilometer =",kilometer)