def solution(s):
    answer = len(s) 
    
    # 1부터 len(s)//2 + 1 까지 단위를 시도
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]  
        count = 1
        
        # step 크기만큼 건너뛰면서 비교
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                compressed += (str(count) + prev) if count >= 2 else prev
                prev = s[i:i+step]
                count = 1
        
        compressed += (str(count) + prev) if count >= 2 else prev
        answer = min(answer, len(compressed))
    
    return answer
