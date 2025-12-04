with open('day4.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

grid = []
for line in input:
    grid.append([x for x in line])

accessable = 0

   
for idxI, i in enumerate(grid):
    for idxJ, j in enumerate(i):
        if j == '@':
            nbrs = 0
            if idxI > 0 and grid[idxI - 1][idxJ] == '@': #UP
                nbrs += 1
            if idxI < len(grid)-1 and grid[idxI + 1][idxJ] == '@': #DOWN
                nbrs += 1
            if idxJ > 0  and grid[idxI][idxJ - 1] == '@': #LEFT
                nbrs += 1
            if idxJ < len(grid[0])-1 and grid[idxI][idxJ+1] == '@': #RIGHT
                nbrs += 1
            
            if idxI > 0 and idxJ < len(grid[0])-1 and grid[idxI - 1][idxJ+1] == '@': #UPRIGHT
                nbrs += 1
            if idxI > 0 and idxJ > 0 and grid[idxI - 1][idxJ - 1] == '@': #UPLEFT
                nbrs += 1
            if idxI < len(grid)-1 and idxJ < len(grid[0])-1 and grid[idxI + 1][idxJ + 1] == '@': #DOWNRIGHT
                nbrs += 1
            if idxI < len(grid)-1 and idxJ > 0 and grid[idxI + 1][idxJ - 1] == '@': #DOWNLEFT
                nbrs += 1

            if nbrs < 4:
                accessable += 1
            
print(accessable)