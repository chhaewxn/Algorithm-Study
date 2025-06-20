from itertools import combinations

def solution(relation):
    n_cols = len(relation[0])
    candidates = []

    for i in range(1, n_cols+1):
        for comb in combinations(range(n_cols), i):
            projection = set(tuple(item[idx] for idx in comb) for item in relation)
            if len(projection) == len(relation):
                is_minimal = True
                for cand in candidates:
                    if set(cand).issubset(set(comb)):
                        is_minimal = False
                        break
                if is_minimal:
                    candidates.append(comb)

    return len(candidates)
