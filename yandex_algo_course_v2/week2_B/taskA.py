# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Всего вводится не более 10000 чисел (не считая завершающего числа 0).
#  Определите, сколько элементов этой последовательности равны ее наибольшему элементу.
# Числа, следующие за числом 0, считывать не нужно.
# Формат ввода

# Вводится последовательность целых чисел, оканчивающаяся числом 0
#  (само число 0 в последовательность не входит).
# Формат вывода

# Выведите ответ на задачу.


if __name__ == "__main__":
    count_max = 0
    max_value = -1
    while True:
        value = int(input())
        if value == 0:
            break
        if value == max_value:
            count_max += 1
        if value > max_value:
            max_value = value
            count_max = 1
    print(count_max)
