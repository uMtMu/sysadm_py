#! /usr/bin/env python
# -*- coding:utf-8 -*-
import sefim
import difflib
import os

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

eski_lsusb_dosyasi = "lsusb.txt"
yeni_lsusb_dosyasi = "lsusb_yeni.txt"
mesaj = ""
konu = "Usb arayüz değişikliği"
print 40 * "*"

try:
    with open(eski_lsusb_dosyasi, 'r') as eski:
        kontrol = eski.read()
except IOError as e:
    print eski_lsusb_dosyasi + " dosyası bulunamadı"
    out, err = sefim.runner('lsusb')
    with open(eski_lsusb_dosyasi, 'w') as eski:
        eski.write(out)
    with open(eski_lsusb_dosyasi, 'r') as eski:
        kontrol = eski.read()


try:
    out, err = sefim.runner('lsusb')

    kontrol = kontrol.splitlines()
    out = out.splitlines()

    if difflib.unified_diff(kontrol, out):
        for l in list(difflib.unified_diff(kontrol, out))[2:]:
            if l[0] == '+':
                mesaj += "Eklendi: " + l
            elif l[0] == '-':
                mesaj += "Çıkarıldı: " + l

        os.rename(eski_lsusb_dosyasi, eski_lsusb_dosyasi + "umut")
        with open(eski_lsusb_dosyasi, "w") as eski:
            eski.write(out)

except Exception as e:
    print e


sefim.send_mail(konu, mesaj)
