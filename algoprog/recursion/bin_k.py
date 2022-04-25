def check(a):
    print(*a)

def find(i):
    if i == k:
        check(a)
        return
    a[i] = 0
    find(i + 1)
    a[i] = 1
    find(i + 1)


def find(i):
    if i == k:
        check(a)
        return
    for j in range(n):
        a[i] = j
        find(i + 1)


k = int(input())
n = int(input())

a = [None] * k
find(0)
