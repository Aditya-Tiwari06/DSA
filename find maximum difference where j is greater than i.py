def max_difference(arr):

    if not arr or len(arr) < 2:
        return None  # Not enough elements to compare

    min_element = arr[0]  # Track the smallest element so far
    max_diff = arr[1] - arr[0]  # Initialize with first possible difference

    for j in range(1, len(arr)):
      
        current_diff = arr[j] - min_element
        if current_diff > max_diff:
            max_diff = current_diff

        if arr[j] < min_element:
            min_element = arr[j]

    return max_diff if max_diff > 0 else None

nums = [2, 3, 10, 6, 4, 8, 1]
result = max_difference(nums)

if result is not None:
    print(f"Maximum difference (j > i) is: {result}")
else:
    print("No valid positive difference found.")