
with open('day3.txt', 'r') as txt:
    data = txt.read()

data = data.split('\n')

tot = 0
groupIdx = 3

while groupIdx <= len(data):
    
    group = data[groupIdx-3: groupIdx]
    
    
    for letter in group[0]:
        if (letter in group[1]) and (letter in group[2]):
            if letter.isupper():
                tot += ord(letter) - 38
            else:
                tot += ord(letter) - 96
            break
    
    groupIdx += 3



print(tot)