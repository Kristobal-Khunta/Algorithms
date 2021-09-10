# Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку sys) записан текст.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
#  Определите, сколько различных слов содержится в этом тексте.

# import sys
# lines = sys.stdin.read()
# s = lines.split()
# print(len(s))

file_object = open("week3/test_file.txt")
#file_object = sys.stdin
lines = file_object.read()
s = lines.split()
print(len(set(s)))
