

with open('day7.txt', 'r') as txt:
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


tot_space_oc = file_sizes['origin/']

remaining_spc = 70000000 - tot_space_oc

space_needed = 30000000 - remaining_spc

min_dir_space = 1000000000000000

for val in file_sizes.values():

    if val >= space_needed and val < min_dir_space:

        min_dir_space = val


print(min_dir_space)






        
    

