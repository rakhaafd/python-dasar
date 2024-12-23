# soal 1
# fruits = {'apple': 3, 'banana': 5, 'cherry': 7, 'date': 2}

# print(fruits.keys()) # mengambil keys
# print(fruits.get('mango', None))


# soal 2
students_scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92}

print(students_scores.values())

def above_80 (x):
    diatas80 = []
    for x in students_scores.values():
        if x > 80:
            diatas80.append(x)
    return diatas80

result = above_80(students_scores)
print(result)



# for x, y in students_scores.items():
#     if y > 80:
#         print(y)


# soal 3
person_info = {'name': 'Rakha', 'age': 17, 'city': 'Semarang'}

print(person_info.items())
for x, y in person_info.items():
    print('Key:', x, 'Value:', y)


# soal 4
inventory = {'pens': 10, 'notebooks': 5, 'erasers': 7, 'markers': 3}

add = inventory['rulers'] = '6'
del inventory['markers']
print(inventory)


# soal 5
employees = {'John': 5000, 'Jane': 6000, 'Doe': 4500, 'Alice': 7000}

l = [inilist for inilist in employees.keys()]
print(l)

allval = sum(employees.values())
print(allval)

for x, y in employees.items():
    if y > 5000:
        print(x, y)