# Статья 83 закона “О выборах депутатов Государственной Думы Федерального Собрания Российской Федерации”
# определяет следующий алгоритм пропорционального распределения мест в парламенте.
# Необходимо распределить 450 мест между партиями, участвовавших в выборах.
# Сначала подсчитывается сумма голосов избирателей,
# поданных за каждую партию и подсчитывается сумма голосов, поданных за все партии.
# Эта сумма делится на 450, получается величина, называемая “первое избирательное частное”
# (смысл первого избирательного частного - это количество голосов избирателей,
# которое необходимо набрать для получения одного места в парламенте).
# Далее каждая партия получает столько мест в парламенте,
# чему равна целая часть от деления числа голосов за данную партию на первое избирательное частное.
# Если после первого раунда распределения мест сумма количества мест,
# отданных партиям, меньше 450, то оставшиеся места передаются по одному партиям,
# в порядке убывания дробной части частного от деления числа голосов
# за данную партию на первое избирательное частное.
# Если же для двух партий эти дробные части равны,
# то преимущество отдается той партии, которая получила большее число голосов.
# Формат ввода

# На вход программе подается список партий, участвовавших в выборах.
# Каждая строка входного файла содержит название партии (строка, возможно, содержащая пробелы),
# затем, через пробел, количество голосов, полученных данной партией – число, не превосходящее 108


from collections import Counter, defaultdict
from typing import IO, Dict


def second_order_distrib(
    unalloceted_votes: int, result: Dict[str, int], remainder: Dict[str, float]
):
    cons_add_votes = sorted(remainder.items(), key=lambda item: item[1], reverse=True)
    for i in range(unalloceted_votes):
        cons_and_vote = cons_add_votes[i]
        cons = cons_and_vote[0]
        result[cons] += 1
    return result


file_object: IO[str] = open("yandex_algo_course_v2/week4_B/inputD.txt")
counter: Counter[str, int] = Counter()
result: Dict[str, int] = {}
remainder: Dict[str, float] = {}
while True:
    line = file_object.readline().strip()
    if len(line) == 0:
        break
    words = line.split()
    num_votes = int(words[-1])
    consignment = " ".join(words[:-1])
    counter[consignment] += num_votes

first_election_number: float = sum(counter.values()) / 450
for cons, sum_votes in counter.items():
    result[cons] = int(sum_votes / first_election_number)
    remainder[cons] = sum_votes % first_election_number
unalloceted_votes = 450 - sum(result.values())
if unalloceted_votes > 0:
    result = second_order_distrib(unalloceted_votes, result, remainder)

for key, val in result.items():
    print(key, val)
