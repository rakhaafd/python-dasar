# Dalam tipe data set, terdapat istilah superset dan juga subset yang berarti:

# Sebuah set dapat dikatakan superset apabila mengandung semua elemen dari set yang lain.

# Dan sebuah set dapat dikatakan subset apabila seluruh elemen terkandung dari set yang lain.

A = {1,2}
B = {1,2,3}

# A adalah subset dari B karena semua elemen A terkandung dalam B.
# B merupakan superset dari A karena B mengandung seluruh elemen dari A.

s1 = {1, 2, 3, 4, 5}
s2 = {1, 2, 3}
s3 = {1, 2, 6}

print(s2.issubset(s1)) #true
print(s3.issubset(s1)) #false
print(s1.issuperset(s2)) # true
print(s1.issuperset(s3)) #false