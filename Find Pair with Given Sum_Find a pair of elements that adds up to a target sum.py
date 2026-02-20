def twoSum(arr, target):
    
    res = []

    st = set()

    for i in range(len(arr)):
        
        complement = target - arr[i]

        if complement in st:
            res.append(complement)
            res.append(arr[i])
            break

        st.add(arr[i])
    
    return res

if __name__ == "__main__":
    arr = [2, 9, 10, 4, 15]
    target = 12

    res = twoSum(arr, target)

    for i in range(len(res)):
        print(res[i], end=" ")