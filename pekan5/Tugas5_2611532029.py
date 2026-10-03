# === PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===

# 1. Mengambil masukan dinamis dari pengguna
print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")
n_2029 = int(input("Masukkan ukuran skala jam pasir (N): "))

# 2. Bingkai Pembatas Horizontal Atas
print("#", end="")
for i_2029 in range(4 * n_2029 + 5):
    print("=", end="")
print("#")

# 3. Fase 1: Jam Pasir Atas (Baris N turun s.d. 1)
for baris_2029 in range(n_2029, 0, -1):
    print("| ", end="")  # Sisi kiri dibatasi garis tegak (|) dan satu spasi padding
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_2029 in range(2 * (n_2029 - baris_2029)):
        print(" ", end="")
        
    # Deret angka mundur dari baris ke 1, dipisahkan spasi
    for angka_2029 in range(baris_2029, 0, -1):
        print(angka_2029, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 ke baris, diawali spasi
    for angka_2029 in range(1, baris_2029 + 1):
        print(" ", end="")
        print(angka_2029, end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_2029 in range(2 * (n_2029 - baris_2029)):
        print(" ", end="")
        
    print(" |")  # Satu spasi padding dan garis tegak (|) di sisi kanan

# 4. Fase 2: Poros Titik Pusat Jam Pasir (Singularity)
print("|", end="")  # Karakter garis tegak pembatas (|) di kiri
for spasi_2029 in range(2 * n_2029 + 1):  # Spasi penyeimbang kiri: (2 * N + 1)
    print(" ", end="")
print("<*>", end="")  # Karakter poros kristal tunggal
for spasi_2029 in range(2 * n_2029 + 1):  # Spasi penyeimbang kanan: (2 * N + 1)
    print(" ", end="")
print("|")  # Karakter garis tegak pembatas (|) di kanan

# 5. Fase 3: Jam Pasir Bawah (Baris 1 naik s.d. N)
for baris_2029 in range(1, n_2029 + 1):
    print("| ", end="")  # Sisi kiri dibatasi garis tegak (|) dan satu spasi padding
    
    # Spasi penyeimbang kiri: 2 * (N - baris)
    for spasi_2029 in range(2 * (n_2029 - baris_2029)):
        print(" ", end="")
        
    # Deret angka mundur dari baris ke 1, dipisahkan spasi
    for angka_2029 in range(baris_2029, 0, -1):
        print(angka_2029, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju dari 1 ke baris, diawali spasi
    for angka_2029 in range(1, baris_2029 + 1):
        print(" ", end="")
        print(angka_2029, end="")
        
    # Spasi penyeimbang kanan: 2 * (N - baris)
    for spasi_2029 in range(2 * (n_2029 - baris_2029)):
        print(" ", end="")
        
    print(" |")  # Satu spasi padding dan garis tegak (|) di sisi kanan

# 6. Bingkai Pembatas Horizontal Bawah
print("#", end="")
for i_2029 in range(4 * n_2029 + 5):
    print("=", end="")
print("#")