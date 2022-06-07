A = [1,1,2,3,3]
B = [2,4,4,6]
C = [1,1,3]



def solution(A, K):
    n = len(A)
    for i in range(n - 1):
        #check if this list is a non-decreasing order
        if (A[i] > A[i + 1]):
            return False
        if (A[0] != 1 and A[n - 1] != K):
            return False
        else:
            return True

print(solution(A,3))
print(solution(C,2))
print(solution(B,6))
print(solution(B,8))