# Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли, что каждый элемент этого списка больше предыдущего).

# Выведите YES, если массив монотонно возрастает и NO в противном случае.


# def monotonic_increase(inputs):
#     val = inputs[0]
#     is_monotonic = True
#     for i in range(1, len(inputs)):
#         # print(inputs[i],val)
#         if inputs[i] > val:
#             val = inputs[i]
#         else:
#             is_monotonic = False
#             break
#     return is_monotonic


# inputs = list(map(float, input().split()))

# if not inputs:
#     print("NO")
# else:
#     is_mon_increase = monotonic_increase(inputs)

# if is_mon_increase:
#     print("YES")
# else:
#     print("NO")

# Var 2 
inputs = list(map(float, input().split()))

flag = "YES"
for i in range((len(inputs) - 1)):
    diff = inputs[i + 1] - inputs[i]
    if diff <= 0:
        flag = "NO"
print(flag)
