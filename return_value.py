def jumlah(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return total

total = jumlah(10,2,3,4,5)

print(total)
