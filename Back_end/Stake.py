import mods
import os
from time import sleep

while True:
    r = mods.menu()
    if r == '1':
        mods.spt()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '2':
        mods.diametro()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '3':
        mods.solos()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '4':
        tipo = mods.tipo()
        os.system('cls' if os.name == 'nt' else 'clear')
    elif r == '5':
        mods.calculo()
    elif r == '6':
        break
    else:
        r = input('Escolha uma opção: ')
    sleep(2)