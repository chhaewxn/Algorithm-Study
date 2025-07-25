def solution(elements):
    n = len(elements)
    extended = elements * 2
    sums = set()

    for length in range(1, n + 1):
        curr_sum = sum(extended[0:length])
        sums.add(curr_sum)
        for start in range(1, n):
            curr_sum = curr_sum - extended[start - 1] + extended[start + length - 1]
            sums.add(curr_sum)
    
    return len(sums)
