def pyramid(n):
    arr = []

    for i in range(1, n + 1):
        arr.append([1] * i)

    return arr


print(pyramid(0))
print(pyramid(1))
print(pyramid(2))
print(pyramid(3))
