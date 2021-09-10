new_number = input()
number1 = input()
number2 = input()
number3 = input()


def replace_list_tokens(s, list_of_tokens, value=""):
    for token in list_of_tokens:
        s = s.replace(token, value)
    # s = s.replace("+7", "8")
    return s


def split_telephone_number(number):
    nums = number[-7:]
    if len(number) < 10:
        code = "495"
    else:
        code = number[-10:-7]
    return nums, code


# TODO Плохо обрабатывается конструкция вида +7-916--242, у меня все ок а наверно должна быть ошибка


tokens = ["-", "(", ")"]
new_number = replace_list_tokens(new_number, tokens)
new_nums, new_code = split_telephone_number(new_number)
for old_number in [number1, number2, number3]:
    old_number = replace_list_tokens(old_number, tokens)
    old_nums, old_code = split_telephone_number(old_number)
    if (old_nums == new_nums) and (old_code == new_code):
        print("YES")
    else:
        print("NO")

