
"""# To skip the iteration at a point"""
for num in range(1, 15):
    if num == 13:
       # print(f"------- Its a lucky number: {num}--------")
        continue
    else:
        print(num)

"""
# To break the iteration at a point
 break"""
print("----------------------- With Break ---------------")
for num in range(1, 10):
    if num == 5:
        break
    else:
        print(num)


