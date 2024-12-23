# stringg = 'tesss'
# for char in stringg:
#     if char in ['a', 'i', 'u', 'e', 'o']:
#         break
#     print(char)
# print('the end') # stop loop jika menemukan huruf vokal

# userI = input('masukkan kalimat yang ingin anda bedah.. ')
# for char in userI:
#     if char in ['a', 'i', 'u', 'e', 'o']:
#         # continue
#         print(char)
# print('fungsi selesai')


# userI = input('masukkan input anda .. ')
# for char in userI:
#     if char in ['a', 'i', 'u', 'e', 'o']:
#         if char == 'u':
#             break
#         elif char == 'e':
#             continue
#         print(char)

# print('proses selesai')


userInput = input('masukkan angka .. ')
angka_list = list(map(int, userInput.split()))

for angka in angka_list:
    if angka < 0:
        print('bilangan tidak boleh negatif!')
        break
    elif angka % 2 == 1:
        print(angka, 'adalah bilangan ganjil')
        
    elif angka % 2 == 0:
        print(angka, 'adalah bilangan genap')
        