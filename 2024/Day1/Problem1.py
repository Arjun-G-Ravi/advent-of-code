with open('Day1/input1.txt') as f:
    data = f.read().split('\n')
l1, l2 =[], []
for i in data:
    l = i.split('   ')
    # print(l)
    l1.append(int(l[0]))
    l2.append(int(l[1]))
l1.sort()
l2.sort()
d = 0

for i, j in zip(l1, l2):
    d += abs(i-j)
print(d)