def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2
    shortage = total_cost - money
    
    return max(0, shortage)
