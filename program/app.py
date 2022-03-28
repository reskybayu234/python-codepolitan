import function

daftarKontak = []
daftarKontak.append({
    "nama" : "resky",
    "email" : "reskybayu234@gmail.com",
    "telepon" : "0823427474"
})
while True:
    print("# Menu")
    print("1. Daftar Kontak")
    print("2. Tambah Kontak")
    print("3. Hapus Kontak")
    print("4. Cari Kontak")
    print("0. Keluar")

    menu = input("Pilih menu program : ")
    if menu == "0":
        break
    elif menu == "1":
        function.display_kontak(daftarKontak)
    elif menu == "2":
        kontak = function.new_kontak()
        daftarKontak.append(kontak)
    elif menu == "3":
        function.hapus_kontak(daftarKontak)
        
print("Program Selesai, Sampai Jumpa")