

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
        if check in (check+check)[1:-1] :

            tot += start

        start += 1


print(tot)