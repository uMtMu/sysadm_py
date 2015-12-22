#! /usr/bin/env python
# -*- coding:utf-8 -*-

import difflib


class Metin:

    def __init__(self):
        pass

    @staticmethod
    def ___karsilastir(a, b):
        a = a.splitlines()
        b = b.splitlines()

        return difflib.unified_diff(a, b)

    @staticmethod
    def karsilastir(a, b):
        return Metin.___karsilastir(a, b)

    @staticmethod
    def eklenen(a, b):
        return (e for e in Metin.___karsilastir(a, b) if e[0] == "+")

    @staticmethod
    def cikarilan(a, b):
        return (c for c in Metin.___karsilastir(a, b) if c[0] == "-")


if __name__ == "__main__":
    a = """merhaba
    umut"""
    b = """merhaba
    nasılsın?"""

    print 40 * "*"
    print list(Metin.karsilastir(a, b))

    print 40 * "*"
    print list(Metin.eklenen(a, b))

    print 40 * "*"
    print list(Metin.cikarilan(a, b))
