with open('day4.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

grid = []
for line in input:
    grid.append([x for x in line])



def check_accessable(idxI, idxJ, grid):
    
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
        return True
    else:
        return False


to_remove = [(0,0)]
tot_removed = 0

while len(to_remove) > 0:
    to_remove = []
    for idxI, i in enumerate(grid):
        for idxJ, j in enumerate(i):
            if j == '@' and check_accessable(idxI, idxJ, grid):
                
                to_remove.append((idxI, idxJ))
    
    tot_removed += len(to_remove)
    
    for (pointi, pointj) in to_remove:
        grid[pointi][pointj] = '.'
    
print(tot_removed) 
                
                    
