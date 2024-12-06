from print_color import print

with open('input.txt', 'r') as f:
    data = f.read()

data1, data2 = data.split('\n\n')
data1 = data1.split('\n')
# print(data1)
hmap = {}
for r in data1:
    k, v = r.split('|')
    hmap[int(v)] = int(k) # reversed order

print(hmap)

data2 = data2.split('\n')
# print(data2)
ct = 0
for r in data2:
    is_correct = True
    if r:
        row = r.split(',')
        row = list(map(int, row))
        # print(row)
        for i in range(len(row)):
            print(row, color='g')
            if row[i] in hmap:
                print(row[i])
                if not (hmap[row[i]] in row[:i]):
                    print(row[i])
                    print(row[:i])
                    print('here')
                    is_correct = False
                    break
    break
    if is_correct:
        ct += 1
        print(row, color='r')

print(ct)
