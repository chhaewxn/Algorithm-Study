import re

def solution(files):
    def parse_file_name(file):
        # HEAD: 숫자가 아닌 문자가 하나 이상
        # NUMBER: 1-5자리 숫자
        # TAIL: 그 나머지 부분
        match = re.match(r'([^\d]+)(\d{1,5})(.*)', file)
        
        if match:
            head, number, tail = match.groups()
            return (head.lower(), int(number), file)
        
        return (file.lower(), 0, file)  # 예외 경우 처리
    
    parsed_files = [(file, parse_file_name(file)) for file in files]
    
    # HEAD 기준 사전 순(대소문자 무시), NUMBER 기준 숫자 순, 입력 순서 유지(원본 파일명)
    sorted_files = sorted(parsed_files, key=lambda x: (x[1][0], x[1][1]))
    
    return [file[0] for file in sorted_files]