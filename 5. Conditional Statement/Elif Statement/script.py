num1 = int(input('masukkan angka pertama anda.. '))
num2 = int(input('masukkan angka kedua anda.. '))

def calc(n1, n2):
    opr = input('input ur operation.. ')
    if opr == '+':
        print(n1 + n2)

    elif opr == '-':
        print(n1 + n2)

    elif opr == '*':
        print(n1 * n2)

    elif opr == '/':
        print(n1 / n2)

    else:
        print('operasi anda salah')

calc(num1, num2)