def union_arrays_python(arr1, arr2):
    
    return list(set(arr1) | set(arr2))

array1 = [10, 20, 30]
array2 = [20, 30, 40]

result = union_arrays_python(array1, array2)
print("Union of arrays:", result)