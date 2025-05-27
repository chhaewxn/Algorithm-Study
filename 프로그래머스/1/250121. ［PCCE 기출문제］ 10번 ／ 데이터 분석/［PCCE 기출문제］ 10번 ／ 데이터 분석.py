def solution(data, ext, val_ext, sort_by):
    column_index = {
        "code": 0,      # 코드번호
        "date": 1,      # 제조일
        "maximum": 2,   # 최대수량
        "remain": 3     # 현재수량
    }
    
    ext_index = column_index[ext]
    sort_index = column_index[sort_by]
    
    filtered_data = []
    for item in data:
        if item[ext_index] < val_ext:
            filtered_data.append(item)
    
    filtered_data.sort(key=lambda x: x[sort_index])
    
    return filtered_data