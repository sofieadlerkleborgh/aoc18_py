file = open ("dec03.txt", "r")

grid = [[0 for i in range(2000)] for j in range (2000)]

my_list = []


for line in file:
    temp = line.split(" ")
    output = []
    output.append(temp[0])
    position = temp[2].split(',')
    position[1] = position[1].strip(':')
    position[0] = int(position[0])
    position[1] = int(position[1])
    output.append(position)
    size = temp[3].split('x')
    size[0] = int(size[0])
    size[1] = int(size[1])
    output.append(size)
    my_list.append(output)

# adding each claim to the grid
for claim in my_list:
    for x in range (claim[1][0], (claim[1][0] + claim[2][0])):
        for y in range (claim[1][1], (claim[1][1] + claim[2][1])):
            grid[y][x] += 1

# counting squares that have been double claimed
counter = 0
for row in range(2000):
    for column in range(2000):
        if grid[row][column] > 1:
            counter += 1

# finding only claim that does not overlap
good_claim = ""
for claim in my_list:
    overlap = False
    for x in range (claim[1][0], (claim[1][0] + claim[2][0])):
        for y in range (claim[1][1], (claim[1][1] + claim[2][1])):
            if grid[y][x] > 1:
                overlap = True
    if overlap == False:
        good_claim = claim[0]


print (counter)
print (good_claim)
