from collections import deque

with open('day7.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')
grid = []
for i in input:
    grid.append([x for x in i])

for idx, i in enumerate(grid[0]):
    if i == 'S':
        start = (0, idx)

tosearch = deque([start])
visited = []

splits = 0

while tosearch:
    
    (y, x) = tosearch.popleft()

    if (y, x) in visited:
        continue

    visited.append((y, x))

    if y < len(grid)-1:
        if grid[y+1][x] == '^':
            splits += 1
            tosearch.append((y+1, x-1))
            tosearch.append((y+1, x+1))
        elif grid[y+1][x] == '.':
            tosearch.append((y+1, x))

print(splits)




