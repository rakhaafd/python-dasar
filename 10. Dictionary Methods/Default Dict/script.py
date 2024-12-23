from collections import defaultdict

dic = {'a': 10,'b': 20,'c': 30, 'd': 40}
# print(dic['z'])  # tidak bisa
dic2 = dic.fromkeys(dic, 100) #membuat dictionary baru dengan 100 sebagai valuenya.
dic2 = defaultdict(int) #Fungsi int() mengembalikan nilai 0 jika key yang diakses belum ada dalam dictionary.

print(dic2['z'])


# soal 2
product_prices = {'apple': 2.5, 'banana': 1.2, 'cherry': 3.0}

default = dict.fromkeys(product_prices, 100)
default = defaultdict(float)
print(default['orange'])


# Membuat defaultdict dengan default factory int (0)
purchase_count = defaultdict(int)

purchase_count['apple'] += 1
purchase_count['banana'] += 2
purchase_count['orange'] += 2

print(purchase_count['grapes'])
for x, y in purchase_count.items():
    print(x, y)


scores = {'John': 70, 'Sara': 85, 'Mia': 90}

dic_baru = dict.fromkeys(scores, 50)
print(dic_baru)

dic_baru['John'] = 80
print(dic_baru)

dic_default = defaultdict(int)
dic_default['John'] += 1

print(dic_default)