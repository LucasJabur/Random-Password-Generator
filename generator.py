import math
import numpy as np
import random
import string

num = string.digits
str = string.ascii_letters
spec = string.punctuation

menu_options = {
    1: "Generate a password just with letters.\n",
    2: "Generate a password just with numbers.\n",
    3: "Generate a password just with special characteres.\n",
    4: "Generate a password with letters and numbers.\n",
    5: "Generate a password with letters and special characteres.\n",
    6: "Generate a password with numbers and special characteres.\n",
    7: "Generate a password with letters, numbers and special characteres\n",
    8: 'Exit\n'
}

def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )

def option_1():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = int(input(f'How many characteres do you want on your password? '))
    for i in range(pwd):
        gen = (''.join(random.choice(str) for ii in range(Lpwd))) 
        print(f'\nYour password is: {gen}\n')

def option_2():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = int(input(f'How many characteres do you want on your password? '))
    for i in range(pwd):
        gen = (''.join(random.choice(num) for ii in range(Lpwd))) 
        print(f'\nYour password is: {gen}\n')

def option_3():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = int(input(f'How many characteres do you want on your password? '))
    for i in range(pwd):
        gen = (''.join(random.choice(spec) for ii in range(Lpwd))) 
        print(f'\nYour password is: {gen}\n')

def option_4():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = float(input(f'How many characteres do you want on your password? '))
    nLpwd = Lpwd/2
    down_Lpwd = math.floor(nLpwd)
    up_Lpwd = math.ceil(nLpwd)
    for i in range(pwd):
        gen1 = (''.join(random.choice(str) for ii in range(up_Lpwd)))
        gen2 = (''.join(random.choice(num) for ii in range(down_Lpwd)))
        genF = list(gen1 + gen2)
        random.shuffle(genF)
        gen = "".join(genF)
        print(f'\nYour password is: {gen}\n')

def option_5():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = float(input(f'How many characteres do you want on your password? '))
    nLpwd = Lpwd/2
    down_Lpwd = math.floor(nLpwd)
    up_Lpwd = math.ceil(nLpwd)
    for i in range(pwd):
        gen1 = (''.join(random.choice(str) for ii in range(up_Lpwd)))
        gen2 = (''.join(random.choice(spec) for ii in range(down_Lpwd)))
        genF = list(gen1 + gen2)
        random.shuffle(genF)
        gen = "".join(genF)
        print(f'\nYour password is: {gen}\n')

def option_6():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = float(input(f'How many characteres do you want on your password? '))
    nLpwd = Lpwd/2
    down_Lpwd = math.floor(nLpwd)
    up_Lpwd = math.ceil(nLpwd)
    for i in range(pwd):
        gen1 = (''.join(random.choice(num) for ii in range(up_Lpwd)))
        gen2 = (''.join(random.choice(spec) for ii in range(down_Lpwd)))
        genF = list(gen1 + gen2)
        random.shuffle(genF)
        gen = "".join(genF)
        print(f'\nYour password is: {gen}\n')

def option_7():
    pwd = int(input(f'How many passwords do you wanna generate? '))
    Lpwd = float(input(f'How many characteres do you want on your password? '))
    nLpwd = Lpwd/3
    if nLpwd > 5:
        down_Lpwd = math.floor(nLpwd)
        up_Lpwd = math.ceil(nLpwd)
        for i in range(pwd):
            gen1 = (''.join(random.choice(str) for ii in range(up_Lpwd)))
            gen2 = (''.join(random.choice(num) for ii in range(down_Lpwd)))
            gen3 = (''.join(random.choice(spec) for ii in range(down_Lpwd)))
            genF = list(gen1 + gen2 + gen3)
            random.shuffle(genF)
            gen = "".join(genF)
            print(f'\nYour password is: {gen}\n')
    else:
        down_Lpwd = math.floor(nLpwd)
        up_Lpwd = math.ceil(nLpwd)
        for i in range(pwd):
            gen1 = (''.join(random.choice(str) for ii in range(up_Lpwd)))
            gen2 = (''.join(random.choice(num) for ii in range(up_Lpwd)))
            gen3 = (''.join(random.choice(spec) for ii in range(down_Lpwd)))
            genF = list(gen1 + gen2 + gen3)
            random.shuffle(genF)
            gen = "".join(genF)
            print(f'\nYour password is: {gen}\n')

while True:
    if __name__ == '__main__':
        while(True):
            print_menu()
            option = ''
            try:
                option = int(input('What do you desire: '))
            except:
                print('Wrong input. Please enter a number...')
            if option == 1:
                option_1()
            elif option == 2:
                option_2()
            elif option == 3:
                option_3()
            elif option == 4:
                option_4()
            elif option == 5:
                option_5()
            elif option == 6:
                option_6()
            elif option == 7:
                option_7()
            elif option == 8:
                print('Exiting...')
                exit()
            else:
                print('Invalid option. Please choose a correct option.')
