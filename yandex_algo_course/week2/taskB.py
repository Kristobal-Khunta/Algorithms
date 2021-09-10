# По последовательности чисел во входных данных определите ее вид:

# CONSTANT – последовательность состоит из одинаковых значений
# ASCENDING – последовательность является строго возрастающей
# WEAKLY ASCENDING – последовательность является нестрого возрастающей
# DESCENDING – последовательность является строго убывающей
# WEAKLY DESCENDING – последовательность является нестрого убывающей
# RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов


def mode_CONST_next(current, val):
    if current == val:
        mode = "CONSTANT"
    elif current > val:
        mode = "WEAKLY ASCENDING"
    else:
        mode = "WEAKLY DESCENDING"
    return mode


def mode_ASCEN_next(current, val):
    if current == val:

        mode = "WEAKLY ASCENDING"
    elif current > val:
        # print(f'current > val,{current} > {val}')
        mode = "ASCENDING"
    else:
        mode = "RANDOM"
    return mode


def mode_WEAKLY_ASCENDING_next(current, val):
    if current < val:
        mode = "RANDOM"
    else:
        mode = "WEAKLY ASCENDING"
    return mode


def mode_DESCENDING_next(current, val):
    if current < val:
        mode = "DESCENDING"
    elif current == val:
        mode = "WEAKLY DESCENDING"
    else:
        mode = "RANDOM"
    return mode


def mode_WEAKLY_DESCENDING_next(current, val):
    if current > val:
        mode = "RANDOM"
    else:
        mode = "WEAKLY DESCENDING"
    return mode


def mode_RANDOM_next(current, val):
    return "RANDOM"


def mode_first_val(current, prev):

    if current < prev:
        mode = "DESCENDING"
    elif current == prev:
        mode = "CONSTANT"
    else:
        mode = "ASCENDING"
    return mode


get_func_to_mode = {
    "CONSTANT": mode_CONST_next,
    "ASCENDING": mode_ASCEN_next,
    "WEAKLY ASCENDING": mode_WEAKLY_ASCENDING_next,
    "DESCENDING": mode_DESCENDING_next,
    "WEAKLY DESCENDING": mode_WEAKLY_DESCENDING_next,
    "RANDOM": mode_RANDOM_next,
    "FIRST": mode_first_val,
}

BREAK_VAL = -2 * 10 ** 9

prev_val = float(input())

mode = "FIRST"
while True:
    cur_val = float(input())

    if cur_val == BREAK_VAL:
        break
    analye_seq = get_func_to_mode[mode]
    mode = analye_seq(cur_val, prev_val)
    prev_val = cur_val
    
    #print(f"cur_val {cur_val}, mode= {mode}")
if mode == "FIRST":
    print("CONSTANT")
else:
    print(mode)
