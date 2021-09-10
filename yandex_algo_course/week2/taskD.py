# Дан список чисел. Определите, сколько в этом списке элементов,
#  которые больше двух своих соседей и выведите количество таких элементов.


inputs = list(map(int, input().split()))

len_inputs = len(inputs)
if len_inputs < 3:
    raise ValueError("incorrect inputs")

left_val = inputs[0]
answer = 0
for i in range(1, len_inputs - 1):
    current_val = inputs[i]
    if (current_val > left_val) and (current_val > inputs[i + 1]):
        answer += 1
    left_val = inputs[i]

print(answer)
