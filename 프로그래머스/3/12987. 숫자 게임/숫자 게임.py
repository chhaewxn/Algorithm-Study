
def solution(A, B):
    A.sort()
    B.sort()
    
    score = 0
    
    a_idx = 0
    b_idx = 0
    
    while a_idx < len(A) and b_idx < len(B):
        if B[b_idx] > A[a_idx]:
            score += 1  
            a_idx += 1  
            b_idx += 1 
        else:
            # 이길 수 없으면 가장 작은 수를 가진 B 버림
            b_idx += 1 
    return score