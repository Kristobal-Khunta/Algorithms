# var1
# text = list(map(str, input().split((" "))))

# var 2
# file_object = open("week3/test_file.txt")
# file_object = sys.stdin
# lines = file_object.read()
# text = lines.split()

# var 3
import sys

lines = sys.stdin.read()
text = lines.split()

count_dict = {}
result = []
for world in text:
    num_prev = count_dict.get(world, 0)
    result.append(str(num_prev))
    if num_prev == 0:
        count_dict[world] = 1
    else:
        count_dict[world] += 1

print(" ".join(result))
