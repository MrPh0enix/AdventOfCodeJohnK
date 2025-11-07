

with open('test.txt', 'r') as txt:
    data = txt.read()

data = data.split('\n')[1:]

current_loc = ['origin/']

file_sizes = {}

for line in data:

    if line[0].isdigit():
        size = int(line.split(' ')[0])
        temp_loc = current_loc.copy()

        while temp_loc:
            dir = "".join(temp_loc)
            
            if dir not in file_sizes.keys():
                file_sizes[dir] = size
            else:
                file_sizes[dir] += size
            
            temp_loc.pop()

    
    elif line[0] == '$':
        cmd_comp = line.split(' ')
        if cmd_comp[1] == 'cd':

            if cmd_comp[2] == '..':
                #go back a step
                current_loc.pop()
            
            else:
                # go forward
                current_loc.append(cmd_comp[2] + '/')

total = 0
for i in file_sizes.values():
    if i <= 100000:
        total += i

print(file_sizes)

        
    

