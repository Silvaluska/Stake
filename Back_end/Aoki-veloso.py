import mods
import os

while True:
    r = mods.menu()
    if r == '1':
        mods.spt()
    elif r == '2':
        mods.diametro()
    elif r == '3':
        mods.solos()
    elif r == '4':
        break
    else:
        r = input('Escolha uma opção: ')
    os.system('cls' if os.name == 'nt' else 'clear')

'''

tipo = [['Franki', 2.5, 5], ['Metálica', 1.75, 3.5], ['Pré-moldada', 1+d/(0.8*100), 2*1+d/(0.8*100)], ['Escavada', 3, 6], ['Raiz, Helíce Continua e Ômega', 2, 4]]

# Pedindo para o usuário inserir os tipos de solo em cada profundidade



r_Ponta = r_Lateral = 0
r_Total = r_Lateral + r_Ponta'''