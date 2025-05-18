def solution(record):
    user_nicknames = {}
    
    actions = []
    
    for log in record:
        parts = log.split()
        command = parts[0]
        
        if command == "Enter":
            user_id, nickname = parts[1], parts[2]
            user_nicknames[user_id] = nickname
            actions.append(("Enter", user_id))
        elif command == "Leave":
            user_id = parts[1]
            actions.append(("Leave", user_id))
        elif command == "Change":
            user_id, nickname = parts[1], parts[2]
            user_nicknames[user_id] = nickname
    
    result = []
    for action, user_id in actions:
        nickname = user_nicknames[user_id]
        
        if action == "Enter":
            result.append(f"{nickname}님이 들어왔습니다.")
        elif action == "Leave":
            result.append(f"{nickname}님이 나갔습니다.")
    
    return result