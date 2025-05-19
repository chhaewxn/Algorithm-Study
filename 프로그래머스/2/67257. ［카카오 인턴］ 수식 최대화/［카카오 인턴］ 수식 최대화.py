from itertools import permutations

def solution(expression):
    operators = []
    if '+' in expression:
        operators.append('+')
    if '-' in expression:
        operators.append('-')
    if '*' in expression:
        operators.append('*')
    
    numbers = []  # 숫자 리스트
    ops = []      # 연산자 리스트
    num = ""
    for char in expression:
        if char in '+-*':
            numbers.append(int(num))
            ops.append(char)
            num = ""
        else:
            num += char
    numbers.append(int(num))  # 마지막 숫자 추가
    
    # 가능한 모든 연산자 우선순위 조합 생성
    max_result = 0
    for op_priority in permutations(operators):
        tmp_numbers = numbers.copy()  
        tmp_ops = ops.copy()
        
        for op in op_priority:
            i = 0
            while i < len(tmp_ops):
                if tmp_ops[i] == op:
                    if op == '+':
                        tmp_numbers[i] = tmp_numbers[i] + tmp_numbers[i+1]
                    elif op == '-':
                        tmp_numbers[i] = tmp_numbers[i] - tmp_numbers[i+1]
                    else:  
                        tmp_numbers[i] = tmp_numbers[i] * tmp_numbers[i+1]
                    
                    tmp_numbers.pop(i+1)
                    tmp_ops.pop(i)
                else:
                    i += 1
        
        max_result = max(max_result, abs(tmp_numbers[0]))
    
    return max_result