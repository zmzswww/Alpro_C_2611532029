# Buat file dengan nama Boolean_NIM.py
# nama variabel ditambah 4 digit terakhir NIM contoh: nilai_2029
# Deklarasi variabel dengan tipe Boolean
is_lulus_2029 = True
is_cumlaude_2029 = True

# Menggunakan Boolean
nilai_2029 = 85
batas_lulus_2029 = 75

# Menentukan nilai Boolean dari kondisi
status_kelulusan_2029 = nilai_2029 >= batas_lulus_2029 #Hasilnya akan True

print("=== Check Kelulusan ===")
print("Nilai: ", nilai_2029)
print("Apakah Lulus?: ", status_kelulusan_2029)
if is_lulus_2029 and is_cumlaude_2029:
    print("Selamat, Anda lulus dengan predikat Cumlaude!")