
def rotateArr(arr, k):
    n = len(arr)

    k %= n
    
    temp = [0] * n

    for i in range(n - k):
        temp[i] = arr[k + i]

    
    for i in range(k):
        temp[n - k + i] = arr[i]

    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    d = 2

    rotateArr(arr, k)

    # Print the rotated array
    for i in range(len(arr)):
        print(arr[i], end=" ")