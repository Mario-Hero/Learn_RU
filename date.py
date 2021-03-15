#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Created by Mario Chen, 06.12.2020, Shenzhen
# My Github site: https://github.com/Mario-Hero

import sys
import math

COLOR_RED = '31'
COLOR_GREEN = '32'
COLOR_ORANGE = '33'

## ------------ Edit This Part To Initialize -----------

COLOR_STRESS = COLOR_RED  # Pick a stress color U like
stressOn = True           # Stress ON!

## -------- The Most Important List, Be Careful --------

ONE = ['оди\'н', 'два\'', 'три\'', 'четы\'ре', 'пя\'ть', 'ше\'сть', 'се\'мь', 'во\'семь', 'девя\'ть']
TWENTY = ['деся\'ть', 'оди\'ннадцать', 'двена\'дцать', 'трина\'дцать', 'четы\'рнадцать', 'пятна\'дцать',
          'шестна\'дцать', 'семна\'дцать', 'восемна\'дцать', 'девятна\'дцать']
NINE_NINE = ['два\'дцать', 'три\'дцать', 'со\'рок', 'пятьдеся\'т', 'шестьдеся\'т', 'се\'мьдесят', 'во\'семьдесят',
             'девяно\'сто']
HUNDRED = ['сто\'', 'две\'сти', 'три\'ста', 'четы\'реста', 'пятьсо\'т', 'шестьсо\'т', 'семьсо\'т', 'восемьсо\'т',
           'девятьсо\'т']
THOUSAND = ['ты\'сяча', 'ты\'сячи', 'ты\'сяч']

NUMBER_ONE = ['пе\'рвый', 'второ\'й', 'тре\'тий', 'четвёртый', 'пя\'тый', 'шесто\'й', 'седьмо\'й', 'восьмо\'й',
              'девя\'тый']
# 11~20 is regular. [i] = TWENTY[i][:-1] + 'ый'
NUMBER_HUNDRED = ['со\'тый', 'двухсо\'тый', 'трехсо\'тый',
                  'четырёхсотый']  # 500-900 is regular. [i] = HUNDRED[i] + 'ый'
NUMBER_THOUSAND = ['тыся\'чный', 'двухты\'сячный', 'трёхтысячный', 'четырёхтысячный', 'пятиты\'сячный',
                   'шеститы\'сячный', 'семиты\'сячный','восьмиты\'сячный','девятиты\'сячный']

MONTH = ['янва\'рь', 'февра\'ль', 'ма\'рт', 'апре\'ль', 'ма\'й', 'ию\'нь', 'ию\'ль', 'а\'вгуст', 'сентя\'брь',
         'октя\'брь', 'ноя\'брь', 'дека\'брь']
MONTH_2 = ['января\'', 'февраля\'', 'ма\'рта', 'апре\'ля', 'ма\'я', 'ию\'ня', 'ию\'ля', 'а\'вгуста', 'сентября\'',
           'октября\'', 'ноября\'', 'декабря\'']
MONTH_6 = ['январе\'', 'феврале\'', 'ма\'рте', 'апре\'ле', 'ма\'е', 'ию\'не', 'ию\'ле', 'а\'вгусте', 'сентябре\'',
           'октябре\'', 'ноябре\'', 'декабре\'']

HELP = "Please input day.month.year or month.year or year or century(XVI form)"


def numberTwenty(num):
    return TWENTY[num - 10][:-1] + 'ый'


def getMonth(num, i):
    if num >= 13 or num <= 0:
        print("Wrong Month")
        exit(1)
    else:
        if i == 1:
            return MONTH[num - 1]
        if i == 2:
            return MONTH_2[num - 1]
        if i == 6:
            return MONTH_6[num - 1]


def thousandNum(num):
    if num >= 10:
        print("Too Many Years")
        exit(1)
    if num >= 1:
        if num >= 5:
            return ONE[num - 1] + ' ' + THOUSAND[2]
        elif num == 1:
            #return 'одна\' ' + THOUSAND[0]
            return THOUSAND[0]
        elif num == 2:
            return 'две\' ' + THOUSAND[1]
        else:
            return ONE[num - 1] + ' ' + THOUSAND[1]
    return THOUSAND[0]


def toCase(num, i):
    if num >= 10000:
        print("Too Many Years.")
        exit(1)
    if num >= 1000:
        if num == math.floor(num / 1000) * 1000:
            if i == 2:
                return NUMBER_THOUSAND[math.floor(num / 1000) - 1][:-2] + 'ого'
            if i == 6:
                return NUMBER_THOUSAND[math.floor(num / 1000) - 1][:-2] + 'ом'
        else:
            return thousandNum(math.floor(num / 1000)) + ' ' + toCase(num - math.floor(num / 1000) * 1000, i)
    elif num >= 100:
        if num == math.floor(num / 100) * 100:
            if i == 2:
                if math.floor(num / 100) >= 5:
                    return HUNDRED[math.floor(num / 100) - 1] + 'ого'
                else:
                    return NUMBER_HUNDRED[math.floor(num / 100) - 1][:-2] + 'ого'
            if i == 6:
                if math.floor(num / 100) >= 5:
                    return HUNDRED[math.floor(num / 100) - 1] + 'ом'
                else:
                    return NUMBER_HUNDRED[math.floor(num / 100) - 1][:-2] + 'ом'
        else:
            return HUNDRED[math.floor(num / 100) - 1] + ' ' + toCase(num - math.floor(num / 100) * 100, i)
    elif num >= 20:
        if num == math.floor(num / 10) * 10:
            if i == 2:
                return NINE_NINE[math.floor(num / 10) - 2][:-1] + 'ого'
            if i == 6:
                return NINE_NINE[math.floor(num / 10) - 2][:-1] + 'ом'
        else:
            return NINE_NINE[math.floor(num / 10) - 2] + ' ' + toCase(num - math.floor(num / 10) * 10, i)
    elif num >= 10:
        if i == 2:
            return TWENTY[num - 10][:-1] + 'ого'
        if i == 6:
            return TWENTY[num - 10][:-1] + 'ом'
    else:
        # 2678 remove й  -> + го
        # 1459 remove ый -> + ого
        # 3    remove ий -> + ьего
        if num == 3:
            number_one_temp = NUMBER_ONE[num - 1][:-2] + 'ье'
        elif num == 1 or num == 4 or num == 5 or num == 9:
            number_one_temp = NUMBER_ONE[num - 1][:-2] + 'о'
        else:
            number_one_temp = NUMBER_ONE[num - 1][:-1]
        if i == 2:
            return number_one_temp + 'го'
        if i == 6:
            return number_one_temp + 'м'


def printWord(word):
    i = word.find("ё")
    findE = False
    if i == -1:
        i = word.find("\'")
    else:
        findE = True
    if stressOn is True:
        if i > 0:
            if findE:
                print(
                    '\033[0m' + word[:i] + '\033[' + COLOR_STRESS + ';1m' + word[i] + '\033[0m' + word[i + 1:],
                    end="")
            else:
                print('\033[0m' + word[:i - 1] + '\033[' + COLOR_STRESS + ';1m' + word[i - 1] + '\033[0m' + word[i + 1:],
                  end="")
        else:
            print(word, end="")
    else:
        if i > 0:
            if findE:
                print(word, end="")
            else:
                print(word[:i] + word[i + 1:], end="")
        else:
            print(word, end="")


def printSentence(sen):
    for word in sen.split(' '):
        printWord(word + ' ')


def main(argv):
    input_word = argv[0].lower()
    # print(input_word)
    cut = [0, 0, 0]
    cutI = 0
    cutPI = 0
    for p in input_word:
        if p == '.':
            cut[cutI] = cutPI
            cutI += 1
        cutPI += 1
    if cutI == 2:
        try:
            day = int(input_word[:cut[0]])
            month = int(input_word[cut[0] + 1:cut[1]])
            year = int(input_word[cut[1] + 1:])
        except ValueError:
            print("Wrong input")
            exit(1)
        if day >= 31 or day <= 0:
            print("Wrong day")
            exit(1)
        sen = toCase(day, 2) + ' ' + getMonth(month, 2) + ' ' + toCase(year, 2) + ' го\'да'
        printSentence(sen)
    elif cutI == 1:
        try:
            month = int(input_word[:cut[0]])
            year = int(input_word[cut[0] + 1:])
        except ValueError:
            print("Wrong input")
            exit(1)
        sen = 'в ' + getMonth(month, 6) + ' ' + toCase(year, 2) + ' го\'да'
        printSentence(sen)
    elif cutI == 0:
        if input_word.find('x') >= 0 or input_word.find('i') >= 0 or input_word.find('v') >= 0:
            i = len(input_word) - 1
            shouldAdd = True
            num = 0
            while i >= 0:
                if input_word[i] == 'i':
                    if shouldAdd:
                        num += 1
                    else:
                        num -= 1
                elif input_word[i] == 'v':
                    num += 5
                    shouldAdd = False
                elif input_word[i] == 'x':
                    num += 10
                    shouldAdd = False
                else:
                    print("Wrong Century Number.")
                    exit(1)
                i -= 1
            sen = toCase(num, 2) + ' ве\'ка'
            printSentence(sen)
        else:
            try:
                year = int(input_word)
            except ValueError:
                print("Wrong Year")
                exit(1)
            sen = 'в ' + toCase(year, 6) + ' году\''
            printSentence(sen)
    print("")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(HELP)
        exit(0)
    main(sys.argv[1:])
