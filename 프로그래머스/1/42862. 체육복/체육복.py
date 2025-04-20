def solution(n, lost, reserve):
    students = [1] * (n + 1)  
    
    # 여벌 체육복이 있는 학생은 +1
    for r in reserve:
        students[r] += 1
    
    # 체육복을 도난당한 학생은 -1
    for l in lost:
        students[l] -= 1
    
    # 체육복 빌려주기 과정
    for i in range(1, n + 1):
        # 체육복이 없는 학생인 경우
        if students[i] == 0:
            # 앞번호 학생에게 빌릴 수 있는지 확인
            if i > 1 and students[i - 1] == 2:
                students[i] = 1
                students[i - 1] = 1
            # 뒷번호 학생에게 빌릴 수 있는지 확인
            elif i < n and students[i + 1] == 2:
                students[i] = 1
                students[i + 1] = 1
    
    # 체육복이 있는 학생 수 계산 (0번 인덱스는 제외)
    return sum(1 for s in students[1:] if s > 0)