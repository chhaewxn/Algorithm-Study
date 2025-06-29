def solution(skill, skill_trees):
    count = 0
    
    for tree in skill_trees:
        filtered = ''.join([s for s in tree if s in skill])
        # skill의 접두사인지 확인
        if skill.startswith(filtered):
            count += 1
            
    return count
