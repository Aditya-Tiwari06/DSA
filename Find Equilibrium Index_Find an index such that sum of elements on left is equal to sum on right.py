def equilibriumPoint(arr):
    prefSum = 0
    total = sum(arr)


    for pivot in range(len(arr)):
        suffSum = total - prefSum - arr[pivot]
        if prefSum == suffSum:
            return pivot
        prefSum += arr[pivot]

    return -1

if __name__ == "__main__":
    arr = [1, 7, 3, 6, 5, 6]

    result = equilibriumPoint(arr)
    print(result)