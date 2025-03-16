from typing import List


def bad_char_heuristic(pattern: str) -> dict:

    bad_char = {}
    for i in range(len(pattern)):
        bad_char[pattern[i]] = i
    return bad_char


def good_suffix_heuristic(pattern: str) -> List[int]:

    m = len(pattern)
    good_suffix = [0] * (m + 1)
    border_pos = [-1] * (m + 1)

    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if good_suffix[j] == 0:
                good_suffix[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j

    j = border_pos[0]
    for i in range(m + 1):
        if good_suffix[i] == 0:
            good_suffix[i] = j
        if i == j:
            j = border_pos[j]

    return good_suffix


def boyer_moore_search(text: str, pattern: str) -> List[int]:
    m = len(pattern)
    n = len(text)

    if m == 0 or n == 0 or m > n:
        return []

    bad_char = bad_char_heuristic(pattern)

    good_suffix = good_suffix_heuristic(pattern)

    s = 0
    result = []

    while s <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        if j < 0:

            result.append(s)
            s += good_suffix[0]
        else:

            bad_char_shift = j - bad_char.get(text[s + j], -1)
            good_suffix_shift = good_suffix[j + 1]
            s += max(bad_char_shift, good_suffix_shift)

    return result


if __name__ == "__main__":
    text = "Пример текста с несколькими повторениями слова 'текст'. Текст повторяется!"
    pattern = "текст"

    indices = boyer_moore_search(text, pattern)
    print(f"Вхождения шаблона '{pattern}' в тексте: {indices}")
