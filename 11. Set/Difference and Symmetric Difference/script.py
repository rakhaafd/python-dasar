# & untuk intersection
# | untuk union
# - untuk difference of set dan,
# ^ untuk symmetric difference

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

print(s1 - s2) # - untuk difference, berarti mengambil data yang HANYA ADA DI S1 ATAU S2. misal s2 - s1 berarti mengambil data yang ada di s2, dan tidak ada di s1.


print(s1 ^ s2) # ^ untuk symmetric difference, berarti mengambil bilangan yang tidak bertabrakan, yang artinya mengambil data yang hanya di s1 dan s2. menghiraukan yang bertabrakan

print(s2 ^ s1) #sama