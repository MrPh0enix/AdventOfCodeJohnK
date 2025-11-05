
with open('day3.txt', 'r') as txt:
    data = txt.read()

data = data.split('\n')

tot = 0

for line in data:
    mid = int(len(line)/2)
    
    left = line[:mid]
    right = line[mid:]
    
    
    for let in left:
    
        if let in right:
            if let.isupper():
                tot += ord(let) - 38
            else:
                tot += ord(let) - 96
            
            break
                
print(tot)