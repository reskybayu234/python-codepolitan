angka = int(input("masukkan angka : "))

for i in range(0, angka):
    if i % 2 == 0:
        continue
    print(i)
