#input dari user
total_belanja_2029 = float(input("Masukkan total belanja (Rp): "))

#input status member (mengecek apakah user mengetik 'y' atau 'ya')
input_member_2029 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_2029 = input_member_2029 in ["y", "ya"]

#input status kode promo (mengecek apakah user mengetik 'y' atau 'ya')
input_promo_2029 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_2029 = input_promo_2029 in ["y", "ya"]

total_diskon_persen_2029 = 0

if total_belanja_2029 > 1000000:
    total_diskon_persen_2029 += 10 #Diskon belanja besar

if is_member_2029:
    total_diskon_persen_2029 += 5 #Diskon member

if kode_promo_valid_2029:
    total_diskon_persen_2029 += 15 #Diskon voucher

nominal_diskon_2029 = total_belanja_2029 * (total_diskon_persen_2029 / 100)
total_bayar_2029 = total_belanja_2029 - nominal_diskon_2029

print("\n--- Rincian Pembayaran ---")
print(f"Total diskon    : {total_diskon_persen_2029}% (Rp {nominal_diskon_2029:,.0f})")
print(f"Total bayar     : Rp {total_bayar_2029:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_persen_2029}%")