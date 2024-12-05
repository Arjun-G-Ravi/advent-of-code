with open('input.txt', 'r') as f:
    data = f.read()

data1, data2 = data.split('\n\n')
data1 = data1.split('\n')
# print(data1)
hmap = {}
for i in data1:
    k, v = i.split('|')
    hmap[int(k)] = int(v)

print(hmap)

data2 = data2.split('\n')
# print(data2)

for i in data2:
    if i:
        row = i.split(',')
        row = list(map(int, row))
        print(row)
        for i in row:
            pass