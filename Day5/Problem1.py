from print_color import print

with open('Day5/input2.txt', 'r') as f:
    data = f.read()

data1, data2 = data.split('\n\n')
data1 = data1.split('\n')
print(data1)
hmap = {}
for r in data1:
    k, v = r.split('|')
    if int(v) not in hmap:
        hmap[int(v)] = [int(k)] # reversed order
    else:
        hmap[int(v)].append(int(k))

print(hmap, color='b')

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
            print('Element:', row[i], color='g')
            if row[i] in hmap and max([hmap[row[i]][j] in row for j in range(len(hmap[row[i]]))]):
                print(row[i])
                # print(list(hmap[row[i]][j] in row[:i] for j in range(len(hmap[row[i]]))))
                # if not max(hmap[row[i]][j] in row[:i] for j in range(len(hmap[row[i]]))): pass
                for j in range(len(hmap[row[i]])):
                    print(j)
                    if hmap[row[i]][j] in row[:i]:
                        print('cow', color='r')
                        print(row, color='r')
                
                        # print(row[i])
                        # print(row[:i])
                        # print('here')
                        is_correct = False
                        break
            if is_correct == False:
                break

    
    if is_correct:
        print(row, 'is correct', color='purple')
        ct += 1
        print(row, color='r')

print(ct)

{53: [47, 75, 61, 97], 13: [97, 61, 29, 47, 75, 53], 61: [97, 47, 75], 47: [97, 75], 29: [75, 97, 53, 61, 47], 75: [97]}