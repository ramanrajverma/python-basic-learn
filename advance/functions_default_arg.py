#default arguments

"""def net_price(list_price, discount, tax):
    return list_price * (1-discount) * (1 + tax)"""

#To make fucntion default parameters
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1-discount) * (1 + tax)


print(net_price(500))

