N = int(input())

result = set()
n = 0
while n != N:
    ab = tuple(map(int, input().split()))
    if (sum(ab) == (N - 1)) and (ab[0] >= 0) and (ab[1] >= 0):
        result.add(ab)
    n += 1

print(result)
print(len(result))
