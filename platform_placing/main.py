import math

n, s, k = [int(x) for x in input().split()]
pegs = []
for i in range(n):
    pegs.append(int(input()))

pegs = sorted(pegs)

if len(pegs) == 1:
    print(k)
    exit(0)

for i in range(len(pegs) - 1):
    if pegs[i + 1] - pegs[i] < s:
        print(-1)
        exit(0)


left_bound = -math.inf
right_bound = math.inf
sum = 0
for left in range(len(pegs)):
    right = len(pegs) - left - 1

    if left > right:
        break
    left_inner_bound = min(pegs[left + 1] - s/2, right_bound)
    left_outer_bound = max(pegs[left] - k/2, left_bound)
    left_half_length = min(abs(pegs[left] - left_inner_bound), abs(pegs[left] - left_outer_bound))
    left_length = int(left_half_length * 2)
    sum += left_length
    left_bound = pegs[left] + left_half_length

    if left == right:
        break
    right_inner_bound = max(pegs[right - 1] + s/2, left_bound)
    right_outer_bound = min(pegs[right] + k/2, right_bound)
    right_half_length = min(abs(pegs[right] - right_inner_bound), abs(pegs[right] - right_outer_bound))
    right_length = int(right_half_length * 2)
    sum += right_length
    right_bound = pegs[right] - right_half_length

print(int(sum))





    
    

