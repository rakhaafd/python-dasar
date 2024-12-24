keys = ['a','b','c','d']
x = dict.fromkeys(keys)
print(x)

#output
# {'a':None , 'b': None, 'c': None, 'd': None}

# tuple ver
keys = ('a','b','c','d')
x = dict.fromkeys(keys, 20)
print(x)

#output
# {'a':None , 'b': None, 'c': None, 'd': None}