




t0, t1 = map(int, input().split())
mode = input()
# list_of_inpust = map(int, input().split())
# print(sum(list_of_inpust))
# print(t0, t1, mode)


def conder(t0, t1, mode):
    # print("insidefunc")
    t_end = t0
    if mode == "fan":
        pass
    elif mode == "auto":
        t_end = t1
    elif (mode == "freeze") and (t1 <= t0):
        t_end = t1
    elif (mode == "heat") and (t1 >= t0):
        t_end = t1
    
    return t_end


t_end = conder(t0, t1, mode)
print(t_end)
