def solution(n):
    answer = 0
    k = 1
    while k * (k+1) // 2 <= n:
        numerator = n-(k*(k-1)) // 2
        if numerator % k == 0:
            answer += 1
        k += 1
    return answer