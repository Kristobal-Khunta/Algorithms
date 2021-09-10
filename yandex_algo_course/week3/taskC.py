M, N = list(map(int, input().split()))

M_set = set()
N_set = set()
for i in range(M):
    M_set.add(int(input()))
for i in range(N):
    N_set.add(int(input()))

inersect = sorted((N_set & M_set), reverse=False)
N_unique = sorted((N_set - M_set), reverse=False)
M_unique = sorted((M_set - N_set), reverse=False)
print(len(inersect))
print(" ".join(map(str, inersect)))
print(len(M_unique))
print(" ".join(map(str, M_unique)))
print(len(N_unique))
print(" ".join(map(str, N_unique)))
