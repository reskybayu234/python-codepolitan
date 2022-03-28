def jumlahAngka(x,*angka_list):
    total = 0
    for angka in angka_list:
        total = total + angka
    print(f"Total {angka_list} = {total}")

jumlahAngka(10,10,1)

# arg_list harus berada di akhir parameter apabila kita menggunakan 2 parameter