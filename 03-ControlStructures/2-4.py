# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("enter firs number:" ))
number2 = int(input("enter second number:" ))
operator = input("enter math operator:")
if operator == "+":
    velue=number1+number2
elif operator == "-":
    velue=number1-number2
elif operator == "*":
    velue=number1*number2
elif operator == "/":
    velue=number1/number2    
else: print("you entered wrong operatoor")
print(f'your velue = {velue}')