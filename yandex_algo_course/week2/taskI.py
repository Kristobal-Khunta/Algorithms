N, M, K = list(map(int, input().split()))

field = []
for n in range(N):
    field.append([0 for m in range(M)])


def is_correct_idx(n, m, N, M, field):
    if (n < 0) or (m < 0) or (n >= N) or (m >= M) or (field[n][m] == "*"):
        return False
    else:
        return True


def add_mine(n_mine, m_mine, field):
    field[n_mine][m_mine] = "*"
    for n in [n_mine - 1, n_mine, n_mine + 1]:
        for m in [m_mine - 1, m_mine, m_mine + 1]:
            if is_correct_idx(n, m, N, M, field):
                field[n][m] += 1
    return field


for k_i in range(K):
    n_mine, m_mine = list(map(int, input().split()))
    n_mine = n_mine - 1
    m_mine = m_mine - 1
    field = add_mine(n_mine, m_mine, field)

mod_field_str = []
for s in field:
    s_mod = [str(x) for x in s]
    mod_field_str.append(" ".join(s_mod))
result = "\n".join(mod_field_str)
print(result)
