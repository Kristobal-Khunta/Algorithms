# Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа,
#  произведение которых максимально. Выведите эти числа в порядке неубывания.

# Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

# Решение должно иметь сложность O(n), где n - размер списка.
inputs = list(map(int, input().split()))


def check_max_1_2(current, max1, max2):
    if current > max1:
        max2 = max1
        max1 = current
    elif current > max2:
        max2 = current
    return max1, max2


def check_min_1_2(current, min1, min2):
    if current < min1:
        min2 = min1
        min1 = current
    elif current < min2:
        min2 = current
    return min1, min2


max1 = max(inputs[0], inputs[1])
max2 = min(inputs[0], inputs[1])

min1 = min(inputs[0], inputs[1])
min2 = max(inputs[0], inputs[1])


for i in range(2, len(inputs)):
    current = inputs[i]
    min1, min2 = check_min_1_2(current, min1, min2)
    max1, max2 = check_max_1_2(current, max1, max2)

if min1 * min2 > max1 * max2:
    print(min1, min2)
else:
    print(max2, max1)

