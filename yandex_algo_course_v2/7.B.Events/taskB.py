# # Идёт 2163 год. Мишу, который работает в отделении таможни при космодроме города Нью-Питер, вызвал в кабинет шеф.
# Как оказалось, недавно Министерство Налогов и Сборов выделило отделению определённую сумму денег на установку новых аппаратов
# для автоматического досмотра грузов. Естественно, средства были выделены с таким расчётом, чтобы грузы теперь находились на
# таможне ровно столько времени, сколько требуется непосредственно на их досмотр.
# В руках шефа каким-то образом оказались сведения о надвигающейся ревизии – список из N грузов,
#  которые будут контролироваться Министерством. Для каждого груза известны время его прибытия,
#  отсчитываемое с некоторого момента, хранимого в большом секрете, и время,
# требуемое аппарату для обработки этого груза. Шеф дал Мише задание по этим данным определить,
# какое минимальное количество аппаратов необходимо заказать на заводе,
#  чтобы все грузы Министерства начинали досматриваться сразу после прибытия.
# Необходимо учесть, что конструкция тех аппаратов, которые было решено установить,
# не позволяет обрабатывать два груза одновременно на одном аппарате.
# Напишите программу, которая поможет Мише справиться с его задачей.

# Необходимо найти максимум одновременно идущих событий


def collect_events() -> list:
    N: int = int(input())
    events: list[tuple(int, int)] = [None] * N
    for i in range(N):
        event = tuple(map(int, input().split()))
        events[i] = event
    return events


def maximum_simultaneous_events(data: list[tuple]) -> int:
    START_EVENT_STATUS: int = 2
    END_EVENT_STATUS: int = 1
    events: list[tuple] = []
    for i in range(len(data)):
        start_t, delta_t = data[i]
        events.append((start_t, START_EVENT_STATUS))
        events.append((start_t + delta_t, END_EVENT_STATUS))
    events.sort(reverse=False)
    counter: int = 0
    max_sim_events: int = 0
    for event_time, event_status in events:
        if event_status == START_EVENT_STATUS:
            counter += 1
        else:
            counter -= 1
        if counter >= max_sim_events:
            max_sim_events = counter
    return max_sim_events


def main() -> None:
    events = collect_events()
    max_sim_events = maximum_simultaneous_events(events)
    print(max_sim_events)


if __name__ == "__main__":
    main()
