# На региональном этапе Всероссийской олимпиады школьников по информатике в 2009 году предлагалась следующая задача.

# Всем известно, что со временем клавиатура изнашивается,и клавиши на ней начинают залипать.
# Конечно, некоторое время такую клавиатуру еще можно использовать, но для нажатий клавиш приходиться использовать большую силу.

# При изготовлении клавиатуры изначально для каждой клавиши задается количество нажатий,которое она должна выдерживать.
#  Если знать эти величины для используемой клавиатуры,то для определенной последовательности нажатых клавиш можно определить,
#  какие клавиши в процессе их использования сломаются, а какие — нет.

# Требуется написать программу, определяющую, какие клавиши сломаются в процессе заданного варианта эксплуатации клавиатуры.
# Формат ввода
# Первая строка входных данных содержит целое число n (1 ≤ n ≤ 1000) —количество клавиш на клавиатуре.
# Вторая строка содержит n целых чисел —с1, с2, … , сn, где сi (1 ≤ ci ≤ 100000) — количество нажатий,
# выдерживаемых i-ой клавишей. Третья строка содержит целое число k (1 ≤ k ≤ 100000) — общее количество нажатий клавиш,
#  и последняя строка содержит k целых чисел pj (1 ≤ pj ≤ n) — последовательность нажатых клавиш.

# Формат вывода
# Программа должна вывести n строк, содержащих информацию об исправности клавиш.
# Если i-я клавиша сломалась, то i-ая строка должна содержать слово YES,если же клавиша работоспособна — слово NO.


n = int(input())
inputs1 = list(map(int, input().split()))
k = int(input())

p = list(map(int, input().split()))

button2press = {}

for i, val in enumerate(inputs1):
    button2press[i + 1] = val

for x in p:
    button2press[x] -= 1


button_ready_list = sorted(button2press.items())
for broken in button_ready_list:
    if broken[1] < 0:
        print("YES")
    else:
        print("NO")
