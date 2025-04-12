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
if age.isdigit():
    while age<0 :
        print("No valid age: ")
        #age = int(input("Enter your age: "))
    print(f"Your age is {age}")
print("No valid age input")
