weight = float(input('Input your bodyweight in kg: '))
height = float(input('Input your bodyheight in cm: '))

height_m = height / 100

bmi = (weight/(height_m ** 2)) # ** adalah kuadrat
print('Your BMI is: ',bmi)