import pymorphy2

import w2n.numeric_dict as nums
from w2n.tools import is_cyrillic, is_numeral, calculate_a_num


replacement_map = []
morph = pymorphy2.MorphAnalyzer()

current_word = ''
current_numeral = []
start_of_numeral, end_of_numeral = None, None


def clear():
    global replacement_map
    global current_numeral
    global current_word
    global start_of_numeral
    global end_of_numeral

    replacement_map = []
    current_numeral = []
    current_word = ''
    start_of_numeral, end_of_numeral = None, None


def update_word(char: str, start: int) -> None:
    global current_word
    global start_of_numeral

    if not current_word:
        start_of_numeral = start
    current_word += char


def update_replacement_map() -> None:
    global replacement_map
    global current_numeral

    if current_numeral:
        num_start, num_end = current_numeral[0][1], current_numeral[-1][2]
        num = calculate_a_num((x[0] for x in current_numeral))
        replacement_map.append((num, num_start, num_end))
        current_numeral = []


def update_numeral(end: int) -> None:
    global current_numeral
    global current_word
    global end_of_numeral

    end_of_numeral = end
    parsed = morph.parse(current_word)[0]
    if is_numeral(parsed.tag.POS, parsed.normal_form):
        current_numeral.append(
            (
                nums.all_num[parsed.normal_form],
                start_of_numeral,
                end_of_numeral
            )
        )
    else:
        update_replacement_map()
    current_word = ''


def get_replacement_map(text: str) -> list:
    for current_position, char in enumerate(text):
        if is_cyrillic(char):
            update_word(char, start=current_position)
        elif current_word:
            if char.isspace():
                update_numeral(end=current_position)
                continue
            update_numeral(end=current_position)
            update_replacement_map()
        elif not char.isspace():
            update_replacement_map()
    else:
        if current_word:
            update_numeral(end=len(text))
            update_replacement_map()
        if current_numeral:
            update_replacement_map()
    return replacement_map
