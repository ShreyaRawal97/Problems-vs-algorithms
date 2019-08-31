def rearrange_digits(input_list):
    arr = reverse(input_list)
    l = len(input_list)
    if l <= 0:
        return [-1, -1]
    if l == 1:
        return [0, input_list[0]]
    x = 0
    i = 0
    while i < l:
        x = x*10 + arr[i]
        i += 2
    y = 0
    j = 1
    while j < l:
        y = y*10 + arr[j]
        j += 2
    return x, y

def partition(xs, start, end):
    follower = leader = start
    while leader < end:
        if xs[leader] <= xs[end]:
            xs[follower], xs[leader] = xs[leader], xs[follower]
            follower += 1
        leader += 1
    xs[follower], xs[end] = xs[end], xs[follower]
    return follower

def _quicksort(xs, start, end):
    if start >= end:
        return
    p = partition(xs, start, end)
    _quicksort(xs, start, p-1)
    _quicksort(xs, p+1, end)

def quicksort(xs):
    _quicksort(xs, 0, len(xs)-1)

def reverse(arr):
    input_list = list()
    quicksort(arr)
    for i in reversed(arr):
        input_list.append(i)
    return input_list

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)
test_function([[], [-1, -1]])
test_function([[0], [0, 0]])
test_function([[1], [0, 1]])
test_function([[0, 0], [0, 0]])
test_function([[0, 0, 1, 1, 5, 5], [510, 510]])
#all test cases pass
