def solution(s):
    return [s[i : i + 2] for i in range(0, len(s), 2)]


print(solution("abc"))
print(solution("abcdef"))
print(solution("asdfads"))
