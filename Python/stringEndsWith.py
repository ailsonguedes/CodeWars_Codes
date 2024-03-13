def solution(text, ending):
    end = ""

    for i in text:
        end = text[-2:]

        if end == ending:
            return True
        else:
            return False


print(solution("abc", "bc"))
print(solution("abc", "d"))
