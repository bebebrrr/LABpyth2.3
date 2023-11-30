#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__=='__main__':
    s1=input("Введите первое слово: ")
    s2=input("Введите второе слово. Оно должно быть короче первого: ")
    if len(s2) >= len(s1):
        print(
            "Заданная длина должна быть короче длины первого введённого слова",
            file=sys.stderr
        )
        exit(1)
    r=s2.replace(s2, s1)
    print(f"Полученное слово: {r}")