from collections import deque

str1 = "( ){[ 1 ]( 1 + 3 )( ){ }}"
str2 = "( 23 ( 2 - 3);:"
str3 = "( 11 }:"
str4 = "( ) { [ ] ( ) ( ) { } } }"
str5 = "( ( ( )"
str6 = "(symbol in braces[1]) and (len(stack) == 0)"


braces = [["(", "{", "["], [")", "}", "]"]]


def symetric(string: str):
    stack = deque()

    for symbol in string:
        if symbol not in braces[0] + braces[1]:
            continue

        if (symbol in braces[1]) and (len(stack) == 0):
            return False

        if symbol in braces[0]:
            stack.append(symbol)
            continue

        i = braces[1].index(symbol)
        if stack[-1] != braces[0][i]:
            return False

        stack.pop()

    if len(stack) != 0:
        return False

    return True


print(str1, " -> ", symetric(str1))
print(str2, " -> ", symetric(str2))
print(str3, " -> ", symetric(str3))
print(str4, " -> ", symetric(str4))
print(str5, " -> ", symetric(str5))
print(str6, " -> ", symetric(str6))
