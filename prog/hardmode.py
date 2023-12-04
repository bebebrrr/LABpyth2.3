#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__=='__main__':
    s1=input("Введите первое слово: ")
    s2=input("Введите второе слово: ")

    for _, item in enumerate(s1):
        if item in s2:
            print("да")
        else:
            print("нет")
