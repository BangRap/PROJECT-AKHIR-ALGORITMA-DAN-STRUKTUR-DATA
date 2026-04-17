import csv

FILE_NAME = "kamar.csv"


data = []          # Ini bakal buat list
history_stack = [] # Ini ngebuat stack ya


# ================= INI FILE HANDLINGNYA (RAFLY YANG BUAT SESUAIN SAVE DATANYA) =================

def load_data():
  '''
  Buat ngeload data yak
  '''
    data = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File kamar.csv tidak ditemukan! Pastikan file sudah dibuat.")
    return data

def save_data(data):
  '''
  Buat Ngesave data disini make id, nomor, lantai, harga, status, penghuni  
  '''
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ["id", "nomor", "lantai", "harga", "status", "penghuni"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader() 
        writer.writerows(data) 

# ================= Bagian CRUD ==================

# === CREATE (Made by Lumaris)===
def tambah_kamar(data):
    kamar = {
        "id": input("Masukkan ID kamar: "),
        "nomor": input("Masukkan nomor kamar: "),
        "lantai": input("Masukkan lantai kamar: "),
        "harga": input("Masukkan harga kamar: "),
        "status": "Kosong",
        "penghuni": "-"
    }
    data.append(kamar)
    save_data(data)
    print("Kamar berhasil ditambahkan!")

# === READ (Made by Lumaris)===
def lihat_kamar(data):
    for kamar in data:
        print(f"ID: {kamar['id']}, Nomor: {kamar['nomor']}, Lantai: {kamar['lantai']}, Harga: {kamar['harga']}, Status: {kamar['status']}, Penghuni: {kamar['penghuni']}")

# === UPDATE ===
def update_kamar(data):
    id_kamar = input("ID: ")
    for kamar in data:
        if kamar["id"] == id_kamar:
            kamar["penghuni"] = input("Nama: ")
            kamar["status"] = "Terisi"
            save_data(data)


# === DELETE ===
def hapus_kamar(data):
    id_kamar = input("ID: ")
    for kamar in data:
        if kamar["id"] == id_kamar:
            data.remove(kamar)
            save_data(data)

# ==== MENU UTAMA ===
def main():
    data = load_data()

    while True:
        print("\n=== MANAJEMEN KOST ===")
        print("1. Tambah Kamar")
        print("2. Lihat Kamar")
        print("3. Update Kamar")
        print("4. Hapus Kamar")
        print("5. Cari Kamar")
        print("6. Sorting")
        print("7. History")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_kamar(data)
        elif pilih == "2":
            lihat_kamar(data)
        elif pilih == "3":
            update_kamar(data)
        elif pilih == "4":
            hapus_kamar(data)
        elif pilih == "5":
            cari_kamar(data)
        elif pilih == "6":
            sorting_kamar(data)
        elif pilih == "7":
            lihat_history()
        elif pilih == "0":
            break
        else:
            print("Input tidak valid!")

main()
