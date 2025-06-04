from itertools import permutations

def is_match(user, banned):
    
    if len(user) != len(banned):
        return False

    for uc, bc in zip(user, banned):
        if bc == '*':  
            continue
        if uc != bc:  
            return False
    return True

def solution(user_id, banned_id):
    result = set() 

    for candidate in permutations(user_id, len(banned_id)):
        matched = True
        # 각 순열 후보를 banned_id에 매핑
        for i in range(len(banned_id)):
            if not is_match(candidate[i], banned_id[i]):
                matched = False
                break  # 한 개라도 안 맞으면 다음 순열로 넘어감
        if matched:
            # 중복 제거 위해 정렬해서 tuple로 저장
            result.add(tuple(sorted(candidate)))

    return len(result)
