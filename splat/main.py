PI = 3.1415926

def dist(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**(1/2)

def solve(drops, checks):
    painting = []
    for c in checks:
        items = c.split()
        x = float(items[0])
        y = float(items[1])
        painting.append([x, y, 'white'])

    for d in drops:
        items = d.split()
        x = float(items[0])
        y = float(items[1])
        v = float(items[2])
        r = (v / PI)**(1/2)
        color = items[3]
        for point in painting:
            if dist(point[0], point[1], x, y) <= r:
                point[2] = color

    for point in painting:
        print(point[2])

t = int(input())
for i in range(t):
    n = int(input())
    drops = []
    checks = []
    for i in range(n):
        drops.append(input())
    m = int(input())
    for i in range(m):
        checks.append(input())
    solve(drops, checks)
