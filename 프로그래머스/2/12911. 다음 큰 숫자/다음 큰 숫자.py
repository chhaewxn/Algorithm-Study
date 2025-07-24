def solution(n):
    count_ones = bin(n).count('1')  # n의 2진수에서 1의 개수
    next_num = n + 1

    while True:
        if bin(next_num).count('1') == count_ones:
            return next_num
        next_num += 1
