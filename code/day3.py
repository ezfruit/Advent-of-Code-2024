import re

#Part 1

def result():
    res = 0
    with open("../inputs/day3_input.txt") as file:
        for line in file:
            exp = r"(?:mul\((\d+),(\d+)\))"
            arr = re.findall(exp, line)
            for match in arr:
                res += int(match[0]) * int(match[1])
    return res

#Part 2

def find():
    res = 0
    with open("../inputs/day3_input.txt") as file:
        enabled = True
        for line in file:
            exp = r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))"
            arr = re.findall(exp, line)
            for match in arr:
                if match[2] == '' and enabled:
                    res += int(match[0]) * int(match[1])
                else:
                    enabled = match[2] == "do()"
    return res

if __name__ == '__main__':
    print("Result: " + str(result()))
    print("New Result: " + str(find()))