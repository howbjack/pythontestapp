import math
def calc_area (radius):
    area = math.pi * radius * radius
    return area

r = int(input("Enter the Radius: "))
the_area=calc_area(r)
print(f"The area of the circle is {round(the_area,2)}") 
the_circum= 2*math.pi*r
print(f"The circumfrence is: {round(the_circum,2)} ")