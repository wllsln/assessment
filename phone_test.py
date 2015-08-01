## given an unsorted integer array, find and return the 2nd largest number in that array

def second_largest(arr):
    if len(arr) < 2:
        raise Exception  # array is only one element
    sort_array = reverse(sorted(arr))  # array sorted from largets to smallest
    for index in range(1,len(sort_array)):
        if sort_array[0] > sort_array[index]:
            return sort_array[index]
    raise Exception   # no second largest element
        
def helper(first, second):
    if second > first:
        return second, first
    else:
        return first, second

def second_largest(arr):
    if len(arr) < 2:
        return "Array is only one element"

    largest, second = helper(arr[0], arr[1])

    for num in arr[2:]:  # start at the third element
        if largest == second:n
            largest, second = helper(largest, num)
        elif num < second:
            pass
        elif num > second:
            if num != largest:  # additional to capture [1,3,3] case
                largest, second = helper(largest, num)
        
    if largest == second:
        return "No largest element"
    
    return second     

# Test cases
# [1, 3, 5] => 3
# [0, 1]  => 0
# [0, 0, 0] => error
# [1] => error
# [-1, -4, 1, -3] => -1
# [2, 2, 1] => 1
# [1, 3, 3] => 1

print second_largest([1,3,5])
print second_largest([0,1])
print second_largest([-1,-4,1,-3])
print second_largest([2,2,1])
print second_largest([1,3,3])
print second_largest([0,0,0])
print second_largest([7])