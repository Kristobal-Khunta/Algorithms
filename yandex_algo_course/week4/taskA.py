N = int(input())
n = 0
sinonims = {}
while n != N:
    t = tuple(map(str, input().split(" ")))
    mini_dict = {t[0]: t[1], t[1]: t[0]}
    sinonims.update(mini_dict)
    n += 1

print(sinonims[str(input())])
