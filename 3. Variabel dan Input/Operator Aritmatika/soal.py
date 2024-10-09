# projek menghitung kecepatan
jarak = float(input("masukan jarak (m): "))
waktu = float(input("masukan waktu (s): "))

if waktu != 0:
    kecepatan = jarak / waktu  # Indentasi ditambahkan
    print("kecepatan =", kecepatan, "m/s")  # Menggunakan indentasi yang tepat
else:
    print("waktu tidak boleh 0")