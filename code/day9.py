with open("../inputs/day9_input.txt") as file:
    line = file.read().strip()

def gen_block(diskmap):
    idx = 0
    id = 0
    block = []
    for char in diskmap:
        isFree = idx % 2
        for _ in range(int(char)):
            if isFree:
                block.append(None)
            else:
                block.append(id)
        if not isFree:
            id += 1
        idx += 1
    return block

def move_block(block):
    i = 0
    j = len(block)-1
    front_ptr = block[i]
    back_ptr = block[j]
    while i != j:
        if front_ptr == None:
            while back_ptr == None:
                j -= 1
                back_ptr = block[j]
            block[i], block[j] = block[j], block[i]
            j -= 1
        i += 1
        front_ptr = block[i]
        back_ptr = block[j]
    return block

def cal_checksum(block):
    res = 0
    for k, x in enumerate(block):
        if x != None:
            res += k * x
    return res

block = gen_block(line)

# --- Uncomment the next 3 lines for part 1 solution ---

#new_block = move_block(block)
#checksum = cal_checksum(new_block)
#print("Checksum: " + str(checksum))

free_space = [0] * int(len(line) / 2)
if len(line) % 2 == 1:
    file_blocks = [0] * int(len(line) / 2 + 1)
else:
    file_blocks = [0] * int(len(line) / 2)

count = 0
for i in range(len(line)):
    if i % 2 != 0:
        free_space[count] = int(line[i])
        count += 1

count = 0
for i in range(len(line)):
    if i % 2 == 0:
        file_blocks[count] = int(line[i])
        count += 1

free_dict = {}
moved = set()

idx = 0
for i in range(len(file_blocks)-1, -1, -1):
    for j in range(len(free_space) - idx):
        if file_blocks[i] <= free_space[j]:
            free_space[j] -= file_blocks[i]
            if j not in free_dict:
                free_dict[j] = []
            free_dict[j].append(i)
            moved.add(i)
            break
    idx += 1

def new_move(block):
    i = 0
    free_space_id = 0
    ptr = block[i]
    while i < len(block):
        idx = 0
        if ptr == None:
            while ptr == None:
                arr = free_dict.get(free_space_id)
                if arr == None:
                    i += free_space[free_space_id] - 1
                    ptr = block[i]
                    break
                if idx >= len(arr):
                    i += free_space[free_space_id] - 1
                    if i >= len(block):
                        break
                    ptr = block[i]
                    break
                file_id = arr[idx]
                times = file_blocks[file_id]
                for _ in range(times):
                    block[i] = file_id
                    i += 1
                    ptr = block[i]
                idx += 1
            free_space_id += 1
        if ptr in moved:
            block[i] = None
        i += 1
        if i >= len(block):
            break
        ptr = block[i]
    return block

#Part 2 solution

new_move(block)
checksum = cal_checksum(block)
print("New Checksum: " + str(checksum))