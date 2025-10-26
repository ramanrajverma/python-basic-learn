"""*args=      allow you to pass multiple non-key argumentrs
**kwargs=   allow you to pass multiple keywords argumentrs"""


def add(a, b):
    return a+b;

#print(add(1,2,3))   #problem to pass dynamic or random number of arguments




def add_new(*args):
    print(type(args))
    total=0
    for arg in args:
        total += arg
    return total

print(add_new(1,2,3,6,8,1)) 

#**kwargs -------------------------

def my_address(**kwargs):
    print(type(kwargs))
    for value in kwargs.values():
        print(value)

    print("---------")


    for key, val in kwargs.items():
        print(f"{key}:{val}")

my_address(village="Chamyar",
           PO="Tihra",
           Teh="Sarkaghat",
           Distt="Mandi",
           State="H.P")