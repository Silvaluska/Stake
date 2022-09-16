import mods
import os
from time import sleep

while True:
    r = mods.menu()
    if r == '1':
        mods.spt()
    elif r == '2':
        mods.diametro()
    elif r == '3':
        mods.solos()
    elif r == '4':
        tipo = mods.tipo()
    elif r == '5':
        mods.calculo()
    elif r == '6':
        break
    else:
        r = input('Escolha uma opção: ')
    sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

'''

tipo = 

# Pedindo para o usuário inserir os tipos de solo em cada profundidade



r_Ponta = r_Lateral = 0
r_Total = r_Lateral + r_Ponta'''