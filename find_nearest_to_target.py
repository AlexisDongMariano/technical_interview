# ==============================
#         Information
# ==============================

# Given 2 lists, list_a and list_b, and a number, target, find two numbers, one from list_a
# and one from list_b which when added is equal or closest to the target
# Example:
    # Input:
    #     list_a = [-1, 3, 8, 2, 9, 5]
    #     list_b = [4, 1, 2, 10, 5, 20]
    #     target = 24	
    # Output:
    #     (5, 20) or
    #     (3, 20)
# Language: Python

# ==============================
#         Solution
# ==============================

# Solution No. 1
# Brute force method with O(n^2)
def find_nearest_to_target(list_a, list_b, target):
	temp_difference = abs(list_a[0] - list_b[0])
	for i in list_a:
		for j in list_b:
			pair_sum = i + j
			if temp_difference >= abs(target - pair_sum):
				temp_difference = abs(target - pair_sum)
				addend1 = i
				addend2 = j
	return (addend1, addend2)


# Solution No. 2
# O(x*n) where x is the number of times the list a iterated
def find_nearest_to_target2(list_a, list_b, target):
	# first list is converted into a set to eliminate duplicates
	set_a = set(list_a)

	loop_counter = 0
	is_add = True
	# we only exit the loop if we found addends that exists in list_a and list_b
	# which the sum is equal or closest to the target
	while True:
		for i in list_b:
			missing_num = target - i
			if missing_num in set_a:
				return missing_num, i
		
		loop_counter += 1
		if is_add:
			target = target + loop_counter
			is_add = False
		else:
			target = target - loop_counter
			is_add = True


# Example inputs
list_a = [-1, 3, 8, 2, 9, 5]
list_b = [4, 1, 2, 10, 5, 20]
target = 24	

print(find_nearest_to_target(list_a, list_b, target))
print(find_nearest_to_target2(list_a, list_b, target))