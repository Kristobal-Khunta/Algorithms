# Август и Беатриса играют в игру. Август загадал натуральное число от 1 до n.
# Беатриса пытается угадать это число,
# для этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел есть задуманное
# или NO в противном случае. После нескольких заданных вопросов
# Беатриса запуталась в том, какие вопросы она задавала и
# какие ответы получила и просит вас помочь ей определить,
# какие числа мог задумать Август.
# Формат ввода

# Первая строка входных данных содержит число n — наибольшее число,
# которое мог загадать Август. Далее идут строки, содержащие вопросы Беатрисы.
# Каждая строка представляет собой набор чисел, разделенных пробелами.
# После каждой строки с вопросом идет ответ Августа: YES или NO.
# Наконец, последняя строка входных данных содержит одно слово HELP.
# Формат вывода

# # Вы должны вывести (через пробел, в порядке возрастания) все числа,
# # которые мог задумать Август.


## Time limit error 


# n = int(input().strip())
# base_set = set(range(1, n + 1))
# positive_set = set()
# negative_set = set()
# while True:
#     inp = input()
#     if inp == "HELP":
#         break
#     cur_set = set(map(int, inp.split()))
#     cur_str = input().strip()
#     if cur_str == "YES":
#         base_set = base_set & cur_set
#     elif cur_str == "NO":
#         base_set = base_set - cur_set
#     else:
#         raise ValueError(f"cur_str must be YES or NO, get {cur_str}")
# print(*sorted(base_set))



n = int(input().strip())
base_set = set(range(1, n + 1))

while True:
    inp = input()
    if inp == "HELP":
        break
    cur_set = set(map(int, inp.split()))
    cur_str = input().strip()
    if cur_str == "YES":
        base_set = base_set & cur_set
    elif cur_str == "NO":
        base_set.difference_update(cur_set)
    else:
        raise ValueError(f"cur_str must be YES or NO, get {cur_str}")

print(*sorted(base_set))

