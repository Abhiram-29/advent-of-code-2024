safe_cnt = 0

def isSafe(report):
    is_safe = True
    is_increasing = report[0]-report[1] < 0
    for i in range(len(report)-1):
        diff = report[i]-report[i+1]
        if is_increasing and (diff >= 0 or diff < -3):
            is_safe = False
            break
        elif is_increasing == False and diff <= 0 or diff > 3:
            is_safe = False
            break
    return is_safe

with open("Day2\input.txt") as reports:
    for r in reports:
        report = list(map(int,r.split()))
        if isSafe(report):
            safe_cnt += 1
        else:
            for i in range(len(report)):
                if isSafe(report[:i]+report[i+1:]):
                    safe_cnt += 1
                    break
print(safe_cnt)