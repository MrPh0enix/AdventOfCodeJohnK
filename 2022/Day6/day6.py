
with open('day6.txt', 'r') as txt:
    data = txt.read()

idx = 0

while (idx+14 <= len(data)):

    if len(set(data[idx: idx+14])) == 14:

        print(idx+14)
        break
    
    else:

        idx += 1


print('Finished')

    