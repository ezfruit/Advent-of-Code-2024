with open("../inputs/day6_input.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

obstacles = []
starting_pos = None

for i in range(n):
    for j in range(m):
        if lines[i][j] == '#':
            obstacles.append((i, j))
        elif lines[i][j] == '^':
            starting_pos = (i, j)

direction = ["UP", "RIGHT", "DOWN", "LEFT"]

visited = [starting_pos]
idx = 0

guard_position = starting_pos
new_guard_position = starting_pos

while 0 < guard_position[0] < n-1 and 0 < guard_position[1] < m-1:
    cur = direction[idx % 4]
    row = guard_position[0]
    column = guard_position[1]
    match cur:
        case "UP":
            new_guard_position = (row - 1, column)
        case "RIGHT":
            new_guard_position = (row, column + 1)
        case "DOWN":
            new_guard_position = (row + 1, column)
        case "LEFT":
            new_guard_position = (row, column - 1)
    if new_guard_position in obstacles:
        idx += 1
        new_guard_position = guard_position
    else:
        guard_position = new_guard_position
        if guard_position not in visited:
            visited.append(guard_position)

#This part 2 takes around 15-20 mins to run

def find_loop():
    visited_with_direction = [(starting_pos, "UP")]
    cur_pos = starting_pos
    idx = 0
    while 0 < cur_pos[0] < n-1 and 0 < cur_pos[1] < m-1:
        cur = direction[idx % 4]
        row = cur_pos[0]
        column = cur_pos[1]
        match cur:
            case "UP":
                new_guard_position = (row - 1, column)
            case "RIGHT":
                new_guard_position = (row, column + 1)
            case "DOWN":
                new_guard_position = (row + 1, column)
            case "LEFT":
                new_guard_position = (row, column - 1)
        if new_guard_position in obstacles:
            idx += 1
            new_guard_position = cur_pos
        else:
            cur_pos = new_guard_position
            if (cur_pos, cur) not in visited_with_direction:
                visited_with_direction.append((cur_pos, cur))
            else:
                return True
    return False

counter = 0
for i in range(1, len(visited)):
    obstacles.append(visited[i])
    if find_loop():
        counter += 1
    obstacles.pop()

print("Total distinct positions: " + str(len(visited)))
print("Total new obstructions: " + str(counter))
