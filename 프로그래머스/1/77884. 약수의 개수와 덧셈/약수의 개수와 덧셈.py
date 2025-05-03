import math

def solution(left, right):
    total = 0
    
    for num in range(left, right + 1):
        # 제곱수인 경우 약수의 개수가 홀수
        # 제곱수 판별: num의 제곱근이 정수인지 확인
        if math.isqrt(num) ** 2 == num:
            total -= num
        else:
            total += num
            
    return total