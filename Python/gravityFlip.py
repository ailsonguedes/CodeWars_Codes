def flip(d, a):
    arr = a

    if d == "R":
        ordarr = sorted(arr)
        return ordarr
    elif d == "L":
        ordarr = sorted(arr, reverse=True)
        return ordarr


print(flip("R", [3, 2, 1, 2]))
print(flip("L", [1, 4, 5, 3, 5]))
