with open('Day4/input.txt') as f:
    data = f.read()
XMAS_count = 0
d = []  # d is the data as a matrix
for i in data.split('\n'):
    if i:
        d.append(list(i))
LEN = len(d)    
print('LEN:', LEN)

for row in range(len(d)):
    for col in range(len(d[row])):
        # print(row,col)
        if d[row][col] == 'A':
            if col-1>=0 and row-1>=0 and col+1<LEN and row+1<LEN:
                if d[row-1][col-1] == 'M' and d[row+1][col-1] == 'M' and d[row-1][col+1] == 'S' and d[row+1][col+1] == 'S':
                    XMAS_count += 1
                    print(row, col)

                if d[row-1][col-1] == 'M' and d[row+1][col-1] == 'S' and d[row-1][col+1] == 'M' and d[row+1][col+1] == 'S':
                    XMAS_count += 1
                    print(row, col)

                if d[row-1][col-1] == 'S' and d[row+1][col-1] == 'S' and d[row-1][col+1] == 'M' and d[row+1][col+1] == 'M':
                    XMAS_count += 1
                    print(row, col)

                if d[row-1][col-1] == 'S' and d[row+1][col-1] == 'M' and d[row-1][col+1] == 'S' and d[row+1][col+1] == 'M':
                    XMAS_count += 1
                    print(row, col)
           

print(XMAS_count)

