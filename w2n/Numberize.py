import w2n.mapper as mapper


def replace_numerals_by_numbers(text: str) -> str:
    replacement_map = mapper.get_replacement_map(text)
    mapper.clear()
    new_text = ''
    prev_end = 0
    for item in replacement_map:
        num, start, end = item
        new_text += text[prev_end:start] + str(num)
        prev_end = end
    return new_text + text[prev_end:]