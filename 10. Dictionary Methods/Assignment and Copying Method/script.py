# copy
dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
cp_dic = dic.copy()
print(dic is cp_dic) # cek apakah kedua dictionary merupakan objek yang sama
print(dic == cp_dic) #cek apakah key-value pairnya sama


# deep copy
x = {'a': {'python':'2.7'},'b':{'python':'3.6'}}
# y = x.copy()

# y['a']['python'] == '2.7.15' #jika copy biasa, tidak bisa melakukan ini,
# print(x)
# print(y)


import copy
y = copy.deepcopy(x)

y['a']['python'] = 'HTML5'
print(y)
print(x)
print(x is y)
print(x == y)

#kita bisa merubah value dari dictionary y dan value dalam dictionary x tidak berubah.