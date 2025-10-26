principle = rate = time = 0;

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be zero or negative number")
while rate <= 0:
    rate = float(input("Enter the rate amount: "))
    if rate <= 0:
        print("Rate cant be zero or negative number")
while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("Time cant be zero or negative number")

#total = principle(1+rate/100)*time
total = principle* pow((1+rate/100),time)



print("----------------------------------------")
print(f"Principle: ₹{principle}")
print(f"Rate: ₹{rate}%")
print(f"Time: {time}")

print("----------- Be Happy ---------------")
print(f"------------- Total Amount {total:,.2f}₹ --------------")