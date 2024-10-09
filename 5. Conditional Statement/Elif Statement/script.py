# simple calc
num1 = int(input('masukkan integer pertama anda .. '))
num2 = int(input('masukkan integer kedua anda .. '))

def func(num1, num2):
    operasi = input('masukkan operasi yang anda inginkan ..\n+\n-\n*\n/\n ...')

    if operasi == '+':
        print(num1 + num2)
    elif operasi == '-':
        print(num1 - num2)
    elif operasi == '*':
        print(num1 * num2)
    elif operasi == '/':
        print(num1 / num2)
    else:
        print('operasi yang anda masukkan tidak tersedia')

func(num1, num2)