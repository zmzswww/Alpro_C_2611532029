# Buat file dengan nama perulangan_for3_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2029 = int(input("Masukkan jumlah perulangan: "))

jumlah_2029 = 0
for i_2029 in range(1, ulang_2029+1):
    print(i_2029, end=" ")
    jumlah_2029 = jumlah_2029 + i_2029

    if i_2029 < ulang_2029:
        print(" + ", end="")
    else:
        print(" = ", jumlah_2029, end="")
print()
print("Jumlah =", jumlah_2029)