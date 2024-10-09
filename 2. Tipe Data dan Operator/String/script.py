print('fuck ' + 'you ' + 'motherfucker')
# print('python ' * str(10)) # error
print('*' * 50)
print(str(100) * 10)

# string indexing
print('hello world' [-1]) # dari belakang

# function split
teks = 'halo, nama saya, rakha'
x = teks.split(',')
print(x) # ['halo', ' nama saya', ' rakha']

# function islower (cek apakah dalam element string adalah huruf kecil)
a = 'hello'
b = 'HELLO'
print(a.islower(), b.islower()) # True False

# function isupper (cek apakah dalam element string adalah huruf besar)

# function count (digunakan untuk menghitung berapa kali sebuah value muncul dalam sebuah string)
teks = "Halo semuanya, disini saya bersama dengan rakha semuanya"
x = teks.count("semuanya")
print(x) # 2