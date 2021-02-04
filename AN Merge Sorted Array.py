
def merge_sorted_array(array1, array2):
    return sorted(array1 + array2)


def merge_sorted_array2(array1, array2):
    array3 = []
    len_array1 = len(array1)
    len_array2 = len(array2)
    index_array1 = index_array2 = 0

    while index_array1 != len_array1 - 1 or index_array2 != len_array2 - 1:
        if array1[index_array1] < array2[index_array2]:
            array3.append(array1[index_array1])
            index_array1 += 1
        else:
            array3.append(array2[index_array2])
            index_array2 += 1
        
    if array1[-1] < array2[-1]:
        array3.append(array1[-1])
        array3.append(array2[-1])
    else:
        array3.append(array2[-1])
        array3.append(array1[-1])
    
    return array3


array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]

print(merge_sorted_array(array1, array2))
print(merge_sorted_array2(array1, array2))

l1 = [1,2,3]