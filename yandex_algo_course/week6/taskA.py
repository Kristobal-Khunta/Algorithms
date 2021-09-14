# Реализуйте двоичный поиск в массиве
# Бинпоиск
# Особенности:
# 1. обе границы включительно
# 2. Слева все плохо, справа все хорошо ( ищем певрое включение элемента)


def value_equal_k(m, seq, value):
    return seq[m] >= value


def binsearchl(l, r, check_f, *args, **kwargs):

    while l < r:
        m = (l + r) // 2
        if check_f(m, *args, **kwargs):
            r = m
        else:
            l = m + 1
    return l


def binsearch_fast(l, r, seq, value):

    while l < r:
        m = (l + r) // 2
        if seq[m] >= value:
            r = m
        else:
            l = m + 1
    return l


n, k = map(int, input().split())
seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))
for k in seq2:
    # m = binsearchl(0, len(seq1) - 1, value_equal_k, seq1, k)
    m = binsearch_fast(0, len(seq1) - 1, seq1, k)
    if seq1[m] == k:
        print("YES")
    else:
        print("NO")
