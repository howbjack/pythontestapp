import math

# Function to Calculate Area

def calc_area (radius):
    area = math.pi * radius * radius
    return area

r = float(input("Enter the Radius: "))
the_area=calc_area(r)
print(f"The area of the whole circle that we specified is {the_area}")

the_num = int(input("Enter the number: "))
timesten = 10 * the_num + the_num
timeshundred = 100 * the_num + 10 * the_num + the_num

the_result = the_num + timesten + timeshundred

print(f"The result for Dev1 is: {the_result}")
