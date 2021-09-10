# Дан список чисел. Определите, сколько в этом списке элементов,
#  которые больше двух своих соседей и выведите количество таких элементов.

len_array = int(input())
inputs = list(map(int, input().split()))

left_pointer = 0
right_pointer = len_array - 1

# print(inputs)
# print(reverse_inputs)

# за О(n) проверяем
def is_palindrom(s):
    return s == s[::-1]


reverse_answer = []
for i in range(len_array):

    subseq = inputs[i:]

    if is_palindrom(subseq):
        break
    else:
        reverse_answer.append(str(inputs[i]))

answer = reverse_answer[::-1]
# итого за O(n^2)
print(i)
if answer:
    print(' '.join(answer))

