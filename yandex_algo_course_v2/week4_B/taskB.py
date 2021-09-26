from typing import Tuple, Dict, IO

file_object: IO[str] = open("yandex_algo_course_v2/week4_B/input.txt")
counter: Dict[int, int] = {}
while True:
    line: str = file_object.readline().strip()
    if len(line) == 0:
        break
    t: Tuple[str, int] = line.split()
    person: str = str(t[0])
    num_votes: int = int(t[1])
    if person not in counter:
        counter[person] = 0
    counter[person] += num_votes


for k in sorted(counter):
    print(k, counter[k])

