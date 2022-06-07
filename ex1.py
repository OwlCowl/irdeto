A = [1,1,2,3,3]
B = [2,4,4,6]
K = 3


def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        #compare current number
        if (A[i] + 1 < A[i + 1]):
            return False
        if (A[0] != 1 and A[n - 1] != K):
            return False
        else:
            return True

# print(solution(A,K))
# print(solution(B,8))
print(solution(B,6))