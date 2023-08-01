#Jessie
#car picker


import random
from PIL import Image

lst = ['car','truck','motorcycle','suv']

random_choice = random.choice(lst)

print('The vehicle you picked is a ' + (random_choice))


if random_choice == 'car':
    print('🚗')
    myImage = Image.open('caro.jpg');
    myImage.show();
elif random_choice == 'suv':
    print('🚙')
    myImage = Image.open('suv.jpg');
    myImage.show();
elif random_choice == 'truck':
    print('🚚')
    myImage = Image.open('truck.jpg');
    myImage.show();
elif random_choice == 'motorcycle':
    print('🏍')
    myImage = Image.open('greenbike.png');
    myImage.show();
