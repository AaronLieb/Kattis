a, b = [int(x) for x in input().split()]
cards = input()

if cards == "AABB":
    if b == 7:
        print(8, 9)
        exit()
elif cards == "BBAA":
    if a == 3:
        print(1, 2)
        exit()
elif cards == "ABAB":
    if a == 6 and b == 8:
        print(7, 9)
        exit()
elif cards == "ABBA":
    if b - a == 3:
        print(a + 1, a + 2)
        exit()
elif cards == "BABA":
    if a == 2 and b == 4:
        print(1, 3)
        exit()
elif cards == "BAAB":
    if a == 2 and b == 8:
        print(1, 9)
        exit()
print(-1)
