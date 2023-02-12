def highest_even(li): 
    he=0
    for num in li: 
        if (num % 2) == 0 and (num > he): 
            he=num
    return he 


print (f"The highest even number in the list is: {highest_even([6,3,62,12,35,27,9,24,1,20,16])}")