# Buat file dengan nama nested_for1_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

batas_2029 = int(input("Masukkan nilai batas: "))
for line_2029 in range(1, batas_2029 + 1):
    for j_2029 in range(1, (-1 * line_2029 + batas_2029) + 1):
        print(".", end="")
    print(line_2029)