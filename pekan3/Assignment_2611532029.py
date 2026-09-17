angka1_2029 = int(input("Input angka ke-1 : "))
angka2_2029 = int(input("Input angka ke-2 : "))

print("\nNilai awal angka1 =",angka1_2029)
print("\nNilai awal angka2 =",angka2_2029)

#Assignment biasa
hasil = angka1_2029
print("\nAssignment biasa(=)")
print("Hasil =",hasil)

#Assignment penambahan
hasil = angka1_2029
hasil += angka2_2029
print("\nAssignment penambahan(+=)")
print("Hasil =",hasil)

#Assignment pengurangan
hasil = angka1_2029
hasil -= angka2_2029
print("\nAssignment pengurangan(-=)")
print("Hasil =",hasil)

#Assignment perkalian 
hasil = angka1_2029
hasil *= angka2_2029
print("\nAssignment perkalian(*=)")
print("Hasil =",hasil)

#Assignment pembagian, pembagian bulat, dan sisa bagi 
if angka2_2029 != 0:
    hasil = angka1_2029
    hasil /= angka2_2029
    print("\nAssignment pembagian(/=)")
    print("Hasil =",hasil)
    #Operator tambahan
    #Pembagian bulat
    hasil = angka1_2029
    hasil //= angka2_2029
    print("\nAssignment pembagian(//=)")
    print("Hasil =",hasil)
    #Sisa bagi
    hasil = angka1_2029
    hasil %= angka2_2029
    print("\nAssignment pembagian(%=)")
    print("Hasil =",hasil)
else:
    print("\nPembagian tidak dapat")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assignment perpangkatan
hasil = angka1_2029
hasil **= angka2_2029
print("\nAssignment perpangkatan (**=)")
print("Hasil =",hasil)