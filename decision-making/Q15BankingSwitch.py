'''Question 59: Develop a program to simulate a basic banking menu:
1: Deposit
2: Withdraw
3: Check Balance
4: Exit
Use a switch to handle user choice and print appropriate messages.
Asked In Just Practice assignment
Input:
Choice = 1 (Deposit)
Amount = 2000

Output
Amount Deposited. New Balance = 7000

Explanation:
When choice 1 is selected, deposit amount is added to balance.

Input:
Choice = 3

Output:
Current Balance = 5000

Explanation:
Choice 3 prints the current account balance.'''
print("1: Deposit")
print("2: Withdraw")
print("3: Check Balance")
print("4: Exit")

amt=int(input("Enter your amt\n"))
choice=int(input("Enter your choice\n"))


match choice:
    case 1:
        d=int(input("Enter deposite amt\n"))
        amt=amt+d
        print("Amount Deposite Balance =",amt)
    
    case 2:
        w=int(input("Enter withdraw amt\n"))
        amt=amt-w
        print("Amount withdraw Balance =",amt)
        
    case 3:
        print("Balance =",amt)
        
    case 4:
        print("Exit")
        exit()
