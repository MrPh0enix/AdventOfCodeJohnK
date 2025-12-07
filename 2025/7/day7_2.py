from collections import deque
from functools import lru_cache

with open('day7.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')
grid = []
for i in input:
    grid.append([x for x in i])

for idx, i in enumerate(grid[0]):
    if i == 'S':
        start = (0, idx)


@lru_cache(None)
def dfs(point):
    
    if point[0] == len(grid)-1:
        return 1

    if point[1] < 0 or point[1] > len(grid[0])-1:
        return 0

    if grid[point[0]+1][point[1]] == '^':
        return dfs((point[0]+1, point[1]+1)) + dfs((point[0]+1, point[1]-1))
        
    elif grid[point[0]+1][point[1]] == '.':
        return dfs((point[0]+1, point[1]))

paths = dfs(start)


print(paths)




