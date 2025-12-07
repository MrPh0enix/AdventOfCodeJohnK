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
    print(start, end)
    if notebook[4][start] == '*':
        res = 1
        for line in [row[start:end] for row in notebook[:4]]:
            res *= int("".join(line))
        
        tot += res
    
    if notebook[4][start] == '+':
        res = 0
        for line in [row[start:end] for row in notebook[:4]]:
            res += int("".join(line))
        
        tot += res

    
print(tot)

