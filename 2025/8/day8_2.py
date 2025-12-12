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



class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False
        
        if self.size[rootX] < self.size[rootY]:
            rootX, rootY = rootY, rootX
        
        self.parent[rootY] = rootX
        self.size[rootX] += self.size[rootY]
        return True

    
    def group_size(self, x):
        return self.size[self.find(x)]




uf = UnionFind(len(points))


out = 0
for i in range(len(heap)):
    d, i, j = heapq.heappop(heap)
    
    uf.union(i, j)

    if uf.group_size(i) == len(points):
        out = points[i][0] * points[j][0]
        break

print(out)






