my_arr = []
rep = 'y'
while rep == 'y':
    print('\nCurrent Array:', my_arr, '\n')
    userConfirm = input('anda ingin menambah atau menghapus array?\nKetik 1 untuk menambah\nKetik 2 untuk menghapus\n.. ')

    if userConfirm == '1':
        userInpAdd = input('masukkan string yang ingin anda masukkan ke array .. ')
        my_arr.extend(userInpAdd.split())
        print(my_arr)

    elif userConfirm == '2':
        userInpRemove = input('masukkan string array yang ingin kamu hapus .. ')

        if userInpRemove in my_arr:
            my_arr.remove(userInpRemove)
            print(my_arr)
        else:
            print('tidak ada dalam array')

    else:
        print('tidak ada dalam pilihan')

    rep = input('ulang? y/n .. ').lower()
print('aborted.')