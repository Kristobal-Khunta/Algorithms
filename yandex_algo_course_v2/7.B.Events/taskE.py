from math import pi


def main():
    n: int = int(input())
    rad1_ans = 0
    rad2_ans = 10**6
    events = []
    # Идея: Вместо индекса угла и сохранения (phi,status,idx),
    #  используем -i и + i в графе эвентов (phi, -i).
    # сортировка аналогична
    for i in range(1, n + 1):
        rad1, rad2, phi1, phi2 = list(map(float, input().split()))
        rad1_ans = max(rad1, rad1_ans)
        rad2_ans = min(rad2, rad2_ans)

        events.append((phi1, -i))
        events.append((phi2, i))
    events.sort()
    cntsegs = 0
    used = set()
    # два прохода
    for event in events:
        if event[1] < 0:  # начало нового проямоугольника
            cntsegs += 1
            used.add(-event[1])  # i-ый прямоугольник
        elif event[1] in used:  # если прямоугольник закончился и есть в множестев
            cntsegs -= 1
    # после 1-ого прохода в cntsegs кол-во начавшихся но не закончившихся прямоугольников
    ans = 0
    # второй проход
    for i in range(len(events)):
        event = events[i]
        if event[1] < 0:
            cntsegs += 1
        else:
            cntsegs -= 1
        if cntsegs == n:
            # если кол-во активных прямоугольников достигло n
            # два вариана:
            # если следующее событие существует
            if i < len(events) - 1:
                area = (
                    (events[i + 1][0] - events[i][0])
                    * (rad2_ans**2 - rad1_ans**2)
                    / 2
                )

                ans += area
            else:
                # обрабатывается в 1-й ситуации:
                # если все n- многоугольников начались но не закончились
                area = (
                    (events[0][0] - events[len(events) - 1][0] + 2 * pi)
                    * (rad2_ans**2 - rad1_ans**2)
                    / 2
                )
                ans += area
    print(ans)


if __name__ == "__main__":
    main()
