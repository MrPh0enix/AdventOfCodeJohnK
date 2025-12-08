with open('day3.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

tot = 0

for bank in input:

    
    highest = 0
    

    for f_idx, first in enumerate(bank):

        for sec in bank[f_idx+1:]:

            num = int(first+sec)

            if num > highest:

                highest = num
    
    tot += highest


print(tot)



