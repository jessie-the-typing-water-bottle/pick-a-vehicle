#Jessie
#car picker


import random

lst = ['car','truck','motorcycle','suv']

random_choice = random.choice(lst)

print('The vehicle you picked is a ' + (random_choice))


if random_choice == 'car':
    print('🚗')
elif random_choice == 'suv':
    print('🚙')
elif random_choice == 'truck':
    print('🚚')
elif random_choice == 'motorcycle':
    print('🏍')
