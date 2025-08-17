
def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Namstey", "Mr.", "Raman", "Verma")
hello("Namstey", first="Raman", last="Verma", title="Mr.")

print("-------------")

for x in range(1,10):
    print(x, end=" ")  #end=" "  is a keyword argumnet
print()

print("1","2","3","4","5", sep="-")


def get_phone(country, area, first, last):
    return f"+{country}-{area}-{first}-{last}"
my_phone_num = get_phone(country=91, area=8968, first=30, last=4100)
print(my_phone_num)