def intersect(a, b):
  
    asSet = set(a)

    rsSet = set()
    res = []

    for elem in b:
      
        if elem in asSet and elem not in rsSet:
            rsSet.add(elem)
            res.append(elem)

    return res

if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    b = [3, 2, 2, 3, 3, 2]

    res = intersect(a, b)
    print(" ".join(map(str, res)))