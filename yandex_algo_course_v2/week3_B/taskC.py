# Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# Элементы нужно выводить в том порядке, в котором они встречаются в списке.


seq = list(map(int, input().split()))
not_unique_elements = set()
cum_set = set()
ans = list()
for v in seq:
    if v in cum_set:
        not_unique_elements.add(v)
    else:
        cum_set.add(v)
for v in seq:
    if v not in not_unique_elements:
        ans.append(v)


print(*ans)
