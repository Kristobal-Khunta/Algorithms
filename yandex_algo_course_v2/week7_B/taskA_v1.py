# На числовой прямой окрасили N отрезков. Известны координаты левого и правого концов каждого отрезка (Li и Ri).
#  Найти длину окрашенной части числовой прямой.
# Формат ввода

# В первой строке находится число N, в следующих N строках - пары Li и Ri.
# Li и Ri - целые, -109 ≤ Li ≤ Ri ≤ 109, 1 ≤ N ≤ 15 000
# Формат вывода

# Вывести одно число - длину окрашенной части прямой.
# /----/      /---/
#    /----/
# Решение:
# Если приходим в очередной эвент с ненулевым счетчиком, прибавляем к оси расстояние текущее положение - предыдущее
# Ведем счетчик


def collect_events() -> list:
    N: int = int(input())
    events: list[tuple(int, int)] = [
        None
    ] * N  # - мы знаем кол-во элементов и можем создать массив заранее
    for i in range(N):
        event = tuple(map(int, input().split()))
        events[i] = event
    return events


def filled_line(events: list) -> int:
    start_val: int = -1  # сортировать будем по возрастанию, cначала закрашиваем
    end_val: int = 1
    data: list[tuple(int, int)] = []
    counter: int = 0
    filled_sum: int = 0
    for t_start, t_end in events:
        data.append((t_start, start_val))
        data.append((t_end, end_val))
    data.sort()
    for i in range(len(data)):
        t_cur, val_event = data[i]
        if counter > 0:
            t_prev, _ = data[i - 1]
            filled_sum += t_cur - t_prev
        if val_event == start_val:
            counter += 1
        else:
            counter -= 1
    return filled_sum


assert filled_line([(10, 20), (20, 40)]) == 30
assert filled_line([(5, 10), (7, 13)]) == 8


def main() -> None:
    events = collect_events()
    filled_sum = filled_line(events)
    print(filled_sum)


if __name__ == "__main__":

    main()
