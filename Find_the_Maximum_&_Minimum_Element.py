def find_max_min(arr):
    if not arr:
        return None, None

    # Initialize with the first element
    max_val = arr[0]
    min_val = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]
            
    return max_val, min_val

data = [3, 5, 1, 2, 4, 8]
maximum, minimum = find_max_min(data)
print(f"Maximum is {maximum} and Minimum is {minimum}")
