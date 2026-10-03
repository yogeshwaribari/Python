'''uestion 53: Create a Java program to simulate a simple calculator using a switch case. 
It should take two numbers and an operator (+, -, *, /, %) as input and perform the corresponding 
operation.
Input:
Number1 = 10
Number2 = 5
Operator = +

Output:
Result = 15
Explanation:
The program uses switch on the operator. When '+' is selected, it performs addition of the two 
numbers.
Input:
Number1 = 10
Number2 = 4
Operator = %

Output:
Result = 2
Explanation:
The '%' operator calculates the remainder after division. 10 % 4 gives remainder 2.'''
print("choose operator")
print("+, -, *, /, %")

a=int(input("Enter number 1\n"))
b=int(input("Enter number 2\n"))
op=input("Enter operator\n")

match op:
    case "+":
        print("Addition =",a+b)
    case "-":
        print("Substraction =",a-b)
    case "*":
        print("Multiplication =",a*b) 
    case "/":
        print("Division =",a//b)
    case "%":
        print("Module =",a%b)
    case _:
        print("Wrong choice")
        
    