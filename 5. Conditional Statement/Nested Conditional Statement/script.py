# pemeriksaan bilangan
num = float(input('masukkan angka .. '))
if num < 0:
    print('angka negatif')
else:
    if num > 0:
        print('angka positif')
        if num % 2 == 0:
            print(int(num), 'angka genap')
        else:
            print(int(num), 'angka ganjil')