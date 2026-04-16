import csv

FILE_NAME = "kamar.csv"

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
