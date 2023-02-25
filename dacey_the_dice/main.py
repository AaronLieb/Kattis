# 1 on top, 2 on right
# must stand on magnet with 5 on bottom
# bfs with visited set only if number is the same

def dice_state(ids, dx, dy):
    # (top, right, bottom, left, front, back)
    # ( 0    1        2      3      4     5 )
    if dx == -1:
        return (ids[1], ids[2], ids[3], ids[0], ids[4], ids[5])
    if dx == 1:
        return (ids[3], ids[0], ids[1], ids[2], ids[4], ids[5])
    if dy == -1:
        return (ids[4], ids[1], ids[5], ids[3], ids[2], ids[0])
    if dy == 1:
        return (ids[5], ids[1], ids[4], ids[3], ids[0], ids[2])

def solve(n, grid):
    ipos = ()
    for i in range(n):
        for j in range(n):
            if grid[j][i] == "S":
                ipos = (i, j)
    starting_state = (1, 2, 6, 5, 3, 4)
    #print("starting_state", starting_state)
    Q = []
    Q.insert(0, (ipos, starting_state))
    visited = set()
    while len(Q) > 0:
        curr = Q.pop()
        if curr in visited:
            continue
        pos = curr[0]
        state = curr[1]
        visited.add(curr)
        # bounds checking
        if pos[0] >= n or pos[0] < 0:
            continue
        if pos[1] >= n or pos[1] < 0:
            continue
        spot = grid[pos[1]][pos[0]]
        # wall
        if spot == "*":
            continue
        #print(pos, state, spot)
        if spot == "H" and state[2] == 5:
            print("Yes")
            return
        Q.insert(0, ((pos[0] - 1, pos[1]), dice_state(state, -1, 0)))
        Q.insert(0, ((pos[0] + 1, pos[1]), dice_state(state, 1, 0)))
        Q.insert(0, ((pos[0], pos[1] - 1), dice_state(state, 0, -1)))
        Q.insert(0, ((pos[0], pos[1] + 1), dice_state(state, 0, 1)))
    print("No")


test_cases = int(input())
for t in range(test_cases):
    grid = []
    n = int(input())
    for i in range(n):
        grid.append(input())
    #print("Starting", t)
    solve(n, grid)

