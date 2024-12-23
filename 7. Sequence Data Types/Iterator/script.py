list1 = [11,22,33,44] * 2
print(list1)

# #output
# [11,22,33,44,11,22,33,44]

tup1 = (1,2,3)
print(tup1 * 2)

#output
# (1,2,3,1,2,3)

str2 = 'hello'
print(str2 * 3)

# #output
# hellohellohello


ran = list(range(5)) * 3
print(ran)

#output
# [0,1,2,3,4,0,1,2,3,4,0,1,2,3,4]

ran = tuple(range(5)) * 3
print(ran)

#output
# (0,1,2,3,4,0,1,2,3,4,0,1,2,3,4)