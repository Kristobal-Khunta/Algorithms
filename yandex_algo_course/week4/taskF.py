# Дана база данных о продажах некоторого интернет-магазина.
#  Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
#  где Покупатель — имя покупателя (строка без пробелов),
#   товар — название товара (строка без пробелов),
#   количество — количество приобретенных единиц товара.
#    Создайте список всех покупателей,
#    а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.

# Формат ввода
# Вводятся сведения о покупках в указанном формате.

# Формат вывода
# Выведите список всех покупателей в лексикографическом порядке,
#  после имени каждого покупателя выведите двоеточие,
#  затем выведите список названий всех приобретенных данным покупателем товаров в лексикографическом порядке,
#  после названия каждого товара выведите количество единиц товара, приобретенных данным покупателем.
#   Информация о каждом товаре выводится в отдельной строке.


def print_output(person2purchace):
    sorted_persons = sorted(person2purchace.keys())
    for person in sorted_persons:
        goods2nums = person2purchace[person]
        sorted_goods = sorted(goods2nums.keys())
        print(f"{person}:")
        for good in sorted_goods:
            print(f"{good} {goods2nums[good]}")

    return None


file_object = open("week4/file_taskF.txt")
# file_object = open("input.txt") - для отправки на yandex
def create_dict_with_defaultdict():
    from collections import defaultdict

    person2purchace = defaultdict(defaultdict)
    goods2nums = defaultdict(int)
    while True:

        line = file_object.readline()
        if len(line) == 0:
            break
        t = line.split()
        person, good, count = str(t[0]), str(t[1]), int(t[2])
        # is_person_exist = person2purchace.get(person, False)
        goods2nums = person2purchace[person]
        goods2nums[good] = +count
        person2purchace[person] = goods2nums
    return person2purchace


def create_person2purchace():
    person2purchace = {}
    goods2nums = {}
    while True:

        line = file_object.readline()
        if len(line) == 0:
            break
        t = line.split()
        person, good, count = str(t[0]), str(t[1]), int(t[2])
        is_person_exist = person2purchace.get(person, False)
        if is_person_exist:
            goods2nums = person2purchace[person]
        else:
            goods2nums = {}
        is_good_exist = goods2nums.get(good, False)
        if is_good_exist:
            goods2nums[good] += count
        else:
            goods2nums[good] = count
        person2purchace[person] = goods2nums
    return person2purchace


person2purchace = create_person2purchace()
print_output(person2purchace)

