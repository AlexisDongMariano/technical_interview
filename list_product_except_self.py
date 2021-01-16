# 0(n^2) brute force method
def list_product_except_self(input_list):
    output_list = []

    for i in range(len(input_list)):
        elements_product = 1
        for j in range(len(input_list)):
            if i == j:
                continue
            elements_product *= input_list[j]
        output_list.append(elements_product)
    
    return output_list


# 0(n) using division
def list_product_except_self2(input_list):
    output_list = []
    total_product = 1

    for i in input_list:
        total_product *= i
    
    for i in input_list:
        output_list.append(int(total_product / i))

    return output_list


# 0(n) but we used extra memory for 3 lists
# get the products to the left side of the index i and store in a separate list
# get the products to the right side of the index i and store in a separate list
# combine the two lists into output list
def list_product_except_self3(input_list):
    product_left = []
    product_right = []
    output_list = []

    product_left.append(1)

    for i in range(1, len(input_list)):
        product_left.insert(i, product_left[i - 1] * input_list[i - 1])

    product_right = product_left.copy()
    product_right[-1] = 1

    # iterable will become 3, 2, 1, 0 as it was reversed
    for i in reversed(range(len(input_list) - 1)):
        product_right[i] = product_right[i + 1] * input_list[i + 1]

    for i in range(len(input_list)):
        output_list.append(product_left[i] * product_right[i])
    
    return output_list


# 0(n) and better space complexity since we only manipulated 1 list
def list_product_except_self4(input_list):
    length = len(input_list)
    product_left = [0] * length

    product_left[0] = 1

    for i in range(1, length):
        product_left[i] = product_left[i - 1] * input_list[i - 1]

    x = 1
    for i in reversed(range(length)):
        product_left[i] = product_left[i] * x
        x *= input_list[i]

    return product_left

input_list = [1, 2, 3, 4, 5]

print(list_product_except_self(input_list))
print(list_product_except_self2(input_list))
print(list_product_except_self3(input_list))
print(list_product_except_self4(input_list))

