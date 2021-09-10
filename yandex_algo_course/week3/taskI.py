N = int(input())

result_min = set()
result_any = set()
n = 0
while n != N:
    M = int(input())
    person_set = set()
    m = 0
    while m != M:
        language = str(input())
        person_set.add(language)
        m += 1
    if n == 0:
        result_min = person_set
    result_min = result_min & person_set
    result_any = result_any | person_set

    n += 1

print(len(result_min))
for l in result_min:
    print(l)
print(len(result_any))
for l in result_any:
    print(l)
