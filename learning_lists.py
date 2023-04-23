"""Gets the highest even number from a list"""
def get_highest_even(thelist):
    """Traverses list"""
    highest_even=0
    for num in thelist:
        if (num % 2) == 0 and (num > highest_even):
            highest_even=num
    return highest_even


mylist = [6,3,62,12,35,27,9,24,1,20,16]
print (f"The highest even number in the list is: {get_highest_even(mylist)}")
