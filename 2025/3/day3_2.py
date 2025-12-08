with open('day3.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

tot = 0

for bank in input:

    select = ""
    highest = 0
    highestIdx = 0

    itr = 11

    while (itr >= 0):

        if itr == 0:
            iterable = bank[:]
        else:
            iterable = bank[:-itr]

        for idx, num in enumerate(iterable):

            if int(num) > highest:

                highest = int(num)
                highestIdx = idx
            
        select += str(highest)
        bank = bank[highestIdx+1:]
        highest = 0


        itr -= 1
    
    tot += int(select)

print(tot)

    



