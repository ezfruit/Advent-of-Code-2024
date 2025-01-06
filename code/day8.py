with open("../inputs/day8_input.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

frequencies = dict()

#Generate a dictionary of frequency locations
for i in range(n):
    for j in range(m):
        char = lines[i][j]
        if char != '.' and char not in frequencies:
            frequencies[char] = []
            frequencies[char].append((i, j))
        elif char != '.':
            frequencies[char].append((i, j))

#Find the two antinodes given two points (does not check bounds)

def find_antinodes(x, y):
    a, b = x
    c, d = y
    new_coord_1 = (b, -a)
    new_coord_2 = (d, -c)
    rise = new_coord_2[1] - new_coord_1[1]
    run = new_coord_2[0] - new_coord_1[0]
    antinode_1 = (new_coord_1[0] + -run, new_coord_1[1] + -rise)
    antinode_2 = (new_coord_2[0] + run, new_coord_2[1] + rise)
    new_antinode_1 = (-antinode_1[1], antinode_1[0])
    new_antinode_2 = (-antinode_2[1], antinode_2[0])
    return (new_antinode_1, new_antinode_2)

count = 0
antinode_locations = []
for frequency in frequencies.keys():
    arr = frequencies[frequency]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            a, b = find_antinodes(arr[i], arr[j])
            if 0 <= a[0] < n and 0 <= a[1] < m and a not in antinode_locations:
                count += 1
                antinode_locations.append(a)
            if 0 <= b[0] < n and 0 <= b[1] < m and b not in antinode_locations:
                count += 1
                antinode_locations.append(b)

print("Unique locations: " + str(count))

antinode_locations.clear()

#Find all antinode locations including the antenna itself (checks bounds)

def find_all_antinodes(x, y):
    a, b = x
    c, d = y
    count = 0
    new_coord_1 = (b, -a)
    new_coord_2 = (d, -c)
    rise = new_coord_2[1] - new_coord_1[1]
    run = new_coord_2[0] - new_coord_1[0]
    antinode_1 = (new_coord_1[0] + -run, new_coord_1[1] + -rise)
    antinode_2 = (new_coord_2[0] + run, new_coord_2[1] + rise)
    new_antinode_1 = (-antinode_1[1], antinode_1[0])
    new_antinode_2 = (-antinode_2[1], antinode_2[0])
    if x not in antinode_locations:
        antinode_locations.append(x)
        count += 1
    if y not in antinode_locations:
        antinode_locations.append(y)
        count += 1
    while 0 <= new_antinode_1[0] < n and 0 <= new_antinode_1[1] < m:
        if new_antinode_1 not in antinode_locations:
            antinode_locations.append(new_antinode_1)
            count += 1
        new_coord_1 = (new_antinode_1[1], -new_antinode_1[0])
        antinode_1 = (new_coord_1[0] + -run, new_coord_1[1] + -rise)
        new_antinode_1 = (-antinode_1[1], antinode_1[0])
    while 0 <= new_antinode_2[0] < n and 0 <= new_antinode_2[1] < m:
        if new_antinode_2 not in antinode_locations:
            antinode_locations.append(new_antinode_2)
            count += 1
        new_coord_2 = (new_antinode_2[1], -new_antinode_2[0])
        antinode_2 = (new_coord_2[0] + run, new_coord_2[1] + rise)
        new_antinode_2 = (-antinode_2[1], antinode_2[0])
    return count

new_count = 0
for frequency in frequencies.keys():
    arr = frequencies[frequency]
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            new_count += find_all_antinodes(arr[i], arr[j])
            
print("Updated unique locations: " + str(new_count))