# Дан список, заполненный произвольными целыми числами. Найдите в этом списке два числа,
#  произведение которых максимально. Выведите эти числа в порядке неубывания.

# Список содержит не менее двух элементов. Числа подобраны так, что ответ однозначен.

# Решение должно иметь сложность O(n), где n - размер списка.



inputs = list(map(int, input().split()))


def check_max_1_2_3(current, max1, max2, max3):
    if current > max1:
        max3 = max2
        max2 = max1
        max1 = current
    elif current > max2:
        max3 = max2
        max2 = current
    elif current > max3:
        max3 = current
    return max1, max2, max3


def check_min_1_2_3(current, min1, min2, min3):
    if current < min1:
        min3 = min2
        min2 = min1
        min1 = current
    elif current < min2:
        min3 = min2
        min2 = current
    elif current < min3:
        min3 = current
    return min1, min2, min3


subarray = inputs[:3]

max1, max2, max3 = sorted(subarray, reverse=True)
min1, min2, min3 = sorted(subarray)

for i in range(3, len(inputs)):
    current = inputs[i]
    min1, min2, min3 = check_min_1_2_3(current, min1, min2, min3)
    max1, max2, max3 = check_max_1_2_3(current, max1, max2, max3)
# varianst: min1,min2,max1/max1,max2,max3

if min1 * min2 * max1 > max1 * max2 * max3:
    print(min1, min2, max1)
else:
    print(max3, max2, max1)
