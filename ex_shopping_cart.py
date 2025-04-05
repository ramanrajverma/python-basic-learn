item = input("What item would you like to buy?: ")
price = float(input("What is the price: "))
quantaty = int(input("How many would you like?: "))
total = price * quantaty
print(f"You have bought {quantaty} {item} X ₹{price}")
print(f"Your total is: ₹{total}")