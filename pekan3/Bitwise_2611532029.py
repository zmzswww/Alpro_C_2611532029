print("\n===================")
print("3. OPERATOR BITWISE")
print("===================")

angka1_2029 = int(input("Masukkan angka bitwise-1: "))
angka2_2029 = int(input("Masukkan angka bitwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1_2029 =", angka1_2029, "| biner", bin(angka1_2029))
print("angka2_2029 =", angka2_2029, "| biner", bin(angka2_2029))

# Bitwise AND
hasil_2029 = angka1_2029 & angka2_2029
print("\nBitwise AND (&)")
print(angka1_2029, "&", angka2_2029, "=", hasil_2029)
print("Biner hasil =", bin(hasil_2029))
print("Biner hasil (8 bit) =", format(hasil_2029, "08b"))

# Bitwise OR
hasil_2029 = angka1_2029 | angka2_2029
print("\nBitwise OR (|)")
print(angka1_2029, "|", angka2_2029, "=", hasil_2029)
print("Biner hasil =", bin(hasil_2029))
print("Biner hasil (8 bit) =", format(hasil_2029, "08b"))

# Bitwise XOR
hasil_2029 = angka1_2029 ^ angka2_2029
print("\nBitwise XOR (^)")
print(angka1_2029, "^", angka2_2029, "=", hasil_2029)
print("Biner hasil =", bin(hasil_2029))
print("Biner hasil (8 bit) =", format(hasil_2029, "08b"))

# Bitwise NOT
hasil_2029 = ~angka1_2029
print("\nBitwise NOT (~)")
print("~", angka1_2029, "=", hasil_2029)
print("Biner hasil =", bin(hasil_2029))
print("Biner hasil (8 bit) =", format(hasil_2029, "08b"))

# Bitwise geser kiri
jumlah_geser_2029 = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil_2029 = angka1_2029 << jumlah_geser_2029
print("\nBitwise geser kiri (<<)")
print(angka1_2029, "<<", jumlah_geser_2029, "=", hasil_2029)
print("Biner hasil =", bin(hasil_2029))
print("Biner hasil (8 bit) =", format(hasil_2029, "08b"))

# Bitwise geser kanan
hasil_2029 = angka1_2029 >> jumlah_geser_2029
print("\nBitwise geser kanan (>>)")
print(angka1_2029, ">>", jumlah_geser_2029, "=", hasil_2029)
print("Biner hasil =", bin(hasil_2029))
print("Biner hasil (8 bit) =", format(hasil_2029, "08b"))