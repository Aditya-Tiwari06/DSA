def findDuplicates(arr):
    
    n = len(arr)
    freq = [0] * (n + 1)  
    ans = []

    for num in arr:
        freq[num] += 1

    for i in range(1, n + 1):
        if freq[i] == 2:
            ans.append(i)

    return ans

if __name__ == "__main__":
    arr = [2, 3, 1, 2, 3]
    res = findDuplicates(arr)

    for ele in res:
        print(ele, end=' ')
    print()