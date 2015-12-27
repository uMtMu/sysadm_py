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
        return (e[1:] for e in Metin.___karsilastir(a, b) if e[0] == "+")

    @staticmethod
    def cikarilan(a, b):
        return (c[1:] for c in Metin.___karsilastir(a, b) if c[0] == "-")


class Dosya:
    @staticmethod
    def oku(dosya_yolu):
        try:
            with open(dosya_yolu, 'r') as dosya:
                dosya_icerik = dosya.read()
            return dosya_icerik
        except IOError:
            print dosya_yolu + " okunamadı"

    @staticmethod
    def yaz(dosya_yolu, dosya_icerik):
        try:
            with open(dosya_yolu, "w") as dosya:
                dosya.write(dosya_icerik)
            return True
        except IOError:
            print dosya_yolu + "'a yazılamadı"


if __name__ == "__main__":
    a = """merhaba
    umut"""
    b = """merhaba
    nasılsın?"""

    #print 40 * "*"
    #print list(Metin.karsilastir(a, b))

    #print 40 * "*"
    #print list(Metin.eklenen(a, b))

    #print 40 * "*"
    #print list(Metin.cikarilan(a, b))

    Dosya.yaz("a.txt", a)
    Dosya.yaz("b.txt", b)
    ax = Dosya.oku("a.txt")
    bx = Dosya.oku("b.txt")

    print "\n".join(Metin.eklenen(ax, bx))
    print "\n".join(Metin.cikarilan(ax, bx))
    print "\n".join(Metin.karsilastir(ax, bx))
