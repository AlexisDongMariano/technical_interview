def first_recurring_character(nums):
    length = len(nums)

    if not nums or type(nums) != list:
        return 'argument is invalid'

    for i in range(length - 1):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                return nums[i]
    
    return 'no recurring number'


def first_recurring_character2(nums):
    nums_map = {}

    if not nums or type(nums) != list:
        return 'argument is invalid'

    for num in nums:
        if num in nums_map:
            return num
        else:
            nums_map[num] = True
    
    return 'no recurring number'


nums = [2, 5, 1, 2, 3, 5, 1, 2, 4]
nums2 = []
nums3 = [2, 3, 4, 5]

print(first_recurring_character(nums))
print(first_recurring_character(nums2))
print(first_recurring_character(nums3))

print(first_recurring_character2(nums))
print(first_recurring_character2(nums2))
print(first_recurring_character2(nums3))