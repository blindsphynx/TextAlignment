from enum import Enum

class Alignment(Enum):
    LEFT = 0,
    RIGHT = 1,
    CENTER = 2,
    JUSTIFY = 3


def alignText(text, alignment=Alignment.LEFT) -> str:
    if Alignment.LEFT:
        while text[0] == ' ':
            text = text[1:] + ' '
    return text


# print(alignText("     akj lk pwmm"))
