#
#
#
from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_2029 = float(input('Masukkan nilai jari-jari: '))
luas_2029 = PI * jari_2029 * jari_2029
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_2029, luas_2029))