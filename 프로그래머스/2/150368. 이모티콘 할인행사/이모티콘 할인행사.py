from itertools import product

def solution(users, emoticons):
    discount_rates = [10, 20, 30, 40]
    answer = [0, 0]  

    for discounts in product(discount_rates, repeat=len(emoticons)):
        subscribers = 0  
        sales = 0

        for rate, limit in users:
            total = 0
            # 사용자가 구매하는 이모티콘 가격 합산
            for discount, price in zip(discounts, emoticons):
                if discount >= rate:
                    total += price * (100 - discount) // 100

            # limit 이상이면 구매 취소하고 서비스 가입
            if total >= limit:
                subscribers += 1
            else:
                sales += total

        if subscribers > answer[0] or (subscribers == answer[0] and sales > answer[1]):
            answer = [subscribers, sales]

    return answer
