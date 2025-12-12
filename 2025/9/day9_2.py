

with open('day9.txt', 'r') as file:
    input = file.read()
    input = input.split('\n')

points = []
for i in input:
    (x, y) = i.split(',')

    points.append((int(x), int(y)))


# def check_tile(tile):
#     corners = 0
#     for point in points:
#         if (point[0] >= tile[0]) and (point[1] >= tile[1]):
#             corners += 1
#         if (point[0] <= tile[0]) and (point[1] >= tile[1]):
#             corners += 1
#         if (point[0] <= tile[0]) and (point[1] <= tile[1]):
#             corners += 1
#         if (point[0] >= tile[0]) and (point[1] <= tile[1]):
#             corners += 1
    
#     if corners == 4:
#         return True
#     else:
#         return False



# n = len(points)
# maxArea = 0
# for i in range(n):
#     for j in range(i+1, n):
#         x = abs(points[i][0] - points[j][0]) + 1
#         y = abs(points[i][1] - points[j][1]) + 1
#         area = x * y
#         if area <= maxArea:
#             continue
#         elif (area > maxArea):
#             for l in range(points[i][0], points[j][0]):
#                 for m in range(points[i][1], points[j][1]):
#                     if check_tile((l, m)):
#                         maxArea = area

# print(maxArea)


def check_corners(x1, y1, x2, y2):
    corners_found = 0
    if (x2 >= x1) and (y2 >= y1):
        for point in points:
            if (point[0] <= x1) and (point[1] >= y2):
                corners_found += 1
            if (point[0] >= x2) and (point[1] <= y1):
                corners_found += 1
    
    elif (x2 <= x1) and (y2 >= y1):
        for point in points:
            if (point[0] <= x2) and (point[1] <= y1):
                corners_found += 1
            if (point[0] >= x1) and (point[1] >= y2):
                corners_found += 1
    
    elif (x2 <= x1) and (y2 <= y1):
        for point in points:
            if (point[0] <= x2) and (point[1] >= y1):
                corners_found += 1
            if (point[0] >= x1) and (point[1] <= y2):
                corners_found += 1
    
    elif (x2 >= x1) and (y2 <= y1):
        for point in points:
            if (point[0] <= x1) and (point[1] <= y2):
                corners_found += 1
            if (point[0] >= x2) and (point[1] >= y1):
                corners_found += 1
    
    if corners_found == 2:
        return True
    else:
        return False


n = len(points)
maxArea = 0
for i in range(n):
    for j in range(i+1, n):
        x = abs(points[i][0] - points[j][0]) + 1
        y = abs(points[i][1] - points[j][1]) + 1
        area = x * y
        if area <= maxArea:
            continue
        elif (area > maxArea):
            x1, y1 = points[i][0], points[j][0]
            x2, y2 = points[i][1], points[j][1]
            if check_corners(x1, y1, x2, y2):
                maxArea = area

print(maxArea)
