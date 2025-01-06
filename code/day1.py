def part1():
    column1 = list()
    column2 = list()
    total = list()
    with open("./inputs/day1_input.txt", 'r') as file:
        for line in file:
            [num, num2] = line.split()
            column1.append(int(num))
            column2.append(int(num2))
    length = len(column1)
    column1.sort()
    column2.sort()
    for i in range(0, length):
        minimum1 = column1[i]
        minimum2 = column2[i]
        total.append(abs(minimum1 - minimum2))
    return sum(total)

def part2():
    column1 = list()
    column2 = list()
    total = list()
    with open("./inputs/day1_input.txt", 'r') as file:
        for line in file:
            [num, num2] = line.split()
            column1.append(int(num))
            column2.append(int(num2))
    for num in column1:
        count = column2.count(num)
        total.append(num * count)
    return sum(total)

if __name__ == '__main__':
    print("Total distance is: " + str(part1()))
    print("Total similarlity score is: " + str(part2()))