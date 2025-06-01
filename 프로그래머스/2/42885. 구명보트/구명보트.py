def solution(people, limit):
    people.sort()  
    left, right, boats = 0, len(people)-1, 0
    
    while left <= right:
        # 가벼운 사람 + 무거운 사람 <= 제한인지 확인
        if people[left] + people[right] <= limit:
            left += 1  # 기벼운 사람도 태운다
        
        # 무거운 사람은 항상 
        right -= 1
        boats += 1
    
    return boats