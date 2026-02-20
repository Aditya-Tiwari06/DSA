def mergeArrays(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    i = j = 0

    merged = []

    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < n:
        merged.append(arr1[i])
        i += 1

    while j < m:
        merged.append(arr2[j])
        j += 1

    for i in range(n):
        arr1[i] = merged[i]

    for j in range(m):
        arr2[j] = merged[n + j]

if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6, 8]

    mergeArrays(arr1, arr2)

    print(*arr1)
    print(*arr2)