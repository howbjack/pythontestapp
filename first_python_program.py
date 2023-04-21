'''First Python Program'''
import math

# Function to Calculate Area

def calc_area (radius):
    '''Calculates the Radius'''
    area = math.pi * radius * radius
    return area

def calc_num_mult(the_num):
    '''Calculates the number to 3 powers'''
    timesten = 10 * the_num + the_num
    timeshundred = 100 * the_num + 10 * the_num + the_num
    res = the_num + timesten + timeshundred
    return res



r = float(input("Enter the Radius: "))
the_area=calc_area(r)
print(f"The area of the whole circle that we specified is {the_area}")

r = int(input("Enter the number: "))
the_result=calc_num_mult(r)
print(f"The multiplied number is: {the_result}")
