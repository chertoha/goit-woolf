from collections import deque
import re


str1 = "A man, a plan, a canal, Panama"
str21 = "Never a foot too far, even."
str2 = "Never a foot too far, eveen."
str3 = "Eva, can I see bees in a cave?"
str4 = "Madam, in Eden, I'm Adam"
str5 = "Won't lovers revolt now?"
str6 = "abba"
str7 = "abcde"


def palindrom(text: str):

    normalized_text = re.sub(r'[^a-zA-Z]', '', text).lower()

    dq = deque()
    dq.extend(normalized_text)

    while len(dq) > 1:

        if dq.popleft() != dq.pop():
            return False

    return True


print(str1, " -> ", palindrom(str1))
print(str2, " -> ", palindrom(str2))
print(str21, " -> ", palindrom(str21))
print(str3, " -> ", palindrom(str3))
print(str4, " -> ", palindrom(str4))
print(str5, " -> ", palindrom(str5))
print(str6, " -> ", palindrom(str6))
print(str7, " -> ", palindrom(str7))
