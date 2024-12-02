with open('Day2/input.txt', 'r') as f:
    data = f.read()

reports = data.split('\n')
safe_ct = 0
not_safe_ct = 0

from print_color import print

def calculate_safe(levels):
    # levels = list(map(int, levels))
    isReportSafe = True
    if sorted(levels) == levels:
        for i in range(1, len(levels)):
            if 1 <= abs(int(levels[i]) - int(levels[i-1])) and abs(int(levels[i]) - int(levels[i-1])) <= 3:
                pass
            else:
                isReportSafe = False
                return 0
                print(report)
                break
        if isReportSafe:
            return 1
    
    elif sorted(levels, reverse=True) == levels:
        for i in range(1, len(levels)):
            if 1 <= abs(int(levels[i]) - int(levels[i-1])) and abs(int(levels[i]) - int(levels[i-1])) <= 3:
                pass
            else:
                isReportSafe = False
                return 0
                print(report)
                break
        if isReportSafe:
            return 1
    else:
        return 0

def remove_one_lists(l):
    out = []
    for i in l:
        l2 = l.copy()
        l2.remove(i)
        out.append(l2)
    return out

tot_safe_ct = 0
tot_problem_damper = 0
for report in reports:
    report = report.split(' ')
    report = list(map(int, report))
    if report:
        if calculate_safe(report):
            tot_safe_ct += 1
            print('Safe', report)
        else:
            problem_damper = remove_one_lists(report)
            print(report, color='r')
            for sub_report in problem_damper:
                print(sub_report, color='g')
                if calculate_safe(sub_report):
                    tot_problem_damper += 1
                    break
            print('Damper:',report)

print('Safe:', tot_safe_ct)
print('Damper:', tot_problem_damper)
print('Tot:', tot_safe_ct+tot_problem_damper)


