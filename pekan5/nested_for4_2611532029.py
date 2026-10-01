# Buat file dengan nama nested_for4_NIM.py
# Buat program untuk perulangan for dalam pytohn
# Nama variabel ditambah 4 digit nim terakhir contoh: ulang_1234
# Program ini menggunakan fungsi input()

tinggi_2029 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_2029 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_2029 = tinggi_2029 
    c_2029 = a_2029
    lebar_2029 = (2 * tinggi_2029) - 2

    for i_2029 in range(1, tinggi_2029 + 1):
        b_2029 = c_2029 + 1

        for j_2029 in range(1, lebar_2029 + 1):

            # baris atas dan bawah

            if i_2029 == 1 or i_2029 == tinggi_2029:
                if j_2029 == 1 or j_2029 == lebar_2029:
                    print("#", end= "")
                else:
                    print("=", end= "")
            # Baris isi
            else:
                if j_2029 == 1 or j_2029 == lebar_2029:
                    print("|", end="")
                else:
                    if j_2029 == c_2029:
                        print("<", end="")
                    elif j_2029 == b_2029:
                        print(">", end="")
                    elif j_2029 == (lebar_2029 - c_2029):
                        print("<", end="")
                    elif j_2029 == (lebar_2029 - c_2029 + 1):
                        print(">", end="")
                    elif j_2029 > b_2029 and j_2029 < (lebar_2029 - c_2029):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        # logika asli java

        a_2029 -= 2

        if a_2029 <= 0:
            c_2029 = (-a_2029) + 2
        else:
            c_2029 = a_2029