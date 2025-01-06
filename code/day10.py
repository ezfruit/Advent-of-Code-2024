with open("../inputs/day10_input.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
adj_list = {}
trailheads = set()

def make_edges(vertex):
    for dir in directions:
        x = dir[0] + vertex[0]
        y = dir[1] + vertex[1]
        if not (0 <= x < n and 0 <= y < m):
            continue
        node = (x, y)
        oldHeight = int(lines[vertex[0]][vertex[1]])
        newHeight = int(lines[x][y])
        isPath = (oldHeight + 1) == newHeight 
        if isPath:
            adj_list[vertex].append(node)

def make_graph():
    for i in range(n):
        for j in range(m):
            vertex = (i, j)
            adj_list[vertex] = []
            make_edges((i, j))
            if int(lines[i][j]) == 0:
                trailheads.add(vertex)

make_graph()

from collections import deque

def bfs(start):
    score = 0
    visited = set()
    queue = deque()
    queue.append(start)
    first = queue.popleft()
    visited.add(first)
    for neighbor in adj_list.get(first):
        queue.append(neighbor)
    while queue:
        first = queue.popleft()
        visited.add(first)
        x = first[0]
        y = first[1]
        if int(lines[x][y]) == 9:
            score += 1
        for neighbor in adj_list.get(first):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return score

scores = 0 
for trailhead in trailheads:
    scores += bfs(trailhead)

print("Total score: " + str(scores))

#Part 2 - Solution is just BFS in part 1 but without a visited set

def bfs_without_visited(start):
    score = 0
    queue = deque()
    queue.append(start)
    first = queue.popleft()
    for neighbor in adj_list.get(first):
        queue.append(neighbor)
    while queue:
        first = queue.popleft()
        x = first[0]
        y = first[1]
        if int(lines[x][y]) == 9:
            score += 1
        for neighbor in adj_list.get(first):
            queue.append(neighbor)
    return score

ratings = 0 
for trailhead in trailheads:
    ratings += bfs_without_visited(trailhead)

print("Total rating: " + str(ratings))