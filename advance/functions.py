
def happy_birthday(name, age):
    print(f"Hello {name}")
    print("Happy Birthday")
    print(f"Your age is : {age}")

happy_birthday("Raman", 20)

print("----------")

def display_invoice(uname, amount, date):
    print(f"Hello champ {uname}")
    print(f"Your electricity bill: {amount} INR")
    print(f"Last date is: {date}")
display_invoice("RamanRajVerma", 12, "16/05/25")


#------------------  Return statement __-------------

def add(x,y):
    z = x+y
    return z
    
print(add(2,3))

