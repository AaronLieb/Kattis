nstr = input()
size = len(nstr)
n = int(nstr)

mstr = nstr
msize = size
m = n

min_steps = None
minpstr = ""

if (size <= 1):
    print("0")
    exit()

while msize < size + 1:
    if mstr == mstr[::-1]:
        steps = 0
        diff = abs(m - n)
        diff -= diff % 10**size
        for i in reversed(range(size)):
            steps += abs(m - n) % (10**i)
            diff -= steps
        if min_steps is None or steps < min_steps:
            min_steps = steps
            print(min_steps)
    m += 1
    mstr = str(m).zfill(size)
    if (len(mstr) > size):
        msize += 1
        mstr = mstr[1:]


print(minpstr)

print(steps)

    
    
