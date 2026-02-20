def getMin(arr, n):

    if n == 1:
        return arr[0]
    return min(arr[n - 1], getMin(arr, n - 1))


def getMax(arr, n):
    
    if n == 1:
        return arr[0]
    return max(arr[n - 1], getMax(arr, n - 1))


arr = [1, 423, 6, 46, 34, 23, 13, 53, 4]
n = len(arr)

print("Minimum element of array:", getMin(arr, n))
print("Maximum element of array:", getMax(arr, n))