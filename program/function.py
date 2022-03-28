def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=====================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")

def new_kontak():
    nama = input("Nama : ")
    email = input("Email : ")
    telepon = input("Telepon : ")
    kontak = {
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak


def hapus_kontak(daftarKontak):
    telepon = input("masukkan nomor telepon")

    index = -1
    
    for i in range(0, len(daftarKontak)):
        kontak = daftarKontak[i]
        if telepon == kontak["telepon"]:
            index = i
            break
    
    if index == -1:
        print("Data kontak tidak ditemukan!")
    else:
        del daftarKontak[index]
        print("Data Berhasil dihapus!")
    