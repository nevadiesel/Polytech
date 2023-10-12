'''Given three arrays of integers, return the sum of elements that are common in all three arrays.

For example: 

common([1,2,3],[5,3,2],[7,3,2]) = 5 because 2 & 3 are common in all 3 arrays
common([1,2,2,3],[5,3,2,2],[7,3,2,2]) = 7 because 2,2 & 3 are common in the 3 arrays'''


def common(array1, array2, array3):
    common_elements = []
    for num in array1:
        if num in array2 and num in array3:
            common_elements.append(num)
            array2.remove(num)
            array3.remove(num)
    return sum(common_elements)


print(common([1, 2, 3], [5, 3, 2], [7, 3, 2]))
print(common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]))
