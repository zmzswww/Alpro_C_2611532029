# === SISTEM SIMULASI TRANSAKSI DAN VALIDASI AKSES TOKO ===
# Menggunakan akhiran NIM 2029 untuk penamaan variabel

# 1. INPUT DATA PELANGGAN & TRANSAKSI
print("=== SISTEM TRANSAKSI TOKO ===")
nama_2029 = input("Masukkan Nama Pelanggan : ")
status_2029 = input("Masukkan Status Pelanggan (member/nonmember) : ").lower()
total_belanja_2029 = float(input("Masukkan Total Belanja : "))
jumlah_barang_2029 = int(input("Masukkan Jumlah Barang : "))
kode_promo_2029 = input("Masukkan Kode Promo : ").upper()

# Daftar promo yang tersedia untuk Operator Membership
daftar_promo_2029 = ["HEMAT10", "HEMAT20", "GRATISONGKIR"]


# 2. OPERATOR PERBANDINGAN
# Memeriksa syarat minimum belanja dan jumlah barang
syarat_belanja_2029 = total_belanja_2029 >= 200000
syarat_barang_2029 = jumlah_barang_2029 >= 3
is_member_2029 = status_2029 == "member"


# 3. OPERATOR LOGIKA & OPERATOR MEMBERSHIP
# Operator Keanggotaan (Membership) untuk cek kode promo
promo_tersedia_2029 = kode_promo_2029 in daftar_promo_2029
promo_invalid_2029 = kode_promo_2029 not in daftar_promo_2029

# Operator Logika (and, or, not)
# Mendapat diskon member jika statusnya member DAN belanja >= 200.000
get_diskon_2029 = is_member_2029 and syarat_belanja_2029
# Mendapat promo tambahan jika jumlah barang cukup ATAU kode promo tersedia, dan syarat belanja tidak gagal
get_promo_2029 = (syarat_barang_2029 or promo_tersedia_2029) and (not promo_invalid_2029)


# 4. OPERATOR ARITMATIKA
# Menghitung besaran diskon, total akhir, rata-rata, dan sisa pembagian %
besaran_diskon_2029 = 0.0
if get_diskon_2029:
    besaran_diskon_2029 = total_belanja_2029 * 0.10  # Diskon 10%

total_bayar_2029 = total_belanja_2029 - besaran_diskon_2029
rata_harga_2029 = total_belanja_2029 / jumlah_barang_2029
sisa_bagi_2029 = int(total_belanja_2029) % jumlah_barang_2029  # Contoh operator %


# 5. OPERATOR PENUGASAN (Augmented Assignment)
# Menggunakan operator penugasan untuk menambahkan poin bonus jika dapat promo
poin_pelanggan_2029 = 0
if get_promo_2029:
    poin_pelanggan_2029 += 50  # Operator +=


# 6. OPERATOR IDENTITAS (Identity)
# Membuat dua objek untuk mendemonstrasikan perbandingan identitas 'is' dan 'is not'
status_salinan_2029 = status_2029
objek_baru_2029 = str(status_2029)  # Membuat string baru dengan nilai yang sama

cek_identitas_true_2029 = status_salinan_2029 is status_2029
cek_identitas_false_2029 = objek_baru_2029 is not status_2029


# 7. OPERATOR BITWISE
# Representasi biner kondisi pelanggan:
# Bit 0 (0001) -> Member
# Bit 1 (0010) -> Belanja >= 200.000
# Bit 2 (0100) -> Barang >= 3
# Bit 3 (1000) -> Promo Tersedia

bit_member_2029 = 0b0001 if is_member_2029 else 0b0000
bit_belanja_2029 = 0b0010 if syarat_belanja_2029 else 0b0000
bit_barang_2029 = 0b0100 if syarat_barang_2029 else 0b0000
bit_promo_2029 = 0b1000 if promo_tersedia_2029 else 0b0000

# Bitwise OR (|) untuk menggabungkan kondisi
kode_status_2029 = bit_member_2029 | bit_belanja_2029 | bit_barang_2029 | bit_promo_2029

# Bitwise AND (&) untuk cek status tertentu
cek_member_bitwise_2029 = kode_status_2029 & 0b0001
cek_promo_bitwise_2029 = kode_status_2029 & 0b1000

# Bitwise XOR (^) untuk membandingkan dengan kode referensi (misal referensi standar = 1011 (11))
kode_referensi_2029 = 0b1011
hasil_xor_2029 = kode_status_2029 ^ kode_referensi_2029

# Bitwise Shift Left (<<)
hasil_shift_2029 = kode_status_2029 << 1


# ================= OUTPUT PROGRAM =================

print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan       : {nama_2029}")
print(f"Status Pelanggan     : {status_2029}")
print(f"Total Belanja        : Rp{total_belanja_2029:.0f}")
print(f"Jumlah Barang        : {jumlah_barang_2029}")
print(f"Kode Promo           : {kode_promo_2029}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000        : {syarat_belanja_2029}")
print(f"Jumlah Barang >= 3         : {syarat_barang_2029}")
print(f"Status Member              : {is_member_2029}")
print(f"Kode Promo Tersedia        : {promo_tersedia_2029}")
print(f"Mendapatkan Diskon         : {get_diskon_2029}")
print(f"Mendapatkan Promo          : {get_promo_2029}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                     : Rp{besaran_diskon_2029:.0f}")
print(f"Total Pembayaran           : Rp{total_bayar_2029:.0f}")
print(f"Rata-rata Harga Barang     : Rp{rata_harga_2029:.2f}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses             : {bin(kode_status_2029)[2:].zfill(4)}")
print(f"Member Access              : {cek_member_bitwise_2029 > 0}")
print(f"Promo Access               : {cek_promo_bitwise_2029 > 0}")
print(f"Poin Bonus Ditambahkan     : {poin_pelanggan_2029}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner   : {bin(kode_status_2029)[2:].zfill(4)}")
print(f"Kode Desimal : {kode_status_2029}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member (Kode & 0001)")
print(f"Hasil Biner   : {bin(cek_member_bitwise_2029)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_member_bitwise_2029}")

print("\nCek Promo (Kode & 1000)")
print(f"Hasil Biner   : {bin(cek_promo_bitwise_2029)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_promo_bitwise_2029}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(kode_status_2029)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_2029)[2:].zfill(4)}")
print(f"Hasil XOR (^)  : {bin(hasil_xor_2029)[2:].zfill(4)} (Desimal: {hasil_xor_2029})")

print("\n=== Shift ===")
print(f"Shift Left (<< 1) Biner   : {bin(hasil_shift_2029)[2:]}")
print(f"Shift Left (<< 1) Desimal : {hasil_shift_2029}")

print("\n=== SELESAI ===")