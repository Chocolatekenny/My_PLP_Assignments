# Get user input
num1 = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))
             
# Perform calculation based on user input
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 == 0:
        result = "Error: Cannot divide by zero"
    else:
        result = num1 / num2
else:
    result = "Error: Invalid operation"
print(num1, operation, num2, "=", result)