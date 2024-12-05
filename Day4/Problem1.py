with open('Day4/input.txt') as f:
    data = f.read()
LEN = 140
XMAS_count = 0
d = []  # d is the data as a matrix

def look_forward(row, col):
    if col+3<LEN:
        if d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            return 1
    return 0

def look_backward(row, col):
    if col-3>0:
        if d[row][col] +d[row][col-1] +d[row][col-2] +d[row][col-3] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            return 1
    return 0

def look_down(row, col):
    if row+3<LEN:
        if d[row][col] +d[row+1][col] +d[row+2][col] +d[row+3][col] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            return 1
    return 0

def look_up(row, col):
    if row-3>0:
        if d[row][col] +d[row-1][col] +d[row-2][col] +d[row-3][col] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            return 1
    return 0










for i in data.split('\n'):
    if i:
        d.append(list(i))
# print(len(d), len(d[0])) # 140 140

for row in range(len(d)):
    for col in range(len(d[row])):
        # print(row,col)
        if d[row][col] == 'X':
            # print('X')
            XMAS_count += look_forward(row, col)
            XMAS_count += look_backward(row, col)
            XMAS_count += look_up(row, col)
            XMAS_count += look_down(row, col)

print(XMAS_count)

