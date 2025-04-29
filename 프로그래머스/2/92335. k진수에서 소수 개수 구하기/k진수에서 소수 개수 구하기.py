def solution(n, k):
    def convert_to_base_k(n, k):
        result = ""
        while n > 0:
            result = str(n % k) + result
            n //= k
        return result

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        
        i = 3
        while i * i <= num:
            if num % i == 0:
                return False
            i += 2
        
        return True
    
    # n을 k진수로 변환
    k_base_n = convert_to_base_k(n, k)
    
    # 변환된 수를 0을 기준으로 분리
    split_by_zero = k_base_n.split('0')
    
    count = 0
    for part in split_by_zero:
        if part and is_prime(int(part)):
            count += 1
    
    return count