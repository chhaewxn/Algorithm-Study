from collections import Counter

def solution(str1, str2):
    # 두 글자씩 끊어서 다중집합의 원소 만들기
    set1 = make_multiset(str1)
    set2 = make_multiset(str2)
    
    # 두 다중집합이 모두 공집합인 경우
    if not set1 and not set2:
        return 65536
    
    counter1 = Counter(set1)
    counter2 = Counter(set2)
    
    intersection = counter1 & counter2  
    union = counter1 | counter2  
    
    intersection_size = sum(intersection.values())
    union_size = sum(union.values())
    
    jaccard = intersection_size / union_size
    
    # 결과 반환 (65536을 곱한 후 정수부만)
    return int(jaccard * 65536)

def make_multiset(s):
    result = []
    
    s = s.lower()
    
    for i in range(len(s) - 1):
        # 두 글자가 모두 영문자인 경우만 포함
        if s[i].isalpha() and s[i+1].isalpha():
            result.append(s[i:i+2])
            
    return result