# В этой задаче Вам требуется найти максимальную по длине подстроку данной строки,
# такую что каждый символ встречается в ней не более k раз.

# Формат ввода
# В первой строке даны два целых числа n и k (1 ≤ n ≤ 100000, 1 ≤ k ≤ n ) ,
# где n – количество символов в строке. Во второй строке n символов – данная строка, состоящая только из строчных латинских букв.

# Формат вывода
# В выходной файл выведите два числа – длину искомой подстроки и номер её первого символа.
# Если решений несколько, выведите любое.


def max_subseq_k_times(seq, K):
    """
    Сейчас r_idx указывает на последний подходящий элемент последовательности.
    [l_idx,r_idx]
    Поэтому длинна последовательности = r_idx-l_idx+1.
    Если бы мы ожидали, что r_idx будет показывать на первый неподходязий элемент,
    то [l_idx,r_idx) len(subseq)  =r-Idx -l_idx
    
    """
    l_idx = 0
    r_idx = 0
    counter = {}
    best_subseq_len = -1
    best_idx = -1
    while r_idx < len(seq):
        r_val = seq[r_idx]
        if r_val not in counter:
            counter[r_val] = 0
        counter[r_val] += 1
        if r_idx - l_idx > best_subseq_len and counter[r_val] <= K:
            best_subseq_len = r_idx - l_idx
            best_idx = l_idx
        while counter[r_val] > K:
            l_val = seq[l_idx]
            counter[l_val] -= 1
            l_idx += 1
        r_idx += 1
    return best_subseq_len + 1, best_idx + 1



if __name__ == "__main__":
    n, k = map(int, input().split())
    seq = list(input())
    print(max_subseq_k_times(seq, k))
