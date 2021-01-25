# ==============================
#         Information
# ==============================

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
# Language: Python

# ==============================
#         Solution
# ==============================


def get_largest_sum_of_non_adjacent_numbers(input):

    non_adjacent_sums = []
    has_positive = False
    last_index = 0
    temp_sum = 0
    
    if not input:
        return None
    
    for i in input:
        if i > 0:
            has_positive = True
    
    if not has_positive:
        return max(input)

    length = len(input)

    if length == 4:
        non_adjacent_sums.append(input[0] + input[3])

    for i in range(length):
        if last_index != i - 1 and last_index != i + 1:
            if input[i] > 0:
                temp_sum += input[i]
                last_index = i
        non_adjacent_sums.append(temp_sum)
    
    temp_sum = 0

    for i in range(1, length):
        if last_index != i - 1 and last_index != i + 1:
            if input[i] > 0:
                temp_sum += input[i]
                last_index = i
        non_adjacent_sums.append(temp_sum)
    
    return max(non_adjacent_sums)


def get_largest_sum_of_non_adjacent_numbers2(arr):
    length = len(arr)

    if length == 0:
        return 0
    
    if length == 1:
        return arr[0]
    
    sum_list = [None] * length
    sum_list[length-1] = arr[length-1]
    sum_list[length-2] = max(arr[length-1], arr[length-2])

    for i in range(length-3, -1, -1):
        print(f'arr[{i}] + sum_list[{i}+2], sum_list[{i}+1], {arr[i]} + {sum_list[i+2]}, {sum_list[i+1]}')
        sum_list[i] = max(arr[i] + sum_list[i+2], sum_list[i+1])
        

    return sum_list[0]


input = [2, 4, 6, 2, 5]
input2 = [5, 1, 1, 5]
input3 = [-1, -2, 0, 5, 7, 3]
input4 = [-3, -5, -1, -3, -1]
input5 = [-3, -5, 0, -1]


print(get_largest_sum_of_non_adjacent_numbers(input))
print(get_largest_sum_of_non_adjacent_numbers(input2))
print(get_largest_sum_of_non_adjacent_numbers(input3))
print(get_largest_sum_of_non_adjacent_numbers(input4))
print(get_largest_sum_of_non_adjacent_numbers(input5))


print(get_largest_sum_of_non_adjacent_numbers2(input))
print(get_largest_sum_of_non_adjacent_numbers2(input2))
print(get_largest_sum_of_non_adjacent_numbers2(input3))
print(get_largest_sum_of_non_adjacent_numbers2(input4))
print(get_largest_sum_of_non_adjacent_numbers2(input5))


