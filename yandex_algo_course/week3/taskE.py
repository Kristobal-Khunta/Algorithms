exists = set(map(int, input().split()))
vals = set([int(x) for x in input()])


diff = vals.difference(exists)
if diff:
    print(len(diff))
else:
    print(0)