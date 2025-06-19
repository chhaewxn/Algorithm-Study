def solution(survey, choices):
    scores = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    score_map = [3, 2, 1, 0, 1, 2, 3]

    for idx in range(len(survey)):
        disagree, agree = survey[idx][0], survey[idx][1]
        choice = choices[idx]
        if choice < 4:
            scores[disagree] += score_map[choice - 1]
        elif choice > 4:
            scores[agree] += score_map[choice - 1]
        # choice == 4일 경우 점수 변화 없음

    result = ''
    pairs = [('R', 'T'), ('C', 'F'), ('J', 'M'), ('A', 'N')]

    for first, second in pairs:
        if scores[first] >= scores[second]:
            result += first
        else:
            result += second

    return result
