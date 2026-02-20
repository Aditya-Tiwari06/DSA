def calculate_sum(arr):
    total_sum = 0
    for num in arr:
        total_sum += num
    return total_sum

arr = [5, 15, 25, 35]
print(f"The sum is: {calculate_sum(arr)}")
