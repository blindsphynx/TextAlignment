import math
from enum import Enum


class Alignment(Enum):
    LEFT = 0,
    RIGHT = 1,
    CENTER = 2,
    JUSTIFY = 3


def alignText(text, alignment=Alignment.LEFT, textWidth=120) -> str:
    widthFormattedText = getWidthFormattedText(text, textWidth)
    if alignment == Alignment.LEFT:
        return '\n'.join(alignmentLeft(widthFormattedText, textWidth))
    if alignment == Alignment.RIGHT:
        return '\n'.join(alignmentRight(widthFormattedText, textWidth))
    if alignment == Alignment.CENTER:
        return '\n'.join(alignmentCenter(widthFormattedText, textWidth))
    # if alignment == Alignment.JUSTIFY:
    #     return '\n'.join(alignmentJustify(widthFormattedText, textWidth))


def alignmentLeft(widthFormattedText, textWidth):
    localWidthFormattedText = list(widthFormattedText)
    for i in range(len(localWidthFormattedText)):
        line = localWidthFormattedText[i]
        while line[0] == ' ':
            line = line[1:] + ' '

        while len(line) < textWidth:
            line = line + ' '

        localWidthFormattedText[i] = line
    return localWidthFormattedText


def alignmentRight(widthFormattedText, textWidth):
    localWidthFormattedText = list(widthFormattedText)
    for i in range(len(localWidthFormattedText)):
        line = localWidthFormattedText[i]
        while line[-1] == ' ':
            line = ' ' + line[:-1]

        while len(line) < textWidth:
            line = ' ' + line

        localWidthFormattedText[i] = line
    return localWidthFormattedText


def alignmentCenter(widthFormattedText, textWidth):
    localWidthFormattedText = list(widthFormattedText)
    for i in range(len(localWidthFormattedText)):
        line = localWidthFormattedText[i]
        while line[0] == ' ':
            line = line[1:]
        while line[-1] == ' ':
            line = line[:-1]
        for j in range(math.floor((textWidth - len(line)) / 2)):
            line = ' ' + line
        for j in range(math.ceil((textWidth - len(line)) / 2)):
            line = line + ' '
        localWidthFormattedText[i] = line
    return localWidthFormattedText


# def alignmentJustify(widthFormattedText, textWidth):
#     pass


def getWidthFormattedText(text, textWidth) -> str:
    def transferWord(_tempWord):
        tempIt = textWidth - len(newText[-1])
        newText[len(newText) - 1] += _tempWord[:tempIt]
        newText.append("")
        if len(_tempWord[tempIt:]) > textWidth:
            return transferWord(_tempWord[tempIt:])
        else:
            return _tempWord[tempIt:]

    def spaceAtTheEndOfAWord():
        if len(newText[-1]) < textWidth:
            newText[len(newText) - 1] += " "
        else:
            newText.append("")

    if textWidth <= 0:
        raise Exception("textWidth less than or equal to 0")

    newText = [""]

    oneStringText = text.replace('\n', ' ')

    for word in oneStringText.split(' '):
        tempWord = word

        if len(word) > textWidth:
            temp = transferWord(tempWord)

            newText[-1] += temp
            spaceAtTheEndOfAWord()

        elif len(word) > textWidth - len(newText[-1]):
            newText.append(tempWord)
            spaceAtTheEndOfAWord()

        else:
            newText[len(newText) - 1] += tempWord
            spaceAtTheEndOfAWord()
    return newText


# print(alignText(text="""Впервые более чем за 250 млн лет ящерицы смогли
# восстановить идеальный хвост. Это получилось при помощи ученых из Университета
# Южной Калифорнии. Исследователи сравнили, как хвосты ящериц растут во время
# эмбрионального периода и во взрослом возрасте — после того как первый хвост
# отпал. В обоих случаях ключевую роль играют нервные стволовые клетки, но ведут они себя по-разному.
# У взрослых ящериц эти клетки вырабатывают молекулярный сигнал, блокирующий
# формирование скелета и нервов, но стимулирующий рост хряща. В итоге получается
# не хвост, а просто хрящевая трубка.
# Ученые попробовали пересаживать эмбриональные клетки взрослым особям,
# но это не помогло. Тогда они применили генетическое редактирование и
# сделали эмбриональные клетки устойчивыми к молекулярному сигналу. После этого
# ящерицы смогли восстановить нормальный хвост уже во взрослом возрасте.
# Теперь исследователи хотят усовершенствовать свой метод и использовать его для
# заживления глубоких и трудных ран.""", alignment=Alignment.CENTER, textWidth=30))
