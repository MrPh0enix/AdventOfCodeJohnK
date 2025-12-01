

with open('day1.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

curNum = 50

count0 = 0

for inst in input:

    if inst[0] == 'L':
        clicks = int(inst[1:])

        for step in range(clicks):
            curNum = (curNum - 1) % 100

            if curNum == 0:
                count0 += 1

    
    elif inst[0] == 'R':
        clicks = int(inst[1:])

        for step in range(clicks):
            curNum = (curNum + 1) % 100
            
            if curNum == 0:
                count0 += 1
    

    
    

print(count0)
