def get_min_max(ints):
    if not ints:
        return
    res = [-float("inf"), float("inf")]
    for i in ints:
        if i > res[0]:
            res[0] = i
        if i < res[1]:
            res[1] = i
    return res[1], res[0]

## Example Test Case of Ten Integers
import random
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")
print ("Pass" if (None == get_min_max([])) else "Fail")
