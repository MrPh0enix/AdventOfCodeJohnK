
visited = set()

head = (0,0)
tail = (0,0)

visited.add(tail)


with open('day9.txt', 'r') as txt:
    data = txt.read().split('\n')

for inst in data:

    dir = inst.split(' ')[0]
    steps = int(inst.split(' ')[1])

    for i in range(steps):
        if dir == 'U':
            head = (head[0], head[1]+1)
        elif dir == 'D':
            head = (head[0], head[1]-1)
        elif dir == 'L':
            head = (head[0]-1, head[1])
        elif dir == 'R':
            head = (head[0]+1, head[1])
        
        if head[0] - tail[0] == 2:
            if head[1] - tail[1] == 0:
                tail = (tail[0] + 1, tail[1])
            elif head[1] - tail[1] == 1:
                tail = (tail[0] + 1, tail[1] + 1)
            elif head[1] - tail[1] == -1:
                tail = (tail[0] + 1, tail[1] - 1)
        
        elif head[0] - tail[0] == 1:
            if head[1] - tail[1] == 2:
                tail = (tail[0] + 1, tail[1] + 1)
            elif head[1] - tail[1] == -2:
                tail = (tail[0] + 1, tail[1] - 1)
        
        elif head[0] - tail[0] == 0:
            if head[1] - tail[1] == 2:
                tail = (tail[0], tail[1] + 1)
            elif head[1] - tail[1] == -2:
                tail = (tail[0], tail[1] - 1)

        elif head[0] - tail[0] == -1:
            if head[1] - tail[1] == 2:
                tail = (tail[0] - 1, tail[1] + 1)
            elif head[1] - tail[1] == -2:
                tail = (tail[0] - 1, tail[1] - 1)
        
        elif head[0] - tail[0] == -2:
            if head[1] - tail[1] == 1:
                tail = (tail[0] - 1, tail[1] + 1)
            elif head[1] - tail[1] == 0:
                tail = (tail[0] - 1, tail[1]) 
            elif head[1] - tail[1] == -1:
                tail = (tail[0] - 1, tail[1] - 1)


        visited.add(tail)   

print(len(visited))