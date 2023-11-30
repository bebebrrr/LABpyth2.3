#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    s = input("Введите предложение без символа - : ")
    if '-' in s:
        print(
            "В предложении не должно присутствовать символа - ",
            file = sys.stderr
        )
        exit(1)
    words = s.split(' ')

    print("Количество букв о в первом слове: ", words[0].count('о'))