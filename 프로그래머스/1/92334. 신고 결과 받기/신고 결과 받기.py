def solution(id_list, report, k):
    report = set(report)
    
    # 신고당한 횟수 집계
    from collections import defaultdict
    report_count = defaultdict(int)
    user_reports = defaultdict(set)  # 누가 누구를 신고했는지 저장
    
    for rep in report:
        reporter, reported = rep.split()
        if reported not in user_reports[reporter]:
            user_reports[reporter].add(reported)
            report_count[reported] += 1

    suspended = {user for user, count in report_count.items() if count >= k}
    
    result = []
    for user in id_list:
        mails = len(user_reports[user] & suspended)
        result.append(mails)
    
    return result
