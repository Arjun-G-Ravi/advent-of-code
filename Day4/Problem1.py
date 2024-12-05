with open('Day4/input2.txt') as f:
    data = f.read()
XMAS_count = 0
d = []  # d is the data as a matrix
for i in data.split('\n'):
    if i:
        d.append(list(i))
LEN = len(d)    
print('LEN:', LEN)

def look_forward(row, col):
    if col+3<LEN:
        if d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            print(row,col,'look_forward')
            return 1
    return 0

def look_backward(row, col):
    if col-3>0:
        if d[row][col] +d[row][col-1] +d[row][col-2] +d[row][col-3] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            print(row,col,'look_backward')
            return 1
    return 0

def look_down(row, col):
    if row+3<LEN:
        if d[row][col] +d[row+1][col] +d[row+2][col] +d[row+3][col] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            print(row,col,'look_down')
            return 1
    return 0

def look_up(row, col):
    if row-3>0:
        if d[row][col] +d[row-1][col] +d[row-2][col] +d[row-3][col] == 'XMAS':
            # print(d[row][col] +d[row][col+1] +d[row][col+2] +d[row][col+3])
            print(row,col,'look_up')
            return 1
    return 0

def look_right_down_diagonal(row, col):
    if row+3<LEN and col+3<LEN:
        if d[row][col] +d[row+1][col+1] +d[row+2][col+2] +d[row+3][col+3] == 'XMAS':
            print(row,col,'look_right_down_diagonal')
            return 1
    return 0

def look_right_up_diagonal(row, col):
    if row-3>0 and col+3<LEN:
        if d[row][col] +d[row-1][col+1] +d[row-2][col+2] +d[row-3][col+3] == 'XMAS':
            print(row,col,'look_right_up_diagonal')
            return 1
    return 0

def look_left_down_diagonal(row, col):
    if row+3<LEN and col-3>0:
        if d[row][col] +d[row+1][col-1] +d[row+2][col-2] +d[row+3][col-3] == 'XMAS':
            print(row,col,'look_left_down_diagonal')
            return 1
    return 0

def look_left_up_diagonal(row, col):
    if row-3>0 and col-3>0:
        if d[row][col] +d[row-1][col-1] +d[row-2][col-2] +d[row-3][col-3] == 'XMAS':
            print(row,col,'look_left_up_diagonal')
            return 1
    return 0





for row in range(len(d)):
    for col in range(len(d[row])):
        # print(row,col)
        if d[row][col] == 'X':
            # print('X')
            XMAS_count += look_forward(row, col)
            XMAS_count += look_backward(row, col)
            XMAS_count += look_up(row, col)
            XMAS_count += look_down(row, col)
            XMAS_count += look_right_down_diagonal(row, col)
            XMAS_count += look_right_up_diagonal(row, col)
            XMAS_count += look_left_down_diagonal(row, col)
            XMAS_count += look_left_up_diagonal(row, col)

print(XMAS_count)

