from typing import Final

# === DEKLARASI KONSTANTA ===
# Menggunakan typing.Final dan huruf kapital sesuai instruksi
BATAS_LULUS: Final[float] = 75.0

print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")

# === INPUT DATA (Tipe Data String & Char) ===
# Mengambil input nama praktikan
nama_2029 = input("Masukkan Nama Mahasiswa     : ")

# Mengambil input jenis kelamin (karakter tunggal)
jk_2029 = input("Masukkan Jenis Kelamin (L/P): ")

# Menyimpan alamat tempat tinggal secara multiline menggunakan tanda petik tiga
alamat_2029 = """Jl. Koto Tuo No.8, Limau Manis, Kec. Pauh, Kota Padang, Sumatera Barat 25163"""


# === INPUT DATA & TYPE CASTING (Tipe Data Numerik) ===
# Konversi input ke Integer untuk umur
umur_2029 = int(input("Masukkan Umur               : "))

# Konversi input ke Float untuk skor tes awal
skor_2029 = float(input("Masukkan Skor Tes Awal      : "))

# Deklarasi variabel bilangan kompleks (Complex) sebagai token identifikasi
token_2029 = 100 + 3j


# === EVALUASI BOOLEAN ===
# Evaluasi status kelulusan secara dinamis menggunakan operator perbandingan
status_lulus_2029 = skor_2029 >= BATAS_LULUS


# === OUTPUT DATA & PENGECEKAN TIPE DATA ===
print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print(f"Nama Mahasiswa  : {nama_2029} | Tipe: {type(nama_2029)}")
print(f"Jenis Kelamin   : {jk_2029} | Tipe: {type(jk_2029)}")
print(f"Alamat Domisili :\n{alamat_2029} | Tipe: {type(alamat_2029)}")
print(f"Umur            : {umur_2029} tahun | Tipe: {type(umur_2029)}")
print(f"Skor Tes Awal   : {skor_2029} | Tipe: {type(skor_2029)}")
print(f"ID Token Sinyal : {token_2029} | Tipe: {type(token_2029)}")

print("\n=== STATUS KELULUSAN PRAKTIKUM ===")
print(f"Batas Minimum Nilai  : {BATAS_LULUS}")
print(f"Apakah Dinyatakan Lulus?: {status_lulus_2029} | Tipe: {type(status_lulus_2029)}")