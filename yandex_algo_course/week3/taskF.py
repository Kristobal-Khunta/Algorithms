input1 = str(input())
input2 = str(input())

second_genom_pairs = set()
for i in range(1, len(input2)):
    pair = input2[i - 1 : i + 1]
    second_genom_pairs.add(pair)
result = 0
for i in range(1, len(input1)):
    pair = input1[i - 1 : i + 1]
    if pair in second_genom_pairs:
        result += 1

print(result)
