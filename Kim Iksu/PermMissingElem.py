# Codility
def solution(A):
    A.sort()
    for i in range(len(A)):
        if (i + 1) != A[i]:
            return i + 1
    return len(A) + 1
