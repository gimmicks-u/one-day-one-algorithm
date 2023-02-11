# Codility
def solution(A):
    front = A[0]
    back = sum(A) - A[0]
    answer = [abs(front - back)]

    for i in range(1, len(A) - 1):
        front += A[i]
        back -= A[i]
        answer.append(abs(front - back))

    return min(answer)
