#! /usr/bin/env python
# -*- coding:utf-8 -*-
from yardimci import Metin
from yardimci import Dosya
import sefim

from datetime import datetime

"""
    Amaç: lsusb komutu çıktısının daha önceki turda üretilen çıktı ile
    karşılaştırılıp değişikliklerinin bildirilmesi.

    eski_lsusb dosyasını oku
        yoksa 
            oluştur. bildir!!
        varsa
            lsusb komutunu çalıştır ve yeni çıktı ile eski çıktıyı karşılaştır.
            fark yoksa
                çık
            fark varsa
                eski_lsusb dosyasının ismini sonuna tarih saat ekleyerek 
                isimlendir komut çıktısını eski_lsusb dosyası olarak kaydet.
                Farkı bildir!!
"""
lsusb_eskiD = "lsusb.txt"

lsusb_eski = Dosya.oku(lsusb_eskiD)
if not lsusb_eski:
    lsusb_eski = sefim.runner("lsusb")[0]
    Dosya.yaz(lsusb_eskiD, lsusb_eski)
    print "Eski dosya bulunamadı"
else:
    lsusb_yeni = sefim.runner("lsusb")[0]

    eklenen = Metin.eklenen(lsusb_eski, lsusb_yeni)
    cikarilan = Metin.cikarilan(lsusb_eski, lsusb_yeni)

    eklenen = "\n".join(list(eklenen)[1:])
    cikarilan = "\n".join(list(cikarilan)[1:])
    if eklenen or cikarilan:
        mesaj = """USB değişikliği
        Eklenen:
        %s
        Çıkarılan:
        %s
        """ % (eklenen, cikarilan)
        lsusb_eskiDx = lsusb_eskiD.split(".")
        tarih = datetime.now().strftime("%Y%m%d%H%M%S")
        lsusb_yeniD = lsusb_eskiDx[0] + "." + tarih + "." + lsusb_eskiDx[1]
        Dosya.yaz(lsusb_yeniD, lsusb_eski)
        Dosya.yaz(lsusb_eskiD, lsusb_yeni)
        sefim.send_mail("USB değişiliği", mesaj)
