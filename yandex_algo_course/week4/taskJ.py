#  # и возможности начинать идентификатор с цифры
#  букв, цифр, подчеркиваний пробелами. Нареж строку на слова. Если не ключевое проверь что корректно, то есть не число
#  и не начинается с цифры если это нельзя
#  если все ок, то увеличь счетчик слов на 1 а если встретилось впервые то запомнить порядкаовый номер слова
def onlylettersDigitsUnderscore(line):
    ans = []
    for c in line:
        if c.isalpha() or c.isdigit() or c == "_":
            ans.append(c)
        else:
            ans.append(" ")
    return "".join(ans)


def isCorrect(word, isCorrect):
    if word.isdigit():
        return False
    if not word[0].isdigit() or stDigit:
        return True
    return False


#  пройди по всему словарю со счетчиками, выбери максимальное кол-во вхождений а зате то которое встречалось раньше
fin = open("week4/file_taskJ.txt", "r") # input.txt 
# strip обрезаем пробелы или каретки в конце строки
n, caseSens, stDigit = fin.readline().strip().split()
n = int(n)
caseSens = caseSens == "yes"
stDigit = stDigit == "yes"
# создай множество ключевых слов, сделай 2 булевых переменные для чувствительности к регистру

keywords = set()
for _ in range(n):
    keyword = fin.readline().strip()
    if not caseSens:
        keyword = keyword.lower()
    keywords.add(keyword)

#   заведи словарь для количества вхождений ид. и их первых позиций
cntPosind = {}
#   создай счетчик слов

wordNumber = 0
#  пробегисо по всем строчкам текста, для каждой строки замени все вхождения символов кроме букв, цифр, подчеркиваний пробелами
for line in fin.readlines():
    line = onlylettersDigitsUnderscore(line)

    # Нареж строку на слова.
    words = line.split()
    # Для каждого слова проверь не ключевое ли оно, с учетом регистра.
    for word in words:
        if not caseSens:
            word = word.lower()
        if word in keywords:
            continue
        if isCorrect(word, stDigit):
            wordNumber += 1
            if word not in cntPosind:
                cntPosind[word] = [0, wordNumber]
            cntPosind[word][0] += 1
print(cntPosind)
bestWord = ""
maxCnt = 0
minPos = 0
for word in cntPosind:
    current_cnt, current_pos = cntPosind[word]
    if (current_cnt > maxCnt) or ((current_cnt == maxCnt) and (current_pos < minPos)):
        bestWord = word
        maxCnt = current_cnt
        minPos = current_pos

print(bestWord)
