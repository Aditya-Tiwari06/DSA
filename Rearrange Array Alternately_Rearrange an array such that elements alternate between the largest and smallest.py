def rearrange_alternately(arr):

    if not isinstance(arr, list) or not all(isinstance(x, (int, float)) for x in arr):
        raise ValueError("Input must be a list of numbers.")

    n = len(arr)
    if n <= 1:
        return arr[:] 

    arr.sort()
    result = []

    left, right = 0, n - 1
    while left <= right:
        if left != right:
            result.append(arr[right])  # Largest remaining
            result.append(arr[left])   # Smallest remaining
        else:
            result.append(arr[left])   # Middle element for odd length
        left += 1
        right -= 1

    return result

try:
    nums = [1, 2, 3, 4, 5, 6, 7]
    rearranged = rearrange_alternately(nums)
    print("Original array:", nums)
    print("Rearranged array:", rearranged)
except ValueError as e:
    print("Error:", e)