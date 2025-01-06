def part1():
    count = 0
    with open("../inputs/day2_input.txt", 'r') as file:
        for line in file:
            arr = line.split()
            increasing = False
            decreasing = False
            safe = False
            for i in range(0, len(arr)-1):
                first = int(arr[i])
                num = int(arr[i+1])
                diff = num - first
                if abs(num - first) > 3:
                    safe = False
                    break
                if diff < 0:
                    decreasing = True
                elif diff > 0:
                    increasing = True
                else:
                    safe = False
                    break
                if increasing ^ decreasing:
                    safe = True
                else:
                    safe = False
                    break
            if safe:
                count += 1
    return count

def isSafe(arr):
    increasing = False
    decreasing = False
    safe = False
    for i in range(1, len(arr)):
        first = int(arr[i-1])
        num = int(arr[i])
        diff = num - first
        if abs(num - first) > 3:
            safe = False
            break
        if diff < 0:
            decreasing = True
        elif diff > 0:
            increasing = True
        else:
            safe = False
            break
        if increasing ^ decreasing:
            safe = True
        else:
            safe = False
            break
    if safe:
        return True
    return False


def part2():
    count = 0
    with open("../inputs/day2_input.txt", 'r') as file:
        for line in file:
            arr = line.split()
            for i in range(len(arr)):
                if isSafe(arr[:i] + arr[i+1:]):
                    count += 1
                    break
    return count

if __name__ == '__main__':
    print("Total reports safe: " + str(part1()))
    print("Total reports now safe: " + str(part2()))