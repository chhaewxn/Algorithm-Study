from itertools import permutations

def solution(numbers):
    # 종이 조각으로 만들 수 있는 모든 숫자 찾기
    number_set = set()
    
    # 1자리부터 numbers의 길이까지 모든 순열 생성
    for i in range(1, len(numbers) + 1):
        perms = permutations(numbers, i)
        for perm in perms:
            # 순열을 숫자로 변환하여 집합에 추가
            number_set.add(int(''.join(perm)))
    
    # 소수 개수 카운트
    count = 0
    for num in number_set:
        if is_prime(num):
            count += 1
    
    return count

def is_prime(n):
    # 0과 1은 소수가 아님
    if n < 2:
        return False
    
    # 2는 소수
    if n == 2:
        return True
    
    # 짝수는 소수가 아님 (2 제외)
    if n % 2 == 0:
        return False
    
    # 3부터 n의 제곱근까지의 홀수로 나누어 떨어지는지 확인
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True