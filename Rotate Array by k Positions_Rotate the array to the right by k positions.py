def rotateclockwise(arr, k):
    n = len(arr)
    
    k = k % n

    res = [0] * n

    for i in range(n):
        if i < k:
            
            res[i] = arr[n + i - k]  
        else:
            
            res[i] = arr[i - k]      

    for i in range(n):
        arr[i] = res[i]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    rotateclockwise(arr, k)
    for it in arr:
        print(it, end=" ")