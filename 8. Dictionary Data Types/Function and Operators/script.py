#len operators
person = {'name' : 'rakha', 
          'age' : '17',
          'hobby' : 'code'}
person['class'] = 'XI SIJA 1'
person['class'] = 'XI TKJ 1'

print(len(person)) #4
print(person)

#in operators 
print('job' in person) # false
print('hobby' in person) # true