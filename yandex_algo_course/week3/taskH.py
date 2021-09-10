N = int(input())

result = set()
n = 0
while n != N:
    t = tuple(map(int, input().split()))
    x = t[0]
    result.add(x)
    n += 1
print(len(result))
