def tambahKontak():
    # Input data kontak
    nama = input("Masukkan nama kontak: ")
    nomor = input("Masukkan nomor telepon: ")

    # Simpan data ke dalam file teks
    with open("Phonebook.txt", "a") as f:
        f.write(f"{nama}, {nomor}\n")

    print("Kontak berhasil ditambahkan.")

def listKontak():
    # Baca data dari file teks
    with open("Phonebook.txt", "r") as f:
        kontak = f.readlines()

    # Tampilkan data kontak
    if kontak:
        for contact in kontak:
            nama, nomor = contact.strip().split(", ")
            print(f"{nama}: {nomor}")
    else:
        print("Phonebook masih kosong.")

def hapusKontak():
    # Input nama kontak yang akan dihapus
    nama = input("Masukkan nama kontak yang akan dihapus: ")

    # Baca data dari file teks
    with open("Phonebook.txt", "r") as f:
        kontak = f.readlines()

    # Cari kontak yang sesuai dengan nama yang diinput
    found = False
    with open("Phonebook.txt", "w") as f:
        for contact in kontak:
            if nama in contact:
                found = True
            else:
                f.write(contact)

    if found:
        print(f"Kontak {nama} berhasil dihapus.")
    else:
        print(f"Tidak ditemukan kontak dengan nama {nama}.")

while True:
    # Tampilkan menu
    print("===== Phonebook =====")
    print("1. Tambah Kontak")
    print("2. Lihat Kontak")
    print("3. Hapus Kontak")
    print("4. Keluar")

    # Input pilihan menu
    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")
    
    match int(pilihan):
        case 1:
            tambahKontak()
        case 2:
            listKontak()
        case 3:
            hapusKontak()
        case 4:
            print("Terimakasih sudah menggunakan phonebook")
            break
        case _:
            print("Pilihan tidak valid. Silakan coba lagi.")
            