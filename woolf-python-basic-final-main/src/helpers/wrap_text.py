from typing import List


def wrap_text(text: str, symbols_num: int) -> List[str]:
    return [text[i:i + symbols_num] for i in range(0, len(text), symbols_num)]
