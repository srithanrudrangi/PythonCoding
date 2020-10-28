weight = int(input('What amount of mass do you want the weight of?'))
mass = weight*9.8
print(mass)
if mass > 500:
    print('It is too heavy.')
else:
    print('It is too light.')
