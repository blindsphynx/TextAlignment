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
    if alignment == Alignment.JUSTIFY:
        return '\n'.join(alignmentJustify(widthFormattedText, textWidth))


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


def alignmentJustify(widthFormattedText, textWidth):
    localWidthFormattedText = list(widthFormattedText)
    for i in range(len(localWidthFormattedText)):
        line = localWidthFormattedText[i]
        if localWidthFormattedText[0] == ' ':                                    # cut spaces on the right
            line = line[1:]
        if localWidthFormattedText[-1] == ' ':                                   # cut spaces on the left
            line = line[:-1]

        countOfWords = len(line.split(' '))                                      # number of words in a line
        tempLine = ""

        if countOfWords == 1:                                                    # if a line has only one word
            tempLine = localWidthFormattedText[i].split(' ')[0]
            localWidthFormattedText[i] = tempLine
            continue

        spacesBetweenWords = textWidth                                           # count available places for spaces

        for word in localWidthFormattedText[i].split(' '):
            spacesBetweenWords -= len(word)

        needSpaces = spacesBetweenWords // (countOfWords - 1)                    # how many spaces to add between words
        extraSpaces = spacesBetweenWords % (countOfWords - 1)                    # extra spaces (when the number is odd)

        for word in localWidthFormattedText[i].split(' ')[:countOfWords - 1]:    # start to put it all together
            if extraSpaces > 0:
                tempLine += word
                for j in range(needSpaces + 1):
                    tempLine += ' '
                    extraSpaces -= 1
            else:
                tempLine += word
                for j in range(needSpaces):
                    tempLine += ' '

        localWidthFormattedText[i] = tempLine + localWidthFormattedText[i].split(' ')[countOfWords - 1]
    return localWidthFormattedText


def getWidthFormattedText(text, textWidth) -> str:          # this function makes every line as long as textWidth
    def transferWord(_tempWord):                            # this function transfers a part of a word to the next line
        tempIt = textWidth - len(newText[-1])               # width of a line without the last word
        newText[len(newText) - 1] += _tempWord[:tempIt]     # add a new word cut to the end of a line
        newText.append("")
        if len(_tempWord[tempIt:]) > textWidth:             # if this new word is longer than width
            return transferWord(_tempWord[tempIt:])         # transfer it
        return _tempWord[tempIt:]

    def spaceAtTheEndOfAWord():
        if len(newText[-1]) < textWidth:                    # if the last word is shorter than a possible line
            newText[len(newText) - 1] += " "                # add space at the end
        else:
            newText.append("")

    if textWidth <= 0:
        raise Exception("textWidth less than or equal to 0")

    newText = [""]                                          # to keep processed words

    oneStringText = text.replace('\n', ' ')                 # convert our text into one string

    for word in oneStringText.split(' '):                   # convert this string into a list of separate words
        tempWord = word                                     # in order to be able to use a word itself, not as iterator

        if len(word) > textWidth:                           # if a word is longer than width of a line
            temp = transferWord(tempWord)                   # transfer a part of a word

            newText[-1] += temp                             # add the first part of a transferred word to newText
            spaceAtTheEndOfAWord()                          # add space if needed

        elif len(word) > textWidth - len(newText[-1]):      # if a word is longer than width without the last newText ->
            newText.append(tempWord)                        # element, add a word to newText
            spaceAtTheEndOfAWord()

        else:
            newText[len(newText) - 1] += tempWord           # add a word at the end of newText
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
# заживления глубоких и трудных ран.""", alignment=Alignment.JUSTIFY, textWidth=30))

# print(alignText(text="""Аналитики Яндекс Go изучили статистику заказов такси в предновогодний вечер,
# ночь и утро 1 января в прошлые годы и поделились рекомендациями, в какое время поездки будут более выгодными.
# Цена на такси зависит от множества факторов: количества свободных машин в районе, где находится пользователь,
# числа желающих заказать такси, пробок, тарифа, расстояния и длительности дороги. Чем больше шоферов готовы принять
# заказ, тем ниже будет стоимость. И наоборот – чем меньше свободных водителей на линии, тем дороже может
# оказаться поездка. Лучше всего 31 декабря заказывать такси до 20:00 или начиная с 22:00. Вечером большинство людей
# уже успели завершить поездки – сделали последние покупки или добрались в гости. То есть свободных машин больше,
# такси приедет быстрее, стоимость поездки будет ниже. Но стоит поторопиться, потому что ближе к полуночи водители
# завершают смены, чтобы успеть к семьям за новогодний стол. После боя курантов и до 2:00 ночи 1 января многие люди
# не сидят дома и путешествуют из гостей в гости или ездят к главным городским ёлкам. Таксистов на линии по-прежнему
# меньше, чем в обычную ночь, а спрос на этот вид транспорта начинает расти. Так что в этот период оно может стоить
# чуть дороже. С 2:00 до 4:00 утра — наиболее удачное время для того, чтобы отправиться в гости, погулять по городу или,
# наоборот, вернуться домой: спрос уже не так высок, и стоимость поездки снижается. Утром 1 января заказывать такси
# лучше с 08:00 утра: в это время водители начинают выходить на линию, а большинство гуляющих к этому моменту уже
# вернулись домой.""", alignment=Alignment.JUSTIFY, textWidth=1))
