with open("../inputs/day14_input.txt") as file:
    lines = file.read().strip().split("\n")

#Part 1 & Part 2

import re

HEIGHT = 103
WIDTH = 101

#Set TIME to 100 for part 1, this was to find part 2
TIME = 10000

space = [[0] * WIDTH for _ in range(HEIGHT)]

arr = [None] * (len(lines))

for i, line in enumerate(lines):
    pos, vel = line.split(" ")
    position, velocity = tuple(map(int, re.findall(r"\d+", pos))), tuple(map(int, re.findall(r"-?\d+", vel)))
    arr[i] = (position, velocity)
    x, y = position[0], position[1]
    space[y][x] += 1
        
#The idea to find the Christmas Tree is to find the frame/time period where there is the longest consecutive sequence of robots in a row

longest = []
for i in range(TIME):
    for k, robot in enumerate(arr):
        curPoint = robot[0]
        x, y = curPoint[0], curPoint[1]
        space[y][x] -= 1
        velocity = robot[1]
        newPoint = ((curPoint[0] + velocity[0]) % WIDTH, (curPoint[1] + velocity[1]) % HEIGHT)
        x, y = newPoint[0], newPoint[1]
        space[y][x] += 1
        arr[k] = (newPoint, velocity)
    curLongest = 0
    longestConsecutive = 0
    for a in range(HEIGHT):
        for b in range(WIDTH):
            if space[a][b] > 0:
                curLongest += 1
                if curLongest > longestConsecutive:
                    longestConsecutive = curLongest
            else:
                curLongest = 0
    longest.append(longestConsecutive)

midHeight = int(HEIGHT / 2)
midWidth = int(WIDTH / 2)

startPoints = [(0, 0), (midWidth + 1, 0), (0, midHeight + 1), (midWidth + 1, midHeight + 1)]

safetyFactor = 1
for startPoint in startPoints:
    count = 0
    for i in range(midHeight):
        for j in range(midWidth):
            count += space[startPoint[1] + i][startPoint[0] + j]
    safetyFactor *= count

print("Safety factor after " + str(TIME) + " seconds passed: " + str(safetyFactor))
print("Longest Consecutive spotted at: " + str(longest.index(max(longest)) + 1) + " seconds")
print("Longest was: " + str(max(longest)))