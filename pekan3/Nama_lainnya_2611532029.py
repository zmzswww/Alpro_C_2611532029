print("=========================")
print("1. OPERATOR KEANGGOTAAN")
print("=========================")

#Input beberarpa data yang ingin dipisahkan dengan koma
input_data_2029 = input("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah input menjadi list integer
data_2029 = [int(angka.strip()) for angka in input_data_2029 .split (",")]

nilai_dicari_2029 = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil_2029 = nilai_dicari_2029 in data_2029
print("\nOperator keanggotaan IN")
print(nilai_dicari_2029,"in",data_2029,"=",hasil_2029)

#Operator not in
hasil_2029 = nilai_dicari_2029  not in data_2029
print("\nOperator keanggotaan not IN")
print(nilai_dicari_2029,"not in",data_2029,"=",hasil_2029)

print("=========================")
print("2. OPERATOR IDENTITAS")
print("=========================")

# objek1_2029 menggunakan list dari input pengguna
objek1_2029 = data_2029

# objek2_2029 merujuk pada objek yang sama dengan objek1_2029
objek2_2029 = objek1_2029

# objek3_2029 memiliki isi sama, tetapi merupakan objek baru
objek3_2029 = data_2029.copy()

print("objek1_2029 =", objek1_2029)
print("objek2_2029 =", objek2_2029)
print("objek3_2029 =", objek3_2029)

# Operator is
hasil_2029 = objek1_2029 is objek2_2029
print("\nOperator identitas IS")
print("objek1_2029 is objek2_2029 =", hasil_2029)

# Operator is not
hasil_2029 = objek1_2029 is not objek3_2029
print("\nOperator identitas IS NOT")
print("objek1_2029 is not objek3_2029 =", hasil_2029)

# Membandingkan identitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1_2029 is objek3_2029 =", objek1_2029 is objek3_2029)
print("objek1_2029 == objek3_2029 =", objek1_2029 == objek3_2029)