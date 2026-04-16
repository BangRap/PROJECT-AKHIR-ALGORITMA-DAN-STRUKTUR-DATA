import csv
import os

FILE_NAME = "kamar.csv"
history_stack = []

data = []          # Ini bakal buat list
history_stack = [] # Ini ngebuat stack ya

# (RAFLY YANG BUAT) INI FILE HANDLING ===
def load_data():
  '''
  Buat ngeload data
  '''
    data = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    return data

def save_data(data):
  '''
  Buat handling save data disini make id, nomor, lantai, harga, status, penghuni
  '''
    with open(FILE_NAME, mode='w', newline='') as file:
        fieldnames = ["id", "nomor", "lantai", "harga", "status", "penghuni"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
#====

#==== MASUK BAGIAN CRUD ====

# 1.) CREATE (Lumaris)

