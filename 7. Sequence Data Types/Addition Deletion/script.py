# my_list1 = ['makan', 'mandi', 69, False]
# my_list2 = ['sleep', 'eat', 'edging']
# my_list_gabungan = my_list1 + my_list2
# print(my_list_gabungan)


# append
# my_l = ['a', 'b', 'c', 'd', 'e']
# print (my_l)
# userI = input('masukkan apa aja.. ')
# my_l.append(userI)
# print(my_l)

# extend
# useri1 = ['a', 'b', 'c', 'd']
# useri2 = ['1', '2', '3', '4']
# useri1.extend(useri2)
# print(useri1)

# del
# useri1 = ['a', 'b', 'c', 'd']
# print(useri1)
# del useri1[0]
# print(useri1)

# pop
# useri1 = ['a', 'b', 'c', 'd']
# print(useri1)
# n = useri1.pop()
# print('n = ', n) # mengembalikan index yang dihapus
# print(useri1)

# remove
rep = 'y'
useri1 = ['a', 'b', 'c', 'd']
while rep == 'y':
    print(useri1)
    item = input('masukkan apa yang ingin anda hapus .. ')
    if item in useri1:
        useri1.remove(item)
        print('item ', item, 'telah dihapus')
        print(useri1)
    else:
        print(item, 'tidak ditemukan dalam daftar')
        print(useri1)
    rep = input('apakah anda ingin ulang? y/n .. ').lower()
print('terimakasih')