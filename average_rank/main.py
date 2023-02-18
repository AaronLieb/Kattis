n, w = [int(x) for x in input().split()]

cum_ranks = [0] * n
players = [0] * n


def sort_func(x):
    return x[1]

for i in range(w):
    points = [int(x)-1 for x in input().split()][1:]
    for point in points:
        players[point] += 1
    leaderboard = sorted(enumerate(players), key=sort_func, reverse=True)
    for i, l in enumerate(leaderboard):
        cum_ranks[l[0]] += i

for cum in cum_ranks:
    print(f"{(cum/w):.6f}")


        


    


