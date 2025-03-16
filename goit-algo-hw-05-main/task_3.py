from timeit import timeit
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search
from get_text_from_file import get_text_from_file

text1 = get_text_from_file("./data/text1.txt")
text2 = get_text_from_file("./data/text2.txt")


pattern1_1 = "перевіривши"
pattern2_1 = "інвертованим списком"
pattern_common = "тобто"


def main():

    rabin_karp_search_text_1 = timeit(
        lambda: rabin_karp_search(text1, pattern1_1), number=3)

    kmp_search_pattern_text_1 = timeit(
        lambda: kmp_search(text1, pattern1_1), number=3)

    boyer_moore_search_text_1 = timeit(
        lambda: boyer_moore_search(text1, pattern1_1), number=3)
    #
    #
    #
    rabin_karp_search_text_2 = timeit(
        lambda: rabin_karp_search(text2, pattern2_1), number=3)

    kmp_search_text_2 = timeit(
        lambda: rabin_karp_search(text2, pattern2_1), number=3)

    boyer_moore_search_text_2 = timeit(
        lambda: rabin_karp_search(text2, pattern2_1), number=3)

    #
    #
    #
    rabin_karp_search_common_text_1 = timeit(
        lambda: rabin_karp_search(text1, pattern_common), number=3)

    kmp_search_common_text_1 = timeit(
        lambda: kmp_search(text1, pattern_common), number=3)

    boyer_moore_search_common_text_1 = timeit(
        lambda: boyer_moore_search(text1, pattern_common), number=3)

    #
    #
    #
    rabin_karp_search_common_text_2 = timeit(
        lambda: rabin_karp_search(text2, pattern_common), number=3)

    kmp_search_common_text_2 = timeit(
        lambda: kmp_search(text2, pattern_common), number=3)

    boyer_moore_search_common_text_2 = timeit(
        lambda: boyer_moore_search(text2, pattern_common), number=3)

    print(f"| {"Pattern":<20} | {"Rabin-Karp":^20} | {
          "KMP":^20} | {"Boyer-Moore":^20} |")

    print(f"| {"-"*20} | {"-"*20} | {"-"*20} | {"-"*20} |")

    print(f"| {pattern1_1:<20} | {rabin_karp_search_text_1:^20.5f} | {
          kmp_search_pattern_text_1:^20.5f} | {boyer_moore_search_text_1:^20.5f} |")

    print(f"| {pattern2_1:<20} | {rabin_karp_search_text_2:^20.5f} | {
          kmp_search_text_2:^20.5f} | {boyer_moore_search_text_2:^20.5f} |")

    print(f"| {pattern_common + " text 1":<20} | {rabin_karp_search_common_text_1:^20.5f} | {
          kmp_search_common_text_1:^20.5f} | {boyer_moore_search_common_text_1:^20.5f} |")

    print(f"| {pattern_common + " text 2":<20} | {rabin_karp_search_common_text_2:^20.5f} | {
          kmp_search_common_text_2:^20.5f} | {boyer_moore_search_common_text_2:^20.5f} |")


if __name__ == "__main__":
    main()
