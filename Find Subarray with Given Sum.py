def subarraySum(arr, target):
    # Initialize window
    s, e = 0, 0
    res = []

    curr = 0
    for i in range(len(arr)):
        curr += arr[i]

        if curr >= target:
            e = i

            while curr > target and s < e:
                curr -= arr[s]
                s += 1

            if curr == target:
                res.append(s + 1)
                res.append(e + 1)
                return res

    return [-1]
  	
if __name__ == "__main__":
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    target = 23
    res = subarraySum(arr, target)

    print(" ".join(map(str, res)))