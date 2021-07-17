import pymorphy2

import numeric_dict as nums


def is_numeral(part_of_speech: str, normal_form: str):
    return part_of_speech == 'NUMR' or normal_form == 'сто'\
           or normal_form == 'один' or normal_form in nums.millenniums


def calculate_a_num(numbers) -> int:
    res, group = 0, 0
    for num in numbers:
        if num < 1E3:
            group += num
            continue
        if group != 0:
            res += group*num
            group = 0
            continue
        res += num
    else:
        res += group
    return int(res)


def get_replacement_map(text):
    morph = pymorphy2.MorphAnalyzer()
    replacement_map = []

    word = ''
    numeral = []
    start, end = None, None

    matched = False

    for i, char in enumerate(text):
        if char.lower() in 'абвгдеэёжзийклмнопрстуфхцшчщяыьъ-':
            if not matched:
                start, matched = i, True
            word += char
            continue
        if word:
            end = i
            parsed = morph.parse(word.replace('-', ''))[0]
            if is_numeral(parsed.tag.POS, parsed.normal_form):
                numeral.append(
                    (nums.all_num[parsed.normal_form], start, end)
                )
            word, matched = '', False
            continue
        if numeral and not char.isspace():
            num_start, num_end = numeral[0][1], numeral[-1][2]
            num = calculate_a_num((x[0] for x in numeral))
            replacement_map.append((num, num_start, num_end))
            numeral = []
    return replacement_map


def replace_numerals_by_numbers(text: str) -> str:
    replacement_map = get_replacement_map(text)

    new_text = ''
    prev_end = 0
    for item in replacement_map:
        num, start, end = item
        new_text += text[prev_end:start] + str(num)
        prev_end = end
    return new_text + text[prev_end:]