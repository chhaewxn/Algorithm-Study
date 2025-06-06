from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []  

    for course_len in course:
        course_combinations = [] 
        
        for order in orders:
            # AC와 CA는 동일한 조합으로 취급해야 함
            sorted_order = sorted(order)
            
            combis = combinations(sorted_order, course_len)

            for combi in combis:
                course_combinations.append(''.join(combi))

        counter = Counter(course_combinations)

        # 조합이 2번 이상 등장한 경우만 고려
        if counter:
            max_order = max(counter.values())
            if max_order >= 2:
                for menu, freq in counter.items():
                    if freq == max_order:
                        answer.append(menu)

    answer.sort()
    return answer
