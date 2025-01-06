with open("../inputs/day7_input.txt") as file:
    lines = file.read().strip().split("\n")

#Part 1

def rec(value, arr, result, i):
    if int(result) == int(value) and i == len(arr) - 1:
        return True
    elif i == len(arr) - 1:
        return False
    addition = rec(int(value), arr, int(result) + int(arr[i+1]), i+1)
    multiplication = rec(int(value), arr, int(result) * int(arr[i+1]), i+1)
    return addition or multiplication

total = 0
for line in lines:
    value, numbers = line.split(":")
    numbers = numbers.lstrip().split(" ")
    if rec(value, numbers, numbers[0], 0):
        total += int(value)

print("Total calibration result: " + str(total))

#Part 2

def new_rec(value, arr, result, i):
    if int(result) == int(value) and i == len(arr) - 1:
        return True
    elif i == len(arr) - 1:
        return False
    addition = new_rec(value, arr, int(result) + int(arr[i+1]), i+1)
    multiplication = new_rec(value, arr, int(result) * int(arr[i+1]), i+1)
    concatenation = new_rec(value, arr, str(result) + str(arr[i+1]), i+1)
    return addition or multiplication or concatenation

new_total = 0
for line in lines:
    value, numbers = line.split(":")
    numbers = numbers.lstrip().split(" ")
    if new_rec(value, numbers, numbers[0], 0):
        new_total += int(value)

print("New total calibration result: " + str(new_total))

#Bug found and fixed: Recursion terminates once intermediate result equals to the value and doesn't check if the full input of numbers is read
#How it was fixed: Added "and i == len(arr) - 1" in the base case