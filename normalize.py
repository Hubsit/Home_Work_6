import re

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()


def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = t_name[::-1]
    t_name_suffix = ''

    for i in t_name:
        t_name_suffix += i
        if i == '.':
            break

    if t_name == t_name_suffix:
        t_name = re.sub(r'\W', '_', t_name[::-1])

    else:
        t_name = t_name[::-1]
        t_name_preffix = list(t_name.partition(t_name_suffix[::-1]))
        t_name = re.sub(r'\W', '_', t_name_preffix[0]) + t_name_suffix[::-1]

    return t_name