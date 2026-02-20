def find_majority_element(nums):

    if not nums:
        raise ValueError("Input list cannot be empty.")

    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    if nums.count(candidate) > len(nums) // 2:
        return candidate
    else:
        raise ValueError("No majority element found.")

if __name__ == "__main__":
    try:
        nums = [2, 2, 1, 1, 1, 2, 2]
        result = find_majority_element(nums)
        print(f"Majority element is: {result}")
    except ValueError as e:
        print(e)