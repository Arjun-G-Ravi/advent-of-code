with open('Day2/input.txt', 'r') as f:
    data = f.read()

reports = data.split('\n')
safe_ct = 0
not_safe_ct = 0

for report in reports:
    if report:
        levels = report.split(' ')
        # if sorted(levels) != sorted(list(set(levels))):
        #     print(levels)
        #     continue
        levels = list(map(int, levels))
        isReportSafe = True
        if sorted(levels) == levels:
            for i in range(1, len(levels)):
                if 1 <= abs(int(levels[i]) - int(levels[i-1])) and abs(int(levels[i]) - int(levels[i-1])) <= 3:
                    pass
                else:
                    isReportSafe = False
                    not_safe_ct += 1
                    print(report)
                    break
            if isReportSafe:
                safe_ct += 1
        
        elif sorted(levels, reverse=True) == levels:
            for i in range(1, len(levels)):
                if 1 <= abs(int(levels[i]) - int(levels[i-1])) and abs(int(levels[i]) - int(levels[i-1])) <= 3:
                    pass
                else:
                    isReportSafe = False
                    not_safe_ct += 1
                    print(report)
                    break
            if isReportSafe:
                safe_ct += 1
        else:
            not_safe_ct += 1

print(safe_ct)
print(not_safe_ct)
