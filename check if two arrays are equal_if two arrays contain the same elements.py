from collections import Counter

def arrays_equal(arr1, arr2):
      
    if not isinstance(arr1, (list, tuple)) or not isinstance(arr2, (list, tuple)):
        raise TypeError("Both inputs must be lists or tuples.")

    if len(arr1) != len(arr2):
        return False

    return Counter(arr1) == Counter(arr2)


if __name__ == "__main__":
    a1 = [1, 2, 3, 2]
    a2 = [2, 3, 1, 2]
    a3 = [1, 2, 3]

    print(arrays_equal(a1, a2))
    print(arrays_equal(a1, a3))