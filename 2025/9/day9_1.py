

with open('day9.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

points = []
for i in input:
    (x, y) = i.split(',')

    points.append((int(x), int(y)))

n = len(points)
maxArea = 0
for i in range(n):
    for j in range(i+1, n):
        x = abs(points[i][0] - points[j][0]) + 1
        y = abs(points[i][1] - points[j][1]) + 1
        area = x * y

        if area > maxArea:
            maxArea = area

print(maxArea)