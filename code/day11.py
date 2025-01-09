with open("../inputs/day11_input.txt") as file:
    line = file.read().strip().split(" ")

#Part 1 - Naive Solution

#Change this constant for however many blinks

BLINKS = 75

def part1():
    new_line = list(map(int, line))
    for _ in range(BLINKS):
        arr = []
        for i in range(len(new_line)):
            if int(new_line[i]) == 0:
                arr.append(1)
            elif len(str(new_line[i])) % 2 == 1:
                arr.append(new_line[i] * 2024)
            else:
                mid = int(len(str(new_line[i])) / 2)
                arr.append(int(str(new_line[i])[:mid]))
                arr.append(int(str(new_line[i])[mid:]))
        new_line = arr.copy()
    return len(new_line)

#Uncomment the next line for part 1 solution

#print("Stones total: " + str(part1()))

#--------------------------------------------

#Part 2 - DP using Memoization

new_line = list(map(int, line))

memo = {}

def rec(blinks, num, count, memo):
    key = (blinks, num)
    if key in memo:
        return memo.get(key)
    if blinks == 0:
        return 1
    if num == 0:
        num = 1
        memo[key] = rec(blinks - 1, num, count, memo) 
    elif len(str(num)) % 2 == 1:
        memo[key] = rec(blinks - 1, num * 2024, count, memo) 
    else:
        mid = int(len(str(num)) / 2)
        memo[key] = rec(blinks - 1 , int(str(num)[:mid]), count, memo) + rec(blinks - 1, int(str(num)[mid:]), count, memo) 
    return memo[key]

def part2():
    new_line = list(map(int, line))
    count = 0
    for i in range(len(new_line)):
        count += rec(BLINKS, new_line[i], 1, memo)
    return count

print("New stones total: " + str(part2()))
