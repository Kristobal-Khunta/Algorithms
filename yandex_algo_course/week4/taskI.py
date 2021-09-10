N = int(input())


def create_dictionary(N):
    dictionary = {}
    for _ in range(N):
        word = str(input())
        l_word = word.lower()
        if l_word not in dictionary:
            dictionary[l_word] = set()

        dictionary[l_word].add(word)
    return dictionary


def n_uppercase_in_str_old(s, s_lower):
    n_upper = 0
    for i in range(len(s)):
        if s[i] != s_lower[i]:
            n_upper += 1
    return n_upper


def n_uppercase_in_str(s,):
    stresses = 0
    for c in s:
        if c.isupper():
            stresses += 1
    return stresses


def find_errors_in_s(s, dictionary):
    s_lower = s.lower()
    n_upper = n_uppercase_in_str(s, s_lower)
    if n_upper != 1:
        return True
    if s_lower in dictionary:
        list_of_possible_vars = dictionary[s_lower]
        if s in list_of_possible_vars:
            return False
        else:
            return True
    else:
        return False


dictionary = create_dictionary(N)
text = list(map(str, input().split()))
total_errors = 0
for w in text:
    has_error = find_errors_in_s(w, dictionary)
    total_errors += int(has_error)
print(total_errors)
