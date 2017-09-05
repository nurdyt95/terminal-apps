import time
from arithmetic_test import *
import os

os.system("mode con cols=80 lines=25")

print('welcome to nurdys tools')
time.sleep(1)
os.system('cls')

while True:
    choice = print('Choose an application: \n1. Arithmetic Test\n2. Password Generator\n3. TBC')
    choice = str(input())
    if choice == '1':
        print('Arithmetic test')
        time.sleep(1)
        arithmetic_test()
    if choice == '2':
        print('Password Generator')
    if choice == '3':
        print('Text Adventure')
##import os
##hw = os.get_terminal_size()
##print("Height:", hw[1], "Width:", hw[0])


