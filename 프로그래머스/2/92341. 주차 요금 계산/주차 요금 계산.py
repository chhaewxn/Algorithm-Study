import math
from collections import defaultdict

def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    
    parking_records = {}
    total_time = defaultdict(int)
    
    for record in records:
        time, car_number, action = record.split()
        
        hours, minutes = map(int, time.split(':'))
        minutes_time = hours * 60 + minutes
        
        if action == "IN":
            parking_records[car_number] = minutes_time
        else:  # action == "OUT"
            in_time = parking_records[car_number]
            del parking_records[car_number]  # 출차 처리
            
            # 주차 시간 누적
            total_time[car_number] += minutes_time - in_time
    
    # 출차 기록이 없는 차량 처리 
    end_of_day = 23 * 60 + 59  # 23:59
    for car_number, in_time in parking_records.items():
        total_time[car_number] += end_of_day - in_time
    
    result = []
    for car_number in sorted(total_time.keys()):
        time = total_time[car_number]
        
        if time <= base_time:
            fee = base_fee
        else:
            additional_time = time - base_time
            additional_units = math.ceil(additional_time / unit_time)
            fee = base_fee + additional_units * unit_fee
        
        result.append(fee)

    return result