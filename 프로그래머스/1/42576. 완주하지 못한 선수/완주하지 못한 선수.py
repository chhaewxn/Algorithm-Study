def solution(participant, completion):
    # 참가자와 완주자 이름을 저장할 딕셔너리 생성
    runner_count = {}
    
    # 참가자 이름을 해시 맵에 저장 (동명이인은 카운트 증가)
    for name in participant:
        if name in runner_count:
            runner_count[name] += 1
        else:
            runner_count[name] = 1
    
    # 완주자 이름을 해시 맵에서 제거 (동명이인은 카운트 감소)
    for name in completion:
        runner_count[name] -= 1
        # 해당 이름의 선수가 모두 완주한 경우 딕셔너리에서 제거
        if runner_count[name] == 0:
            del runner_count[name]
    
    # 남아있는 선수가 완주하지 못한 선수
    return list(runner_count.keys())[0]