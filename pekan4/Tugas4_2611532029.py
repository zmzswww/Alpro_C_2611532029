print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")
nama_2029 = input("Masukkan Nama Pengunjung        : ")
umur_2029 = int(input("Input umur anda                 : "))

# .strip().lower() untuk menangani input string
sim_2029 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

# Menu Paket Wahana
print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_2029 = input("Masukkan nomor paket (1-5)      : ").strip()
jumlah_tiket_2029 = int(input("Masukkan jumlah tiket           : "))

# Pilar 1: IF Tunggal untuk Validasi Kelogisan Tiket
if jumlah_tiket_2029 <= 0:
    print("[PERINGATAN] Kuota tiket tidak valid!")
    exit()

is_member_2029 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_valid_2029 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# Inisialisasi variabel pendukung
harga_satuan_2029 = 0
status_akses_2029 = ""

# Pilar 2: MATCH - CASE untuk Pemilihan Wahana
match paket_2029:
    case "1":
        harga_satuan_2029 = 50000
    case "2":
        harga_satuan_2029 = 75000
    case "3":
        harga_satuan_2029 = 120000
    case "4":
        harga_satuan_2029 = 100000
    case "5":
        harga_satuan_2029 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# Pilar 3: IF - ELIF - ELSE dan Operator Logika untuk Validasi Izin Kendali
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
if paket_2029 == "3":
    if umur_2029 >= 17 and sim_2029 == 'y':
        status_akses_2029 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
    elif umur_2029 >= 17 and sim_2029 != 'y':
        status_akses_2029 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
    elif umur_2029 < 17 and sim_2029 == 'y':
        status_akses_2029 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
    else:
        status_akses_2029 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
else:
    if umur_2029 >= 10:
        status_akses_2029 = "Anda memenuhi syarat umur untuk menikmati wahana ini."
    else:
        status_akses_2029 = "Anda belum cukup umur untuk menikmati wahana ini."

print(f"Status Akses: {status_akses_2029}")

# Perhitungan Subtotal
subtotal_2029 = harga_satuan_2029 * jumlah_tiket_2029
total_diskon_persen_2029 = 0

# Pilar 4: MULTI-IF Terpisah untuk Akumulasi Diskon Bertingkat
if subtotal_2029 >= 200000:
    total_diskon_persen_2029 += 10

if is_member_2029 in ['y', 'ya']:
    total_diskon_persen_2029 += 5

if kode_promo_valid_2029 in ['y', 'ya']:
    total_diskon_persen_2029 += 15

if jumlah_tiket_2029 >= 5:
    total_diskon_persen_2029 += 5

# Perhitungan Nominal Diskon dan Total Bayar
nominal_diskon_2029 = subtotal_2029 * (total_diskon_persen_2029 / 100)
total_bayar_2029 = subtotal_2029 - nominal_diskon_2029

# Pilar 5: IF - ELSE untuk Evaluasi Kelulusan Audit & Bonus
catatan_layanan_2029 = ""
if total_bayar_2029 > 300000:
    catatan_layanan_2029 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_2029 = "Terima kasih telah berkunjung."

# OUTPUT RINCIAN PEMBAYARAN (Format Desimal f-string)
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_2029:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_2029}% (Rp {nominal_diskon_2029:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_2029:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_2029}")
print("Program Selesai")