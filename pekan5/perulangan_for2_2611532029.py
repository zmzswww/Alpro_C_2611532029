# Buat file dengan nama perulangan_for2_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

ulang_2029 = int(input("Masukkan Jumlah Perulangan: "))
print("perulangan ke-0 sampai ke-", ulang_2029-1)
for i in range(ulang_2029):
    print(i, end=" ")
print()
print("Perulangan ke-1 sampai ke-", ulang_2029)
for i in range(1, ulang_2029+1):
    print(i, end=" ")