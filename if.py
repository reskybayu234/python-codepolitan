print("harga barang : ")
hargaBarang = int(input())
print("uang kita : ")
uangKita = int(input())

if hargaBarang < uangKita:
    print("sikat")

if hargaBarang > uangKita:
    print("nabung sik")

if hargaBarang == uangKita:
    print("alhamdulillah")

sisa = uangKita - hargaBarang
print(f"sisa uang : {sisa}")