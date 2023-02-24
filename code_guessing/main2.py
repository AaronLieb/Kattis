a, b = [int(x) for x in input().split()]
cards = input()

potential = []
for i in range(1, 10):
    if i not in [a, b]:
        potential.append(i)

valids = []
for i in range(0, 6):
    for j in range(i + 1, 7):
        astack = [b, a]
        bstack = [j, i]
        nums = []
        acount = 0
        bcount = 0
        for x in cards:
            if x == "A":
                nums.append(astack.pop())
            if x == "B":
                nums.append(bstack.pop())
        if nums[0] < nums[1] < nums[2] < nums[3]:
            valids.append([i, j])

if len(valids) == 1:
    print(valids[0][0], valids[0][1])
else:
    print(-1)


