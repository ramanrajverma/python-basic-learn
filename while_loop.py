name = input("Enter your name: ")


if name == "":
    print("No name enterd")
else:
    print(f"Your name is: {name}")


####
## Below loop will go infinite
"""while name == "":
    print("No name entered")
    print("Enter your name: ")
print(f"Your name is : {name}")"""

#e.g 2
age = input("Enter your age: ")
#print(type(age))
if age.isdigit():
    age = int(age)
    while age < 0 :
        print("No valid age: ")
        #age = int(input("Enter your age: "))
    print(f"Your age is {age}")
else:
    print("No valid age input")

#------------------------------------------------------------------"""
print("----------------------------------------")
food = input("Enter a food you like(input q to quit): ")
while not food == "q":
    print(f"You like food: {food}")
    food = input("Enter the food You like: ")
print("Bye-Bye")

print("--------------------------------------")
num = int(input("Enter the number between 1 to 10: "))
while num < 1 or num > 10:
    print("Not a valid number")
    num = int(input("Enter the number between 1 to 10: "))
print(f"Your entred number is : {num}")