with open("../inputs/day4_input.txt") as file:
    lines = file.read().strip().split("\n")

n = len(lines)
m = len(lines[0])

directions = [(-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (0, -1), (1, -1)]

def result():
    count = 0
    for i in range(n):
        for j in range(m):
            for d in directions:
                count += has_xmas(i, j, d)
    return count

def has_xmas(i, j ,d):
    dx, dy = d
    for k, x in enumerate("XMAS"):
        ii = i + k * dx
        jj = j + k * dy
        if not (0 <= ii < n and 0 <= jj < m):
            return False
        elif lines[ii][jj] != x:
            return False
    return True

new_directions = [(-1, 1), (1, 1), (-1, -1), (1, -1)]

def new_result():
    count = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            count += has_mas(i, j)
    return count

def has_mas(i, j):
    if lines[i][j] != 'A':
        return False
    diag_1 = f"{lines[i-1][j-1]}{lines[i+1][j+1]}"
    diag_2 = f"{lines[i-1][j+1]}{lines[i+1][j-1]}"
    letters = ["MS", "SM"]
    if not (diag_1 in letters and diag_2 in letters):
        return False
    return True

if __name__ == '__main__':
    print("Times XMAS appears: " + str(result()))
    print("Times X-MAS appears: " + str(new_result()))
