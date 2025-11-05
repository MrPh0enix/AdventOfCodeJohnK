

with open('day1.txt', "r") as f:
    data = f.read()

lines = data.split('\n')


data = []

sum1 = 0
for idx,l in enumerate(lines):
    if l == '':
        data.append(sum1)
        sum1 = 0
    else:
        sum1 += int(l)

data.sort()
data = data[-3:]
total = sum(data)

print(total)