with open("../inputs/day13_input.txt") as file:
    lines = file.read().strip().split("\n\n")

#Part 1 - DP using memoization

import re
import sys

def rec(a, b, cur, prize, tokens, memo):
    if cur in memo:
        return memo[cur]
    elif cur[0] == prize[0] and cur[1] == prize[1]:
        return tokens
    elif cur[0] > prize[0] or cur[1] > prize[1]:
        return sys.maxsize
    memo[cur] = min(rec(a, b, (cur[0] + a[0], cur[1] + a[1]), prize, tokens + 3, memo),
               rec(a, b, (cur[0] + b[0], cur[1] + b[1]), prize, tokens + 1, memo))
    return memo[cur]

tokensSpent = 0
for line in lines:
    a, b, prize = line.split("\n")
    a = tuple(map(int, re.findall(r"\d+", a)))
    b = tuple(map(int, re.findall(r"\d+", b)))
    prize = tuple(map(int, re.findall(r"\d+", prize)))
    tokens = rec(a, b, (0, 0), prize, 0, memo={})
    if tokens != sys.maxsize:
        tokensSpent += tokens

print("Total tokens spent: " + str(tokensSpent))

#Part 2 - System of Equations

import numpy as np

#Comment out line 46 to get part 1 answer as well

EPSILON = 0.001

tokensSpent = 0
for line in lines:
    a, b, prize = line.split("\n")
    a = tuple(map(int, re.findall(r"\d+", a)))
    b = tuple(map(int, re.findall(r"\d+", b)))
    prize = tuple(map(int, re.findall(r"\d+", prize)))
    prize = (prize[0] + 10000000000000, prize[1] + 10000000000000)
    A = np.array([[a[0], b[0]], [a[1], b[1]]])
    B = np.array([prize[0], prize[1]])
    solution = np.linalg.solve(A, B)
    x, y = solution[0], solution[1]
    x_is_int = abs(x - round(x)) <= EPSILON
    y_is_int = abs(y - round(y)) <= EPSILON
    if x_is_int and y_is_int and round(x) > 0 and round(y) > 0:
        tokensSpent += round(x) * 3 + round(y)

print("New total tokens spent: " + str(tokensSpent))