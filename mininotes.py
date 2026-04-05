"""
mini-notes v1 — Geliştirilmiş sürüm
Öğrenci: Pelin Kışlak (251478025)

V1 GÖREVLERİ:
1. Hata mesajları Türkçeye çevrildi.
2. Sabit tarih yerine sistemin o anki tarihi eklendi.
3. SPEC dökümantasyonu akademik standartlara göre güncellendi.
"""
import sys
import os
from datetime import datetime

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def initialize():
    if os.path.exists(".mininotes"):
        return "Sistem zaten kurulu."
    os.mkdir(".mininotes")
    f = open(".mininotes/notes.dat", "w", encoding="utf-8")
    f.close()
    return "Kurulum tamamlandı: .mininotes/ klasörü oluşturuldu."

def add_note(content):
    if not os.path.exists(".mininotes"):
        return "Hata: Önce 'init' komutunu çalıştırmalısınız."
    
    f = open(".mininotes/notes.dat", "r", encoding="utf-8")
    data = f.read()
    f.close()
    
    note_id = data.count("\n") + 1
    current_date = get_current_date()
    
    f = open(".mininotes/notes.dat", "a", encoding="utf-8")
    f.write(str(note_id) + "|" + content + "|" + current_date + "\n")
    f.close()
    return "Not kaydedildi! ID: " + str(note_id)

if len(sys.argv) < 2:
    print("Kullanım: py mininotes.py <komut> [argümanlar]")
else:
    command = sys.argv[1]
    if command == "init":
        print(initialize())
    elif command == "add":
        if len(sys.argv) < 3:
            print("Hata: Not içeriği girmelisiniz!")
        else:
            print(add_note(sys.argv[2]))
    else:
        print("Bilinmeyen komut: " + command)
        