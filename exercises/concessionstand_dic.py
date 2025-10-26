
print("--------------- Menu -------------------------")
menu = {"daalmakhni": 10.00,
        "vegbiryani": 20.00,
        "rotti": 2.00,
        "greensalad": 3.00,
        "pannerkhadi": 20.00}
cart = []
total = 0

for key, value in menu.items():
    print(f"{key} ---- INR {value: <.2f}")

print("--------------- Menu -------------------------")

while True:
    food = input("Select an item(q to  quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
    else:
        print(f"This food not in menu list {food}")


print("--------- Your order-----------")

#print(f"Your ordered food: {cart}")
for food in  cart:
    total += menu.get(food)
    print(food, end=" ")
print()
print(f"Your order total:--- INR {total}")


        

