def longest_consecutive(nums):

    if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
        raise ValueError("Input must be a list of integers.")

    num_set = set(nums)  # Remove duplicates and allow O(1) lookups
    longest = 0

    for num in num_set:
      
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest = max(longest, current_streak)

    return longest


if __name__ == "__main__":
    try:
        nums = [100, 4, 200, 1, 3, 2]
        print("Length of longest consecutive sequence:", longest_consecutive(nums))
    except ValueError as e:
        print("Error:", e)