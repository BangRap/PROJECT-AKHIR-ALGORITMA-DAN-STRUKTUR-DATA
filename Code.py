import csv  # untuk baca/tulis file CSV

FILE_NAME = "kamar.csv"    # nama file penyimpanan data

# ================= DATA GLOBAL =================
data = []    # list untuk menyimpan semua data kamar (struktur data utama)
history_stack = []     # stack untuk menyimpan riwayat perubahan (undo)



# ================= FILE HANDLING =================

def load_data():
    data = []     # list kosong untuk menampung data dari file

    try:
        # buka file CSV dalam mode read
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # membaca CSV sebagai dictionary

            for row in reader:
                data.append(row) # setiap baris dimasukkan ke list

    except FileNotFoundError:
         # jika file belum ada, program tidak error
        pass

    return data    # kembalikan data dalam bentuk list


def save_data(data):
     """
    Fungsi untuk menyimpan data ke file CSV
    """
    with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
         # menentukan nama kolom
        fieldnames = ["id", "nomor", "lantai", "harga", "status", "penghuni"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()  # menulis header kolom
        writer.writerows(data) # menulis semua data ke file




# ================= LINKED LIST =================

class Node:
    def __init__(self, data):
        self.data = data  # menyimpan data kamar
        self.next = None    # pointer ke node berikutnya


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def tambah_kamar(self, kamar):
        new_node = Node(kamar)

        if not self.head:
            self.head = new_node # jika kosong, jadi head
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node    # sambungkan node baru

    def rebuild(self, data):
        self.head = None

        for kamar in data:
            self.tambah_kamar(kamar)

    def display(self):
        temp = self.head

        if not temp:
            print("Linked List kosong")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")


# ================= CRUD =================

def tambah_kamar(sll):
    '''
    Fungsi CREATE: untuk nambahin data kamar baru
    '''
    global data
    
    id = input("ID: ")
    nomor = input("Nomor kamar: ")
    lantai = input("Lantai: ")
    harga = input("Harga: ")
    status = input("Status: ") 
    penghuni = input("Penghuni: ")  

    # data disimpan dalam dictionary
    kamar = {
        "id": id,
        "nomor": nomor,
        "lantai": lantai,
        "harga": harga,
        "status": status,
        "penghuni": penghuni
    }

    history_stack.append(data.copy()) # simpan state lama ke stack

    data.append(kamar) # tambah ke list
    save_data(data) # simpan ke CSV
    sll.tambah_kamar(kamar) # tambah ke linked list

    print("Kamar berhasil ditambahkan!")


def lihat_kamar():
    '''
    Fungsi READ : untuk menampilkan semua data kamar
    '''
    global data
    
    if not data:
        print("Data kosong")
        return
   
    print("\n===== DATA KAMAR =====")

    # looping semua data
    for kamar in data:
        print(f"""
ID       : {kamar['id']}
Nomor    : {kamar['nomor']}
Lantai   : {kamar['lantai']}
Harga    : {kamar['harga']}
Status   : {kamar['status']}
Penghuni : {kamar['penghuni']}
------------------------
""")


def update_kamar(sll):
    '''
    Fungsi UPDATE: mengubah data kamar
    '''
    global data

    id_kamar = input("Masukkan ID kamar: ")

    for kamar in data:
        if kamar["id"] == id_kamar:
            history_stack.append(data.copy())  simpan ke stack

            kamar["penghuni"] = input("Nama penghuni baru: ")
            kamar["status"] = "Terisi"

            save_data(data) # update file
            sll.rebuild(data)    # update linked list

            print("Data berhasil diupdate!")
            return

    print("ID tidak ditemukan!")


def hapus_kamar(sll):
     """
    Fungsi DELETE: menghapus data kamar
    """
    global data

    id_kamar = input("Masukkan ID kamar: ")

    for kamar in data:
        if kamar["id"] == id_kamar:
            history_stack.append(data.copy())  # simpan ke stack

            data.remove(kamar) # hapus dari list

            save_data(data) # update file

            sll.rebuild(data) # update linked list

            print("Data berhasil dihapus!")
            return

    print("ID tidak ditemukan!")


# ================= STACK UNDO =================

def undo(sll):
    """
    Mengembalikan data ke kondisi sebelumnya (undo)
    """
    global data

    if history_stack:
        data = history_stack.pop() # ambil data terakhir dari stack

        save_data(data) # simpan ulang
        sll.rebuild(data) # rebuild linked list

        print("Undo berhasil!")

    else:
        print("Tidak ada riwayat.")


# ================= MENU =================

def menu():
     """
    Fungsi utama program (menu interaktif)
    """
    global data

    data = load_data() # load data dari file

    sll = SingleLinkedList()
    sll.rebuild(data) # bangun linked list dari data

    while True:
        print("""
===== MENU KAMAR =====
1. Tambah Kamar
2. Lihat Kamar
3. Update Kamar
4. Hapus Kamar
5. Undo
0. Keluar
""")
=======

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

            tambah_kamar(sll)

        elif pilih == "2":
            lihat_kamar()

        elif pilih == "3":
            update_kamar(sll)

        elif pilih == "4":
            hapus_kamar(sll)

    

        elif pilih == "5":
            undo(sll)


        elif pilih == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


# ================= RUN =================

menu()
=======
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

