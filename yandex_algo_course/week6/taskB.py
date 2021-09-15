# Для каждого из чисел второй последовательности найдите ближайшее к нему в первой.
# Формат ввода

# В первой строке входных данных содержатся числа N и K ().
# Во второй строке задаются N чисел первого массива,
# отсортированного по неубыванию,
# а в третьей строке – K чисел второго массива.
# Каждое число в обоих массивах по модулю не превосходит 2⋅109.
# Формат вывода

# Для каждого из K чисел выведите в отдельную строку число из первого массива,
# наиболее близкое к данному.
# Если таких несколько, выведите меньшее из них.


def check_less(m, min_diff, seq, value):
    current_diff = abs(seq[m] - value)
    return current_diff < min_diff  # and (seq[m]<value)


def binsearch_2vals(seq, value):

    left = 0
    right = len(seq) - 1
    while left < right:
        mid = (left + right) // 2
        if seq[mid] > value:
            right = mid
        else:
            left = mid + 1
    near_val_1 = seq[left - 1]
    near_val_2 = seq[left]

    if abs(near_val_1 - value) <= abs(near_val_2 - value):
        return near_val_1
    else:
        return near_val_2


if __name__ == "__main__":
    n, k = map(int, input().split())
    seq1 = list(map(int, input().split()))
    seq2 = list(map(int, input().split()))
    for k in seq2:
        # m = binsearchl(0, len(seq1) - 1, value_equal_k, seq1, k)
        m = binsearch_2vals(seq1, k)
        print(m)
