end_time, total, num_flipped = [int(x) for x in input().split()]
flips = [int(x) for x in input().split()]
cur = 0
last_time = 0

side = "bottom"
other_side = "top"

glass = {
        "bottom": total,
        "top": 0
        }

flips.append(end_time)

for t in flips:
    diff = t - last_time
    last_time = t
    sand_lost = min(glass[other_side], diff)
    glass[side] += sand_lost
    glass[other_side] -= sand_lost
    if side == "bottom":
        other_side = "bottom"
        side = "top"
    else:
        side = "bottom"
        other_side = "top"

print(glass[side])

