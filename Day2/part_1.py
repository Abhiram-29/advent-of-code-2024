safe_cnt = 0
with open("Day2\input.txt",'r') as reports:
    for r in reports:
        report = list(map(int,r.strip().split()))
        is_increasing = report[0]-report[1] < 0
        is_safe = True
        for i in range(len(report)-1):
            diff = report[i]-report[i+1]
            if is_increasing and (diff >= 0 or diff < -3):
                    is_safe = False
                    break
            elif is_increasing == False and diff <= 0 or diff > 3:
                is_safe = False
                break
        if is_safe:
            safe_cnt += 1
print(safe_cnt)
        