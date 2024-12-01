with open('Day1/input1.txt') as f:
    data = f.read().split('\n')
l1, l2 =[], []
for i in data:
    l = i.split('   ')
    # print(l)
    l1.append(int(l[0]))
    l2.append(int(l[1]))

val = 0
for i in l1:

    val += i * l2.count(i)

print(val)