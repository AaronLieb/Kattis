n, c = [int(x) for x in input().split()]

blocks=[]
for i in range(n):
    blocks.append([int(x) for x in input().split()])

cum_sum = 0

def recur(total_width, height):
    if len(blocks) <= 0:
        return
    if blocks[0][0] <= total_width and blocks[0][1] <= height:
        w, h = blocks.pop(0)
        recur(total_width - w, h)

while len(blocks) > 0:
    cum_sum += blocks[0][1]
    recur(c, blocks[0][1])

print(cum_sum)
    



