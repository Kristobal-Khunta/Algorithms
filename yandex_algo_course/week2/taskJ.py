n = int(input())

prev = float(input())
lower = 30.0
upper = 4000.0


def update_upper(upper, value, prev):
    new_upper = (value + prev) / 2
    if new_upper < upper:
        upper = new_upper
    return upper


def update_lower(lower, value, prev):
    new_lower = (value + prev) / 2
    if new_lower > lower:
        lower = new_lower
    return lower


def analyse_value(value, prev, lower, upper, mode):
    if mode == "closer":
        if value < prev:
            upper = update_upper(upper, value, prev)
        elif value > prev:
            lower = update_lower(lower, value, prev)
    elif mode == "further":
        if value > prev:
            upper = update_upper(upper, value, prev)
        elif value < prev:
            lower = update_lower(lower, value, prev)
    return lower, upper


# import time
# print('**')
for _ in range(1, n):
    inputs = list(input().split())
    val, mode = float(inputs[0]), str(inputs[1])
    # print("input:", val, mode)
    # print("old_lower,old_upper", lower, upper)
    lower, upper = analyse_value(val, prev, lower, upper, mode)
    # print("lower, upper", lower, upper)
    prev = val
    # print("*" * 100)
    # time.sleep(0.2)

print(lower, upper)
