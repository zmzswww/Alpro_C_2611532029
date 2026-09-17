angka1_2029 = int(input("Input angka-1= "))
angka2_2029 = int(input("Input angka-2= "))

#Penjumlahan
hasil_2029 = angka1_2029 + angka2_2029
print("\nOperator Penjumlahan")
print("Hasil = ", hasil_2029)

#Pengurangan
hasil_2029 = angka1_2029 - angka2_2029
print("\nOperator Pengurangan")
print("Hasil = ", hasil_2029)

#Perkalian
hasil_2029 = angka1_2029 * angka2_2029
print("\nOperator Perkalian")
print("Hasil = ", hasil_2029)

#Pembagian, Pembagian Bulat, Sisa Bagi
if angka2_2029 != 0:
    hasil_2029 = angka1_2029 / angka2_2029
    print("\nOperator Pembagian")
    print("Hasil = ", hasil_2029)

    hasil_2029 = angka1_2029 // angka2_2029
    print("\nOperator Pembagian Bulat")
    print("Hasil = ", hasil_2029)

    hasil_2029 = angka1_2029 % angka2_2029
    print("\nOperator Sisa Bagi")
    print("Hasil = ", hasil_2029)
else:
    print("Angka kedua tidak boleh bernilai 0.")

#Pangkat
hasil_2029 = angka1_2029 ** angka2_2029
print("\nOperator Pangkat")
print("Hasil = ", hasil_2029)