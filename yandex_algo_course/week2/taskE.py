# Дан список чисел. Определите, сколько в этом списке элементов,
#  которые больше двух своих соседей и выведите количество таких элементов.

len_array = int(input())
inputs = list(map(int, input().split()))

winner_idx = 0
winner_value = inputs[winner_idx]

for i in range(len_array):
    if inputs[i] > winner_value:
        winner_value = inputs[i]
        winner_idx = i
# print("winner_value", winner_value, "winner_idx", winner_idx)
proposals = []
for i in range(winner_idx + 1, len_array - 1):
    # print("i", i)
    # print(inputs[i] % 5)
    if (inputs[i] % 5 == 0) and (inputs[i] % 10 != 0) and (inputs[i + 1] < inputs[i]):
        proposals.append(inputs[i])
# print("proposals", proposals)
if proposals:
    max_p = max(proposals)
    place = 1
    for i in range(len_array):
        if inputs[i] > max_p:
            place += 1
    print(place)
else:
    print(0)
