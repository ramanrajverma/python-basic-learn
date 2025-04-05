weight = float(input("Please enter the weight: "))
unit = input("Please enter the unit: K/L: ")
result = 0
if unit == "K":
    result = weight*2.205
    unit = "LBS"
elif unit == "L":
    result = weight/2.205
    unit = "KG"
else:
    print("No conversion")
print(f"Your weight is {round(result)} {unit}")
