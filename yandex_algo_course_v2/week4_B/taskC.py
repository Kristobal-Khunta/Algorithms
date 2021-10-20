# Дан текст. Выведите все слова, встречающиеся в тексте, по одному на каждую строку.
# Слова должны быть отсортированы по убыванию их количества появления в тексте,
# а при одинаковой частоте появления — в лексикографическом порядке. Указание.
# После того, как вы создадите словарь всех слов,
# вам захочется отсортировать его по частоте встречаемости слова.
# Желаемого можно добиться, если создать список,
# элементами которого будут кортежи из двух элементов:
# частота встречаемости слова и само слово.
# Например, [(2, 'hi'), (1, 'what'), (3, 'is')].
# Тогда стандартная сортировка будет сортировать список кортежей,
# при этом кортежи сравниваются по первому элементу,
# а если они равны — то по второму. Это почти то, что требуется в задаче.


from collections import Counter
from typing import IO

file_object: IO[str] = open("yandex_algo_course_v2/week4_B/inputC.txt")
counter: Counter[str, int] = Counter()

while True:
    line = file_object.readline().strip()
    if len(line) == 0:
        break
    words = line.split()
    counter.update(words)


sorted_counter_tuples = sorted(counter.items(), key=lambda x: x[0], reverse=False)
sorted_counter_tuples = sorted(sorted_counter_tuples, key=lambda x: x[1], reverse=True)
for key, val in v2:
    print(key)
