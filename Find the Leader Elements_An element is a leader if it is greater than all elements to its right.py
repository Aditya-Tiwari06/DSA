def leaders(arr):
    result = []
    n = len(arr)

    maxRight = arr[-1]

    result.append(maxRight)

    for i in range(n - 2, -1, -1):
        if arr[i] >= maxRight:
            maxRight = arr[i]
            result.append(maxRight)

    result.reverse()

    return result

if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2]
    result = leaders(arr)
    print(" ".join(map(str, result)))