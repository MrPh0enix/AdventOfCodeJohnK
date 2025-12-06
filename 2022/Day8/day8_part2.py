
with open('day8.txt', 'r') as txt:
    data = txt.read()

data = data.split('\n')
grid = []
for line in data:
    line = list(line)
    row = [int(x) for x in line]
    grid.append(row)



def checkScore(currTree, trees):
    score = 0

    for i in trees:

        if i >= currTree:

            score += 1
            return score
        
        if i < currTree:

            score += 1
    
    return score

maxTot = 0

for y, row in enumerate(grid):

    for x, tree in enumerate(row):

        if x == 0  or x == len(grid[0]) - 1 or y == 0 or y == len(grid) - 1:
            continue

        # right
        treesToCheck = grid[y][x+1:]
        score1 = checkScore(tree, treesToCheck)
        
        
        # left
        treesToCheck = grid[y][:x][::-1]
        score2 = checkScore(tree, treesToCheck)
        
        # up
        treesToCheck = [item[x] for item in grid[:y]][::-1]
        score3 = checkScore(tree, treesToCheck)

        # down
        treesToCheck = [item[x] for item in grid[y+1: ]]
        score4 = checkScore(tree, treesToCheck)

        tot = score1 * score2 * score3 * score4

        if tot > maxTot:

            maxTot = tot
            

    
print(maxTot)




        
        


    
