import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    N = int(sys.stdin.readline().strip())
    rank = list(map(int, sys.stdin.readline().strip().split()))
    result = {}

    for data in rank:
        result[data] = result.get(data, 0) + 1

    fifth_goal_idx = [0] * (max(result.keys()) + 1)
    score_map = {}
    temp_map = {}
    score = 1

    for element in rank:
        if result[element] >= 6:
            temp_map[element] = temp_map.get(element, 0) + 1

            if temp_map[element] <= 4:
                score_map[element] = score_map.get(element, 0) + score

            if temp_map[element] == 5:
                fifth_goal_idx[element] = score
            score += 1

    key_data = list(score_map.keys())
    key_data.sort(key=lambda x: (score_map[x], fifth_goal_idx[x]))

    print(key_data[0])
