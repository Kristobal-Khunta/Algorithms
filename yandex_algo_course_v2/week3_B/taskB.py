    # Во входной строке записана последовательность чисел через пробел. 
    # Для каждого числа выведите слово YES (в отдельной строке),
    #  если это число ранее встречалось в последовательности или NO, если не встречалось.

seq = list(input().split())
set_cur = set()
for i in seq:
    if i not in set_cur:
        set_cur.add(i)
        print('NO')
    else:
        print('YES')