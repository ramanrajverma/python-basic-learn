
###
age = int(input("Enter the age: "))

if age < 0:
    print("You need to born - champ")
elif age < 18:
    print("You are not an adult")
else:
    print("You are a Super fit guy")


###
response = input("If user want food? Y/N: ")
if response == 'Y':
    print("Please give him a food")
else:
    print("No food needed")

###
# Boolean

for_sale = True
if for_sale:
    print("This item is for sale")
else: 
    print("This item is not for the sale")