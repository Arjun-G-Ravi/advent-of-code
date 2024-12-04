import re
from print_color import print
with open('Day3/input.txt') as f:
    data = f.read()

# Define the pattern
pattern = r'(mul\(\d{1,3},\s?\d{1,3}\)|do\(\)|don\'t\(\))'

matches = re.findall(pattern, data)
print(matches)
tot = 0
enabled = True
for i in matches:
    if i =='do()':
        enabled = True
        continue
    elif i == "don't()":
        enabled = False
        continue
    if enabled:
        match = i[4:-1].split(',')
        tot += int(match[0]) * int(match[1])
print(tot)