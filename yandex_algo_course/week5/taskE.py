# заведем булеву маску, чтобы проверять,что все элементы из K присуствуют в текущем отрезке,
# если присутсвуют, значит он нас устраивает
# будем идти думя указателями по массиву.
# первый указатель указывает на 0-ой элем, правый на 1-ый, добавляем в булеву маску
# на idx позицию true, если правый указатель начинает указывать на нее.
# в случае если правый указатель указывает на то-же значение что и левый, сдвигаем левый на 1.
# действуем так, пока у правый указатель не упрется в конец массива.


def find_min_subseq(seq, K):
    """
    Двигаем правый указатель, до тех пор пока не найдем последовательность,
    в которой есть все цвета. затем будем поддерживать это условие.
    
    """
    counter = {}
    best_idx_subseq = [0, len(seq)]
    l_idx = 0
    for r_idx in range(len(seq)):
        if seq[r_idx] not in counter:
            counter[seq[r_idx]] = 0
        counter[seq[r_idx]] += 1
        if len(counter) == K:
            while l_idx < r_idx:
                if counter[seq[l_idx]] == 1:
                    break
                counter[seq[l_idx]] -= 1
                l_idx += 1
            if r_idx - l_idx < best_idx_subseq[1] - best_idx_subseq[0]:
                best_idx_subseq = [l_idx, r_idx]
    return best_idx_subseq


def find_min_subseq_modified(seq, K):
    """
    Двигаем правый указатель, до тех пор пока не найдем последовательность,
    в которой есть все цвета. затем будем поддерживать это условие.
    
    """
    counter = {}
    best_idx_subseq = [0, len(seq)]
    l_idx = 0
    for r_idx in range(len(seq)):
        if seq[r_idx] not in counter:
            counter[seq[r_idx]] = 0
        counter[seq[r_idx]] += 1
        if len(counter) == K:
            while counter[seq[l_idx]] > 1:
                counter[seq[l_idx]] -= 1
                l_idx += 1
            if r_idx - l_idx < best_idx_subseq[1] - best_idx_subseq[0]:
                best_idx_subseq = [l_idx, r_idx]
    return best_idx_subseq


assert find_min_subseq([5, 1, 1, 2, 2, 4, 4, 4, 3, 2, 1, 5], 5) == [7, 11]
assert find_min_subseq([1, 2, 3, 2, 2, 1, 4, 2, 2, 2, 2, 2, 3, 4, 1], 4) == [11, 14]
assert find_min_subseq([1], 1) == [0, 0]
if __name__ == "__main__":
    N, K = map(int, input().split())
    seq = list(map(int, input().split()))
    l, r = find_min_subseq(seq, K)
    print(l + 1, r + 1)

