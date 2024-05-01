# 11501 주식

import sys

# 테스트 케이스의 수를 입력받습니다.
T = int(sys.stdin.readline())

for _ in range(T):
    # 주식 가격의 개수 입력
    n = int(sys.stdin.readline())
    # 주식 가격 입력
    prices = list(map(int,sys.stdin.readline().split()))
    
    # 최대 이익을 저장할 변수
    max_profit = 0
    # 뒤에서부터 확인할 현재 최대 주식 가격
    max_price = 0
    
    # 뒤에서부터 주식 가격을 확인
    for i in range(n-1, -1, -1):
        # 현재 확인하고 있는 가격
        current_price = prices[i]
        # 현재 가격이 현재까지의 최대 가격보다 큰 경우, 최대 가격을 현재 가격으로 갱신
        if current_price > max_price:
            max_price = current_price
        # 현재 가격이 최대 가격보다 작은 경우, 이 차이만큼 이익을 얻을 수 있으므로 최대 이익에 더해줍니다.
        else:
            max_profit += max_price - current_price
    
    # 최대 이익 출력
    print(max_profit)
