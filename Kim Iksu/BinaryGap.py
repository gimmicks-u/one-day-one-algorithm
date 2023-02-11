# Codility
def solution(N):
    binN = bin(N)[2:]

    answer = 0
    gap = 0

    for ch in binN:
        if ch == "0":
            gap += 1
        else:
            if gap > answer:
                answer = gap
            gap = 0

    return answer
