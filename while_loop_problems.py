# Tasks / Requirements
# Implement a Python function print_numbers(n) that uses a while loop to print numbers from 1 to n (inclusive), where n is a positive integer provided as input to the function.
num=int(input("Enter Number : "))
c=1
while num>=c:
    print(c)
    c+=1
# Write a Python program that simulates a simple bank account system. The system should use a while loop to continuously prompt the user for actions (deposit, withdraw, check balance) until the user decides to exit. The initial balance should be $1000.
intial_balance=1000
while True:
    choice=int(input("Enter Actions : \n1.checkbalance, 2.deposit 3.withdraw,And 4.Exit : "))
    if choice==1:
        print(f"${intial_balance}")
    elif choice==2:
        deposit_ammount=float(input("Enter Deposite Ammount $: "))
        intial_balance+=deposit_ammount
        print(f"${deposit_ammount} is Sucessfully deposited Into your Account")
    elif choice==3:
        withdraw_ammount=int(input("Enter Withdraw ammount $: "))
        if withdraw_ammount<intial_balance:
            intial_balance-=withdraw_ammount
            print(f"${withdraw_ammount} is sucessfully Completed ")
        else:
            print("Invalid Ammount \nplease Check your Balance")
    else:
        break

# Create a function find_factorial(n) that calculates the factorial of a given number n using a while loop. The function should handle cases where n is less than 0 by raising a ValueError.
num=int(input("Enter number: "))
factorial_number=1
c=1
while c<=num:
    factorial_number*=c
    c+=1
print(factorial_number)
# Develop a simple number guessing game where the computer thinks of a number between 1 and 100, and the user has to guess it. After each guess, the computer should give a hint (higher or lower) using a while loop to repeatedly ask for guesses until the correct number is guessed
import random as rd
num=rd.randint(1,100)
while True:
    guess=int(input("Guess a number : "))
    if guess>100 or guess<1:
        print(f"{guess} is Out of range please enter number between 1 to 100 ")
    elif guess>num:
        print("Hint TO High ... Try again")
    elif guess<num:
        print("Hint TO low ... Try again")
    else:
        print("Congratulations! You guessed it right.")
        break

