n = int(input())
s = ''
for _ in range(n):
    a = input()
    s += '1' if a == 'Z' else '0'

start = int(s, 2)
end = int('1' * len(s), 2)
print(end - start)
