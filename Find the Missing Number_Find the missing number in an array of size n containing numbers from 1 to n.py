def missingNum(arr):
    n = len(arr) + 1

    totalSum = sum(arr)

    expSum = n * (n + 1) // 2

    return expSum - totalSum

if __name__ == '__main__':
    arr = [8, 2, 4, 5, 3, 7, 1]
    print(missingNum(arr))