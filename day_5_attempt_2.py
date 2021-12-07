import numpy as np

with open('day5_test.txt', 'r') as f:
    read_f = f.read()

lines =[i.split(' -> ') for i in  read_f.split('\n')]

tuples = []
for row in lines: 
    source = row[0].split(',')
    target = row[1].split(',')
    source_tup = tuple([int(source[0]), int(source[1])])
    target_tup = tuple([int(target[0]), int(target[1])])
    tuples.append([source_tup, target_tup])
    

horizontal_and_vertical_indices = []
diagonal_indices = []

for i, row in enumerate(tuples):
    x1 = row[0][0]
    y1 = row[0][1]
    x2 = row[1][0]
    y2 = row[1][1]
    
    if x1 == x2 or y1 == y2:
        horizontal_and_vertical_indices.append(i)
    
    elif abs(x2-x1) == abs(y2-y1):
        diagonal_indices.append(i)


grid = np.zeros(shape = (10,10), dtype=int)

for index in horizontal_and_vertical_indices:
    x1 = tuples[index][0][0]
    y1 = tuples[index][0][1]
    x2 = tuples[index][1][0]
    y2 = tuples[index][1][1]
    
    if x1==x2: #vertical line
        ycoords = [i for i in range(min(y1,y2),max(y1,y2)+1)]
        for y in ycoords:
            grid[x1][y] += 1
    elif y1 == y2: #horizontal line
        xcoords = [i for i in range(min(x1,x2),max(x1,x2)+1)]
        for x in xcoords:
            grid[x][y1] += 1

for index in diagonal_indices:
    x1 = tuples[index][0][0]
    y1 = tuples[index][0][1]
    x2 = tuples[index][1][0]
    y2 = tuples[index][1][1]
    
    if y2 > y1 and x2 > x1: # Upward diagonal line
        distance = y2-y1
        for i in range(distance+1):
            grid[x1+i][y1+i] += 1
            
    if y2 < y1 and x2 < x1: # Downward diagonal 
        distance = y1-y2
        for i in range(distance+1):
            grid[x1+i][y1-i] += 1