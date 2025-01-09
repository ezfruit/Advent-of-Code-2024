with open("../inputs/day12_input.txt") as file:
    lines = file.read().strip().split("\n")

#Part 1

from collections import deque

n = len(lines)
m = len(lines[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
adj_list = {}

def make_edges(vertex):
    for dir in directions:
        x = dir[0] + vertex[0]
        y = dir[1] + vertex[1]
        if not (0 <= x < n and 0 <= y < m):
            continue
        node = (x, y)
        curLetter = lines[vertex[0]][vertex[1]]
        newLetter = lines[x][y]
        if curLetter == newLetter:
            adj_list[vertex].append(node)

def make_graph():
    for i in range(n):
        for j in range(m):
            vertex = (i, j)
            adj_list[vertex] = []
            make_edges((i, j))

make_graph()

visited = set()

def bfs(start):
    queue = deque()
    queue.append(start)
    first = queue.popleft()
    visited.add(first)
    area = 1
    region = [first]
    for neighbor in adj_list.get(first):
        queue.append(neighbor)
    while queue:
        first = queue.popleft()
        visited.add(first)
        area += 1
        region.append(first)
        for neighbor in adj_list.get(first):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return (area, region)

def get_perimeter(vertex):
    perimeter = 0
    for dir in directions:
        x = dir[0] + vertex[0]
        y = dir[1] + vertex[1]
        if not (0 <= x < n and 0 <= y < m):
            perimeter += 1
            continue
        curLetter = lines[vertex[0]][vertex[1]]
        newLetter = lines[x][y]
        if curLetter != newLetter:
            perimeter += 1
    return perimeter

areas = []
perimeters = {}

for i in range(n):
    for j in range(m):
        vertex = (i, j)
        perimeters[vertex] = get_perimeter(vertex)
        if vertex not in visited:
            areas.append(bfs(vertex))

price = 0
for area_tuple in areas:
    area = area_tuple[0]
    perimeter = 0
    for vertex in area_tuple[1]:
        perimeter += perimeters.get(vertex)
    price += area * perimeter

print("Total price: " + str(price))

#Part 2

directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

isCorner = [[1, 0, 0, 0],
            [1, 1, 1, 0],
            [1, 0, 0, 1]]

#Calculate the number of sides on a single point in a region
def get_sides(vertex):
    sides = 0
    for dir in directions:
        x, y = vertex[0], vertex[1]
        i, j = dir[0], dir[1]
        points = [(x, y), (x + i, y), (x, y + j), (x + i, y + j)]
        cornerArray = [0] * 4
        for i, point in enumerate(points):
            a, b = point[0], point[1]
            if 0 <= a < n and 0 <= b < m:
                cornerArray[i] = int(lines[x][y] == lines[a][b])
        sides += cornerArray in isCorner
    return sides

price = 0
for area_tuple in areas:
    area = area_tuple[0]
    sides = 0
    for vertex in area_tuple[1]:
        sides += get_sides(vertex)
    price += area * sides

print("New total price: " + str(price))