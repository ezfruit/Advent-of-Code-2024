with open("../inputs/day5_input.txt") as file:
    lines = file.read().strip().split("\n")

splitter = lines.index("")
rules = lines[:splitter]
updates = lines[splitter+1:]

mappedRules = dict()

for update in updates:
    pages = update.split(",")
    for page in pages:
        left = f"{page}|"
        right = f"|{page}"
        for rule in rules:
            if left in rule or right in rule:
                if page not in mappedRules:
                    mappedRules[page] = list()
                mappedRules[page].append(rule)

def isCorrectOrder(pages):
    for i in range(0, len(pages)):
        for j in range(i+1, len(pages)):
            if f"{pages[j]}|{pages[i]}" in mappedRules.get(pages[j]):
                return False 
    return True
            
total = 0
incorrect = []
for update in updates:
    pages = update.split(",")
    if isCorrectOrder(pages):
        total += int(pages[int(len(pages)/2)])
    else:
        incorrect.append(pages)

def bubble_sort(pages):
    for i in range(len(pages)):
        for j in range(0, len(pages)-i-1):
            if f"{pages[j+1]}|{pages[j]}" in mappedRules.get(pages[j]):
                pages[j], pages[j+1] = pages[j+1], pages[j]
                swapped = True
        if not swapped:
            break
    return pages

new_total = 0
for pages in incorrect:
    new_pages = bubble_sort(pages)
    new_total += int(new_pages[int(len(new_pages)/2)])

print("Total: " + str(total))
print("New Total: " + str(new_total))