with open('day6.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

notebook = []

for line in input:
    notebook.append(list(line))


start = 0
end = 0
slices = []
for idx, c in enumerate(notebook[4]):
    if c != ' ':
        end = idx - 1
        slices.append((start, end))
        start = idx
slices.append((start, len(notebook[4])))

slices = slices[1:]

tot = 0

for start, end in slices:
    numList = []
    
    if notebook[4][start] == '*':
        res = 1
        
        for i in range(end-1, start-1, -1):
            num = ''
            
            for line in notebook[:4]:
                num += line[i]
            
            res *= int(num)
        
        tot += res
        
    
    if notebook[4][start] == '+':
        res = 0

        for i in range(end-1, start-1, -1):
            num = ''
            for line in notebook[:4]:
                num += line[i]
            
            res += int(num)
        
        tot += res

    
print(tot)

