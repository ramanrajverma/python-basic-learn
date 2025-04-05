import math

print("-----------To find the Circumfrance of  Circle----------")
# calculate circumfrance of circle
#c = 2 π r

radius = float(input("Enter the radius of circle: "))
circumfrance = 2 * math.pi * radius
print(f"Circumfrance of circle: {round(circumfrance,2)}")

print("-----------To find the area of Circle ----------")
# Calculate area of circle
# a = π * r * r
area1  = math.pi * radius * radius
area2 = math.pi * pow(radius, 2)
print(f"Area1 of circle: {round(area1, 2)}")
print(f"Area2 of circle: {round(area2, 2)}")

#Area of right angle triangle
print("-----------To find the area of Triangle ----------")
a = float(input("Enter the side A: "))
b = float(input("Enter the side b: "))
c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Area of right angle triangle: {round(c,2)}")

