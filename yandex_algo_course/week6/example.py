def lbinsearch(left, right, check, params):
    """
    Границы включительно: [a,b]
    Ищем первый элемент удовлетворяющий условию check
    Если условие удовлетворено, check ==True,
    то значит первый элемент удовлетворяющий словию либо этот, либо слева/
    Значит надо переместить правый указатель.
    Если же условие не выполнено, то нужный элемент не текущий и точно правее.
    """
    while left < right:
        m = (left + right) // 2
        if check(m, params):
            right = m
        else:
            left = m + 1
    return left


def right_binsearch(left, right, check, params):
    """
    Границы включительно: [a,b]
    Ищем ПОСЛЕДНИЙ элемент удовлетворяющий условию check,
    сначала все хорошоб в конце все плохо.
    Если условие удовлетворено, check ==True,
    то значит первый элемент удовлетворяющий словию либо этот, либо слева/
    Значит надо переместить правый указатель.
    Если же условие не выполнено, то нужный элемент не текущий и точно правее.
    """
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, params):
            left = mid
        else:
            right = mid - 1
    return left


# Задана отсортированная по неубыванию последовательность из N чисел и число X
# Необходимо определить сколько раз число X входит в последовательность


def check_is_greater_or_equal(index, params):
    seq, x = params
    return seq[index] >= x


def check_is_greater(index, params):
    seq, x = params
    return seq[index] > x


def find_first(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    # Если бинпоиск сошелся к числу не удовлетворяющему условию (х нет в массиве)
    # то вернем индекс длины массива
    if not check(ans, (seq, x)):
        return len(seq)
    return ans


def count_x_in_sorted(seq, x):
    """
    Найдем одним левым бинпоиском число больше либо равное х
    Другим бинпоиском число строго большее Х
    Разность индексов и будет количеством вхождений
    Отдельно надо проверить, что если в массиве [....,x,x,x,x]

    указатель для случая строго больше будет указывать на

    """
    indexgt = find_first(seq, x, check_is_greater)
    indexge = find_first(seq, x, check_is_greater_or_equal)
    return indexgt - indexge


def check_month_perc(value_from_m, value_outer):
    return value_from_m > value_outer


def check(m, params):
    pass


def fbinsearch(l, r, eps, check, checkparams):
    while l + eps < r:
        m = (l + r) / 2
        if check(m, checkparams):
            r = m
        else:
            l = m
        return l
