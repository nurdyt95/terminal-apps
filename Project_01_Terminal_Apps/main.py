import time
from arithmetic_test import *
import os
import colorama
from colorama import Fore, Back, Style

colorama.init()
os.system("mode con cols=80 lines=25")

def app_selection():
    while True:
        choice = print('Choose an application: \n1. Arithmetic Test\n2. Password Generator\n3. TBC')
        choice = str(input())
        if choice == '1':
            os.system('cls')
            time.sleep(1)
            arithmetic_test()
        if choice == '2':
            print('Password Generator')
        if choice == '3':
            print('Text Adventure')

def login():
    print('\n\n')
    #print(Fore.BLACK + Back.WHITE + 'Login' + Style.RESET_ALL)
    print('{:@^80}'.format('----LOGIN----'))
    #print('{:^90}'.format((Fore.BLACK + Back.WHITE + 'LOGIN' + Style.RESET_ALL)))
    print('\n')
    uname = input('USERNAME: ')
    upass = input('PASSWORD: ')
    print(Fore.GREEN + '\nSuccessful' + Style.RESET_ALL)
    time.sleep(2)
    os.system('cls')
    app_selection()

def splash_screen():
    
    print('\n'*10)
    print('{:^95}'.format((Fore.BLACK + Back.WHITE + 'Project_01_Terminal_Apps' + Style.RESET_ALL)))
    time.sleep(1)
    print('{:^80}'.format('created by nurdy'))
    #print('\n'*11)
    time.sleep(3)
    os.system('cls')
    login()
    
splash_screen()
  

##import os
##hw = os.get_terminal_size()
##print("Height:", hw[1], "Width:", hw[0])
