from itertools import groupby

word = "babaa"
word2 = "bbbab"
word3 = "bbbaaabbb"

def solution(S):
    lst = []
    loop = [list(g) for k, g in groupby(S)]
    #return list for investigation
    for data in loop:
        lst.append("".join(data))
    #find the longest element in list
    maxEl = max(lst, key = len)
    #compare with others element
    #count the difference in length
    #count the sum of missed elements
    count = sum([(len(maxEl) - len(data)) for data in lst])
    return count


print(solution(word))
print(solution(word2))
print(solution(word3))

