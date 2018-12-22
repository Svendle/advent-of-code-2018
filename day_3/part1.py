
matrix = [[0] * 1000 for x in range(1000)]
data = (tuple(int(x) for x in line.split(',')) for line in open('input.txt'))

for dp in data:
    _, x_off, y_off, width, height = dp
    
    for row in matrix[y_off:y_off + height]:
        row[x_off:x_off + width] = [x + 1 for x in row[x_off:x_off + width]]


count = sum(sum(x > 1 for x in row) for row in matrix)
print(count)