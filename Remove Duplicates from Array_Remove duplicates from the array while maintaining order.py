def remove_duplicates_ordered(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list.")
    
    seen = set()
    result = []
    
    for item in arr:
        # Only add if not seen before
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

if __name__ == "__main__":
    try:
        data = [1, 3, 2, 3, 4, 1, 5, 2, 6]
        print("Original list:", data)
        unique_list = remove_duplicates_ordered(data)
        print("List without duplicates (order preserved):", unique_list)
    except Exception as e:
        print("Error:", e)