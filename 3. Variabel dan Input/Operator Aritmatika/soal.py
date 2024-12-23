jarak = float(input('masukkan jarak dalam satuan m.. '))
waktu = float(input('masukkan waku dalam satuan s.. '))

if waktu !=0:
    kecepatan = jarak / waktu
    print('kecepatan anda adalah', kecepatan, 'm/s')
else:
    print('kecepatan tidak boleh 0')