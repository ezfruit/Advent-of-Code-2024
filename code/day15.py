with open("../inputs/day15_input.txt") as file:
    lines = file.read().strip().split("\n\n")

#Part 1

grid, moves = lines[0].split("\n"), lines[1].split("\n")
moves = "".join(moves)

for i, row in enumerate(grid):
    grid[i] = list(row)

n = len(grid)
m = len(grid[0])

walls = set()
boxes = []
player_position = None

#Make the grid
for i in range(n):
    for j in range(m):
        match grid[i][j]:
            case "#":
                walls.add((i, j))
            case "O":
                boxes.append((i, j))
            case "@":
                player_position = (i, j)

directions = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}

#Make the move sequence from the input
def move_sequence(moves, player_position):
    for move in moves:
        dir = directions.get(move)
        x, y = player_position
        newPos = (x + dir[0], y + dir[1])
        xx, yy = newPos
        if newPos not in walls and newPos not in boxes:
            grid[x][y] = "."
            player_position = newPos
            grid[xx][yy] = "@"
        elif newPos in boxes:
            boxesToMove = set()
            ptr = newPos
            while ptr in boxes:
                boxesToMove.add(ptr)
                ptr = (ptr[0] + dir[0], ptr[1] + dir[1])
                if grid[ptr[0]][ptr[1]] == "#":
                    break
            if grid[ptr[0]][ptr[1]] == ".":
                for box in boxesToMove:
                    boxes.remove(box)
                    newBoxPos = (box[0] + dir[0], box[1] + dir[1])
                    boxes.append(newBoxPos)
                    a, b = newBoxPos
                    grid[a][b] = "O"
                grid[x][y] = "."
                player_position = newPos
                grid[xx][yy] = "@"

#Find the GPS coordinates
def find_GPS_coords():
    res = 0
    for box in boxes:
        x, y = box
        res += (100 * x) + y 
    return res

#Uncomment the next 2 lines for part 1 solution

#move_sequence(moves, player_position)
#print("Sum of GPS coordinates is: " + str(find_GPS_coords()))

#Part 2

walls = set()
boxes = {}
player_position = None

new_grid = [[0] * (2 * m) for _ in range(n)]

#Make the new grid
for i in range(n):
    widthIdx = 0
    for j in range(m):
        match grid[i][j]:
            case "#":
                new_grid[i][widthIdx] = "#"
                new_grid[i][widthIdx+1] = "#"
                walls.add((i, widthIdx)), walls.add((i, widthIdx+1))
            case "O":
                new_grid[i][widthIdx] = "["
                new_grid[i][widthIdx+1] = "]"
                boxes[(i, widthIdx)], boxes[(i, widthIdx+1)] = "[", "]"
            case ".":
                new_grid[i][widthIdx] = "."
                new_grid[i][widthIdx+1] = "."
            case "@":
                new_grid[i][widthIdx] = "@"
                new_grid[i][widthIdx+1] = "."
                player_position = (i, widthIdx)
        widthIdx += 2

#Find if the boxes are moveable when moving up or down
def is_moveable(pos, dir):
    x, y = pos
    i, j = dir
    other_half = None
    match new_grid[x][y]:
        case "[":
            other_half = (x, y+1)
        case "]":
            other_half = (x, y-1)
        case "#":
            return False
        case ".":
            return True
    return is_moveable((x + i, y + j), dir) and is_moveable((other_half[0] + i, other_half[1] + j), dir)

#Get all the boxes that newed to be moved
def get_boxes(pos, dir, boxesToMove):
    x, y = pos
    i, j = dir
    other_half = None
    match new_grid[x][y]:
        case "[":
            other_half = (x, y+1)
            boxesToMove.add(pos)
            boxesToMove.add(other_half)
        case "]":
            other_half = (x, y-1)
            boxesToMove.add(pos)
            boxesToMove.add(other_half)
        case ".":
            return boxesToMove
    return get_boxes((x + i, y + j), dir, boxesToMove) | get_boxes((other_half[0] + i, other_half[1] + j), dir, boxesToMove)

#Make the move sequence from the input on the new grid
def new_move_sequence(moves, player_position):
    for move in moves:
        dir = directions.get(move)
        x, y = player_position
        newPos = (x + dir[0], y + dir[1])
        xx, yy = newPos
        if newPos not in walls and newPos not in boxes:
            new_grid[x][y] = "."
            player_position = newPos
            new_grid[xx][yy] = "@"
        elif newPos in boxes:
            ptr = newPos
            boxesToMove = set()
            if (move == "^" or move == "v") and is_moveable(ptr, dir):
                boxesToMove = get_boxes(ptr, dir, boxesToMove)
                newBoxLocations = set()
                for box in boxesToMove:
                    boxLabel = boxes[box]
                    del boxes[box]
                    newBoxPos = (box[0] + dir[0], box[1] + dir[1])
                    newBoxLocations.add(newBoxPos)
                    i, j = box
                    a, b = newBoxPos
                    if boxLabel == "[":
                        new_grid[a][b] = "["
                    else:
                        new_grid[a][b] = "]"
                    if box not in newBoxLocations:
                        new_grid[i][j] = "."
                for box in boxesToMove:
                    newBoxPos = (box[0] + dir[0], box[1] + dir[1])
                    a, b = newBoxPos
                    boxLabel = new_grid[a][b]
                    if boxLabel == "[":
                        boxes[newBoxPos] = "["
                    else:
                        boxes[newBoxPos] = "]"
                new_grid[x][y] = "."
                player_position = newPos
                new_grid[xx][yy] = "@"
            elif move == "<" or move == ">":
                while ptr in boxes:
                    boxesToMove.add(ptr)
                    ptr = (ptr[0] + dir[0], ptr[1] + dir[1])
                    if new_grid[ptr[0]][ptr[1]] == "#":
                        break
                if new_grid[ptr[0]][ptr[1]] == ".":
                    for box in boxesToMove:
                        boxLabel = boxes[box]
                        del boxes[box]
                        newBoxPos = (box[0] + dir[0], box[1] + dir[1])
                        a, b = newBoxPos
                        if boxLabel == "[":
                            new_grid[a][b] = "["
                        else:
                            new_grid[a][b] = "]"
                    for box in boxesToMove:
                        newBoxPos = (box[0] + dir[0], box[1] + dir[1])
                        a, b = newBoxPos
                        boxLabel = new_grid[a][b]
                        if boxLabel == "[":
                            boxes[newBoxPos] = "["
                        else:
                            boxes[newBoxPos] = "]"
                    new_grid[x][y] = "."
                    player_position = newPos
                    new_grid[xx][yy] = "@"

new_move_sequence(moves, player_position)

#Find the new GPS coordinates on the new grid
def find_new_GPS_coords():
    res = 0
    for box in boxes:
        x, y = box
        if new_grid[x][y] == "[":
            res += (100 * x) + y 
    return res

print("Sum of scaled-up GPS coordinates is: " + str(find_new_GPS_coords()))