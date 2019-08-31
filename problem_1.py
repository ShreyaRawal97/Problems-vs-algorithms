def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0 or number == 1:
        return number
    if number < 0:
        return None
    s = 1
    e = number/2
    while s <= e:
        mid = (s+e)//2
        if (mid*mid == number):
            return mid
        if mid*mid < number:
            s = mid+1
            res = mid
        else:
            e = mid - 1
    return res


#Test Case 1
print ("Pass" if  (3 == sqrt(9)) else "Fail") #pass

#Test Case 2
print ("Pass" if  (0 == sqrt(0)) else "Fail") #pass

#Test Case 3
print ("Pass" if  (4 == sqrt(16)) else "Fail") #pass

#Test Case 4
print ("Pass" if  (1 == sqrt(1)) else "Fail") #pass

#Test Case 5
print ("Pass" if  (5 == sqrt(27)) else "Fail") #pass

print ("Pass" if  (None == sqrt(-9)) else "Fail") #pass
