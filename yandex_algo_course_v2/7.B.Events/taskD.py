# D. Наполненность котятами
# На прямой в точках a_i (возможно, совпадающих) сидят n котят.
# На той же прямой лежат m отрезков.
#  Нужно для каждого отрезка узнать его наполненность котятами — сколько котят сидит на отрезке.

from dataclasses import dataclass


@dataclass
class EventType:
    segment_start: int = -1
    cat_here: int = 0
    segment_end: int = 1


def collect_input() -> list:
    # TODO n, m python type hints
    n: int
    m: int
    cats: list
    n, m = list(map(int, input().split()))
    cats = list(map(int, input().split()))
    lines: list = []
    for _ in range(m):
        t_left: int
        t_right: int
        t_left, t_right = list(map(int, input().split()))
        lines.append((t_left, t_right))
    return cats, lines


def cats_in_segment(cats: list, segments: list) -> list:
    # кол-во котят на отрезке = кол-во котят в конце отрезка - кол-во в начале
    events: list = []
    event_type = EventType()
    for i, cat_time in enumerate(cats):
        events.append((cat_time, event_type.cat_here, i))
    for i, segment in enumerate(segments):
        t_in, t_out = segment
        events.append((t_in, event_type.segment_start, i))
        events.append((t_out, event_type.segment_end, i))
    events.sort()
    cats_on_start_segm = [0] * len(segments)
    result_cats_in_segm = [0] * len(segments)
    cats_counter = 0
    for event in events:
        time_event, type_event, idx = event
        match type_event:
            case event_type.cat_here:
                cats_counter += 1
            case event_type.segment_start:
                cats_on_start_segm[idx] += cats_counter
            case event_type.segment_end:
                result_cats_in_segm[idx] = cats_counter - cats_on_start_segm[idx]
    return result_cats_in_segm

assert cats_in_segment([2,2], [(0,1)]) == [0]
assert cats_in_segment([2,2], [(0,1)]) == [0]

assert cats_in_segment([2, 2, 2, 2], [(0, 1), (1, 3), (1, 4)]) == [0,4,4]


def main() -> None:
    # событие : Время, тип, индекс
    cats: list[int]
    segments: list[tuple]
    cats, segments = collect_input()
    # sort events:
    result_cats_in_segm = cats_in_segment(cats, segments)
    #print(f'{result_cats_in_segm=}')
    print(*result_cats_in_segm)


if __name__ == "__main__":
    main()
