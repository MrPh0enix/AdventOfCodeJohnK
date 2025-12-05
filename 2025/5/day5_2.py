with open('day5.txt', 'r') as file:
    input = file.read()
    rngs, ids  = input.split('\n\n')


rng2 = rngs.split('\n')
rngs = []
for rng in rng2:
    start, end = rng.split('-')
    rngs.append((int(start), int(end)))

rngs = sorted(rngs, key= lambda x: x[0])

merged = []

for start, end in rngs:
    
    if not merged or start > merged[-1][1]:
        
        merged.append([start, end])
    
    else:
        
        merged[-1][1] = max(merged[-1][1], end)
        
tot = sum(end - start + 1 for start, end in merged)

print(tot)

  
