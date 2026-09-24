umur_2029 = int(input("Input umur anda: "))
sim_2029 = input("Apakah anda sudah punya sim C (y/t): ")[0]

if umur_2029 >= 17 and sim_2029 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_2029 >= 17 and sim_2029 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_2029 < 17 and sim_2029 == 'y':
    print("Anda belum cukup umur untuk punya SIM")

if umur_2029 < 17 and sim_2029 != 'y':
    print("Anda belum cukup umur bawa motor")