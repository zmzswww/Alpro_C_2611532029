# Buat file dengan nama Boolean_NIM.py
# nama variabel ditambah 4 digit terakhir NIM contoh: nilai_2029
# Deklarasi variabel dengan tipe Boolean
is_lulus = True
is_cumlaude = True

# Menggunakan Boolean
nilai = 85
batas_lulus = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan = nilai >= batas_lulus #Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai: ", nilai)
print("Apakah Lulus?: ", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")