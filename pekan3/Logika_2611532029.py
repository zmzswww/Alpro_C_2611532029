a1_2029 = input("Input nilai boolean-1 (True/false): ").strip().lower()== "true"
a2_2029 = input("Input nilai boolean-2 (True/false): ").strip().lower()== "true"

print("\nA1", a1_2029)
print("\nA2", a2_2029)

# Konjungsi : bernilai True jika keduanya True
hasil = a1_2029 and a2_2029
print("\nKonjungsi(AND)")
print("A1 and A2 =", hasil)

# Disjungsi : bernilai True jika salah satunya True
hasil = a1_2029 or a2_2029
print("\nDisjungsi(OR)")
print("A1 or A2 =", hasil)

# Negasi a1_2029 : membalik nilai a1_2029
hasil = not a1_2029
print("\nNegasi A1(NOT)")
print("not A1 =", hasil)

# Negasi a2_2029 : membalik nilai a2_2029
hasil = not a2_2029
print("\nNegasi A2(NOT)")
print("not A2 =", hasil)

#XOR: bernilai True jika kedua nilai berbeda
hasil = a1_2029 != a2_2029
print("\nDisjungsi Ekslusif (XOR)")
print("A1 XOR A2=",hasil)