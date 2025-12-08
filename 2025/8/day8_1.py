import math
import heapq

with open('day8.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')
points = []
for i in input:
    x, y, z = i.split(',')
    points.append((int(x), int(y), int(z)))



def dist(p, q):
    return math.sqrt((p[0] - q[0])**2 + (p[1] - q[1])**2 + (p[2] - q[2])**2)


n = len(points)
heap = []

for i in range(n):
    for j in range(i+1, n):
        d = dist(points[i], points[j])
        heapq.heappush(heap, (d, i, j))

result = []
for i in range(1000):
    d, i, j = heapq.heappop(heap)
    for 



