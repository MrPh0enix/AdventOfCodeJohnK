
with open('day8.txt', 'r') as txt:
    data = txt.read()

data = data.split('\n')
grid = []
for line in data:
    line = list(line)
    row = [int(x) for x in line]
    grid.append(row)

# # initialize to represent the edge trees
# vis_trees = (len(gird)*2) + ((len(grid[0])- 2) * 2 )

vis_trees = set()



def checkVis(currTree, trees):

    for i in trees:
        
        if i >= currTree:

            return False
    
    return True



for y, row in enumerate(grid):

    

    for x, tree in enumerate(row):

        if x == 0  or x == len(grid[0]) - 1 or y == 0 or y == len(grid) - 1:
            vis_trees.add((x, y))
            continue

        # right
        treesToCheck = grid[y][x+1:]
        if checkVis(tree, treesToCheck):
            vis_trees.add((x, y))
            continue
        
        # left
        treesToCheck = grid[y][:x]
        if checkVis(tree, treesToCheck):
            vis_trees.add((x, y))
            continue
        
        # up
        treesToCheck = [item[x] for item in grid[:y]]
        if checkVis(tree, treesToCheck):
            vis_trees.add((x, y))
            continue

        # down
        treesToCheck = [item[x] for item in grid[y+1: ]]
        if checkVis(tree, treesToCheck):
            vis_trees.add((x, y))
            continue




print(len(vis_trees))



        
        


    
