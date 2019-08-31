def sort_012(input_list):
    low = 0
    high = len(input_list) - 1
    index = 0
    while index <= high:
        if input_list[index] == 0:
            input_list[index] = input_list[low]
            input_list[low] = 0
            low = low + 1
            index = index + 1
        elif input_list[index] == 1:
            index = index + 1
        else:
            input_list[index] = input_list[high]
            input_list[high] = 2
            high = high - 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

test_function([0, 0, 0, 0, 0, 0])
test_function([])
