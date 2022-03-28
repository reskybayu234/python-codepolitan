data = int(input("masukkan banyak data : "))

nama = []
umur = []

for d in range(0, data):
    data_nama = input("masukkan nama : ")
    data_umur = int(input("masukkan umur : "))

    nama.append(data_nama)
    umur.append(data_umur)

print(len(nama))

for n in range(0, len(nama)):
    data_nama = nama[n]
    data_umur = umur[n]
    print(f" nama {data_nama}, umur {data_umur}")
