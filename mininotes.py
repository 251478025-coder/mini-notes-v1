"""
mini-notes v2 — İkinci Sürüm
Öğrenci: Pelin Kışlak (251478025)

V2 GÖREVLERİ:
1. 'list' komutu eklendi: Tüm notlar kullanıcı dostu şekilde listeleniyor.
2. 'search' komutu eklendi: Notlar içinde kelime bazlı arama yapılabiliyor.
3. V1 -> V2 geçişi için README ve kod yorum satırları güncellendi.
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
    with open(".mininotes/notes.dat", "w", encoding="utf-8") as f:
        pass
    return "Kurulum tamamlandı: .mininotes/ klasörü oluşturuldu."

def add_note(content):
    if not os.path.exists(".mininotes"):
        return "Hata: Önce 'init' komutunu çalıştırmalısınız."
    
    with open(".mininotes/notes.dat", "r", encoding="utf-8") as f:
        data = f.readlines()
    
    note_id = len(data) + 1
    current_date = get_current_date()
    
    with open(".mininotes/notes.dat", "a", encoding="utf-8") as f:
        f.write(f"{note_id}|{content}|{current_date}\n")
    return f"Not kaydedildi! ID: {note_id}"

# --- V2 İLE EKLENEN YENİ FONKSİYONLAR ---

def list_notes():
    if not os.path.exists(".mininotes/notes.dat"):
        return "Hata: Henüz hiç not yok."
    
    print("\n--- KAYITLI NOTLARINIZ ---")
    with open(".mininotes/notes.dat", "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 3:
                print(f"[{parts[0]}] {parts[2]}: {parts[1]}")
    return "--------------------------"

def search_notes(keyword):
    if not os.path.exists(".mininotes/notes.dat"):
        return "Hata: Not dosyası bulunamadı."
    
    found = False
    print(f"\n'{keyword}' için arama sonuçları:")
    with open(".mininotes/notes.dat", "r", encoding="utf-8") as f:
        for line in f:
            if keyword.lower() in line.lower():
                parts = line.strip().split("|")
                print(f"-> Bulundu [ID: {parts[0]}]: {parts[1]}")
                found = True
    
    return "Arama tamamlandı." if found else "Eşleşen not bulunamadı."

# --- ANA PROGRAM ---

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
    elif command == "list":
        print(list_notes())
    elif command == "search":
        if len(sys.argv) < 3:
            print("Hata: Aranacak kelimeyi giriniz!")
        else:
            print(search_notes(sys.argv[2]))
    else:
        print("Bilinmeyen komut: " + command)
