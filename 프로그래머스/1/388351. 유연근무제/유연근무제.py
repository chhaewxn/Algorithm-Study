def solution(schedules, timelogs, startday):
    def add_10_minutes(time):
        h = time // 100
        m = time % 100
        m += 10
        if m >= 60:
            h += 1
            m -= 60
        return h * 100 + m

    def is_weekday(day_idx):
        return (startday + day_idx) % 7 not in [0, 6]

    n = len(schedules)
    count = 0

    for i in range(n):
        hope = schedules[i]
        limit = add_10_minutes(hope)
        success = True
        for day in range(7):
            if not is_weekday(day):
                continue
            if timelogs[i][day] > limit:
                success = False
                break
        if success:
            count += 1

    return count
