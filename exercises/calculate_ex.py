operator = input("Enter an operator (+ - * /): ")
if operator != "+" and operator != "-" and operator != "*" and  operator != "/":
    print(f"Not a valid operaor: {operator}")
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
result = 0
if operator == "+":
    result = num1+num2
elif operator == "-":
    result = num1-num2
elif operator == "-":
    result = num1*num2
elif operator == "/":
    result = num1/num2
#else:
#    print("Good Luck!!!")
print(f"Result of the operation: {round(result)}")

