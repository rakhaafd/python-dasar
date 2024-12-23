num = int(input('input number .. '))
def option(n):
    confirm = int(input('anda ingin apa?\ncek bilangan (1).. \ncalc simple(2).. '))

    if confirm == 1:
        if n % 2 == 0:
            print(n, 'adalah bilangan genap')
        else:
            print(n, 'adalah bilangan ganjil')

    else:
        input2 = int(input('masukkan angka kedua.. '))
        operasi = input('masukkan operasi.. +\n-\n*\n/\n')

        if operasi == '+':
            print(n + input2)

        elif operasi == '-':
            print(n - input2)

        elif operasi == '*':
            print(n * input2)

        elif operasi == '/':
            print(n / input2)

        else:
            print('operasi tidak sesuai')

option(num)