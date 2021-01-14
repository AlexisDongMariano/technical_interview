
# ==============================
#         Information
# ==============================

# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# Example:
    # Input:
    #     num_list = [10, 15, 3, 7]
    #     k = 17	
    # Output:
    #     True --> since 10 + 7 = 17
# Language: Python

# ==============================
#         Solution
# ==============================

# Solution No. 1
# Brute force method with O(n^2)
# consider converting the list into a set to remove duplicates
def does_addends_exists(num_list, k):
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if num_list[i] + num_list[j] == k:
                return True
    return False


# Solution No. 2
# O(n)
def does_addends_exists2(num_list, k):
    num_set = set(num_list)

    for i in num_set:
        other_number = k - i
        if other_number in num_set:
            return True
    return False


# Example inputs
num_list = [10, 15, 3, 7]
k = 17

print(does_addends_exists(num_list, k))
print(does_addends_exists2(num_list, k))