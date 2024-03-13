def solution(s):
    ret = [s[i : i + 2] for i in range(0, len(s), 2)]
    count = 0

    for i in ret:
        for j in i:
            count += 1
            ret = [i + "_" if len(i) == 1 else i for i in ret]

    return ret


print(solution("abc"))
print(solution("abcdef"))
print(solution("asdfads"))
