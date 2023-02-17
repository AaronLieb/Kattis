zooms = input()
x = 0
y = 0
offset = 0
for c in zooms:
    zoom = int(c)
    if (zoom == 1 or zoom == 3):
        x += 1
    if (zoom == 2 or zoom == 3):
        y += 1
    offset += 1
    x *= 2
    y *= 2

print(offset, int(x/2), int(y/2))

    
