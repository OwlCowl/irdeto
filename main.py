numbers = [6, 4, 3,-5, 0, 2, -7, 1]
num2 = [-1,-3]


def solution(a):
    #remove duplicates
    a = list(dict.fromkeys(a))
    new_list = [i for i in range(1, (len(a)+1))]
    a.sort()
    #check if numbers positive
    for number in a:
        if number >0:
            difference = set(new_list).difference(set(a))
            if difference:
                element = next(iter(difference))
            else:
                element = a[-1] + 1
        else:
            new_list = 1
            return new_list

    return element


def minpositive(a):
    A = set(a)
    ans = 1
    while ans in A:
       ans += 1
    return ans

print(minpositive(num2))

