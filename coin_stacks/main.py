input()
stacks = [[int(x), i] for i, x in enumerate(input().split())]
num_stacks = 0
total = 0
for stack in stacks:
    if (stack[0] > 0):
        num_stacks += 1
    total += stack[0]
evens = 0
odds = 0
moves = []

def sort_func(x):
    return x[0]

if total % 2 == 1:
    print("no")
    exit()

while total >= 0:
    if num_stacks == 1:
        break
    if num_stacks == 0:
        print("yes")
        for move in moves:
            print(move[0] + 1, move[1] + 1)
        exit()

    stacks = sorted(stacks, key=sort_func, reverse=True)
    stacks[0][0] -= 1
    stacks[1][0] -= 1
    if (stacks[0][0] == 0):
        num_stacks -= 1
    if (stacks[1][0] == 0):
        num_stacks -= 1
    moves.append((stacks[0][1], stacks[1][1]))
    total -= 2

print("no")
exit()

