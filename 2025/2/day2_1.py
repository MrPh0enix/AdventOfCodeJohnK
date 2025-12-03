

with open('day2.txt', 'r') as file:
    input = file.read()
    input = input.split(',')


tot = 0

for rng in input:

    start, end = rng.split('-')
    start = int(start)
    end = int(end)

    while start <= end:

        check = str(start)
        if check[0:int(len(check)/2)] == check[int(len(check)/2):] :

            tot += start

        start += 1


print(tot)