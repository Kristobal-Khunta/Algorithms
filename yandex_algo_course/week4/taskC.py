import sys

lines = sys.stdin.read()
text = lines.split()

# file_object = open("week3/test_file.txt")
# file_object = sys.stdin
# lines = file_object.read()
# text = lines.split()
#text = list(map(str, input().split((" "))))

import sys

lines = sys.stdin.read()
text = lines.split()

count_dict = {}
for world in text:
    if world in count_dict.keys():
        count_dict[world] += 1
    else:
        count_dict[world] = 1


worlds = []
max_count = 0
for world, count in count_dict.items():
    if count > max_count:
        max_count = count
        worlds = [world]
    elif count == max_count:
        worlds.append(world)
    else:
        pass
result = sorted(worlds)[0]
print(result)
