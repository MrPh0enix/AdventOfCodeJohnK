with open('day5.txt', 'r') as file:
    input = file.read()
    ranges, ids  = input.split('\n\n')

ids = [int(x) for x in ids.split('\n')]

ranges2 = ranges.split('\n')
ranges = []
for range in ranges2:
    start, end = range.split('-')
    ranges.append((int(start), int(end)))

fresh = 0
  
for id in ids:
    for range in ranges:
        if id >= range[0] and id <= range[1]:
            fresh += 1
            break
            
print(fresh)