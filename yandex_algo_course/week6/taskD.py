# Для освоения Марса требуется построить исследовательскую базу.
# База должна состоять из n одинаковых модулей,
# каждый из которых представляет собой прямоугольник.
# Каждый модуль представляет собой жилой отсек,
# который имеет форму прямоугольника размером a на b метров.
# Для повышения надежности модулей инженеры могут добавить вокруг
# каждого модуля слой дополнительной защиты.
# Толщина этого слоя должна составлять целое число метров, и
# все модули должны иметь одинаковую толщину дополнительной защиты.
# Модуль с защитой, толщина которой равна d метрам,
# будет иметь форму прямоугольника размером (a+2d)(b+2d) метров.
# Все модули должны быть расположены на заранее подготовленном
# прямоугольном поле размером wh метров.
# При этом они должны быть организованы в виде регулярной сетки:
# их стороны должны быть параллельны сторонам поля, и
# модули должны быть ориентированы одинаково.
# Требуется написать программу, которая по заданным количеству и
# размеру модулей, а также размеру поля для их размещения,
# определяет максимальную толщину слоя дополнительной защиты,
# который можно добавить к каждому модулю.
# Формат ввода

# Входной файл содержит пять разделенных пробелами целых чисел:
# n, a, b, w и h (1 ≤ n, a, b, w, h ≤ 1018). Гарантируется,
# что без дополнительной защиты все модули можно разместить
# в поселении описанным образом.
# Формат вывода

# Выходной файл должен содержать одно целое число:
# максимальную возможную толщину дополнительной защиты.
# Если дополнительную защиту установить не удастся,
# требуется вывести число 0.
def check_max_in_row(w_block, h_block, W, H, n):
    if w_block > W:
        return False
    n_rows = W // w_block

    n_cols = n // n_rows + bool(n % n_rows)
    return n_cols * h_block <= H


def check_max_in_col(w_block, h_block, W, H, n):
    if h_block > H:
        return False
    n_cols = H // h_block
    n_rows = n // n_cols + bool(n % n_cols)
    return n_rows * w_block <= W


def check_is_possible_square(d, params):
    a, b, W, H, n = params
    w_block = a + 2 * d
    h_block = b + 2 * d
    var_1 = check_max_in_row(w_block, h_block, W, H, n)
    var_2 = check_max_in_col(w_block, h_block, W, H, n)
    var_3 = check_max_in_row(h_block, w_block, W, H, n)
    var_4 = check_max_in_col(h_block, w_block, W, H, n)
    return var_1 or var_2 or var_3 or var_4


def binsearch_right_border(left, right, check, params):
    while left < right:
        mid = (left + right + 1) // 2
        if check(mid, params):
            left = mid
        else:
            right = mid - 1
    return left


n, a, b, w, h = 1, 1, 1, 1, 1
assert (
    binsearch_right_border(0, max(w, h), check_is_possible_square, (a, b, w, h, n)) == 0
)

n, a, b, w, h = 1, 1, 1, 3, 3
assert (
    binsearch_right_border(0, max(w, h), check_is_possible_square, (a, b, w, h, n)) == 1
)

n, a, b, w, h = 11, 3, 2, 21, 25
assert (
    binsearch_right_border(0, max(w, h), check_is_possible_square, (a, b, w, h, n)) == 2
)

n, a, b, w, h = 18, 1, 7, 98, 49
assert (
    binsearch_right_border(0, max(w, h), check_is_possible_square, (a, b, w, h, n)) == 5
)

if __name__ == "__main__":
    (
        n,
        a,
        b,
        w,
        h,
    ) = map(int, input().split())
    print(
        binsearch_right_border(0, max(w, h), check_is_possible_square, (a, b, w, h, n))
    )
