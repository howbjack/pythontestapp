import math
def calc_area (radius):
    area = math.pi * radius * radius
    return area

r = int(input("Enter the Radius: "))
the_area=calc_area(r)
print(f"The area of the circle is {the_area}") 