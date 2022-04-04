# C. Минимальное покрытие


def collect_input() -> tuple:
    M = int(input())
    seq = []
    while True:
        left, right = list(map(int, input().split()))
        if left == 0 and right == 0:
            break
        if left < M and right > 0:
            seq.append((left, right))
    return M, seq


def main() -> None:
    M, seqs = collect_input()
    seqs.sort()  # sort by left
    rightnow: int = 0  # левая граница отрезков не должна заходить за это значение
    rightnext: int = 0  # насколько далеко
    nowbest: tuple = 0, 0  # отрезок- лучший кандидат чтобы попасть в ответ
    ans: list = []
    for left, right in seqs:
        # Выбираем кандидата в ответ, если левая граница правее нашего барьера и образуется дырка
        if left > rightnow:
            ans.append(nowbest)
            rightnow = rightnext  # перемещаю правую границу
            if rightnow >= M:
                break
        if left <= rightnow and right >= rightnext:
            # левая граница лежит внутри уже покрытого отрезка
            rightnext = right
            nowbest = left, right
    # проверим может еще добавить один отрезок, так как не весь интервал [0, M ] покрыт
    if rightnow < M:
        rightnow = rightnext
        ans.append(nowbest)

    if rightnow < M:
        print("No solution")
    else:
        print(len(ans))
        for seq in ans:
            print(*seq)


if __name__ == "__main__":
    main()
