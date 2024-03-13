def open_or_senior(data):
    outArr = []

    for i in data:
        if i[0] >= 55 and i[1] > 7:
            outArr.append("Senior")

        else:
            outArr.append("Open")

    return outArr


print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
print(open_or_senior([[46, 4], [31, 20], [81, 21], [76, 7], [41, 8], [17, 2], [65, 14], [82, 24]]))
