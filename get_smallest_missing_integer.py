# ==============================
#         Information
# ==============================

# Reverse a list

# Example:
    # Input:
    # input = [5, 4, 3, 2 ,1]
    # output = [1, 2, 3, 4, 5]
# Language: Python

# ==============================
#         Solution
# ==============================

def reverse_list(input):
    output = []

    for i in reversed(range(len(input))):
        output.append(input[i])
    
    return output


def reverse_list2(input):
    length = int(len(input) / 2)

    for i in range(length):
        right = len(input) - 1 - i
        temp = input[i]
        input[i] = input[right]
        input[right] = temp
        
    return input


input = [5, 4, 3, 2 ,1]

print(reverse_list(input))
print(reverse_list2(input))


