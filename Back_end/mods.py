# Funções do programa


from pickle import GLOBAL


def titulo(nome):
    print('-='*20)
    print(f'{nome:^40}')
    print('-='*20)


def menu():
    titulo('STAKE PROGRAM')
    spt = 'SPT'
    print(f'{spt:39}1')
    d = 'DIÂMETRO DA ESCATA'
    print(f'{d:39}2')
    s = 'SOLOS'
    print(f'{s:39}3')
    f = 'FECHAR PROGRAMA'
    print(f'{f:39}4')
    print('-='*20)
    r = input('Escolha uma opção: ')
    return r


def spt():
    titulo('SPT')
    global prof
    prof = []
    n = 1
    while True:
        spt = float(input(f'Digite o SPT á {n} m: '))
        if spt == 999:
            break
        prof.append(spt)
        n += 1
    print('Dados do SPT Salvos!')


def diametro():
    titulo('DIÂMETRO')
    from cmath import pi
    d = int(input('Qual Diamêtro da estaca (cm): '))
    p = pi*d/100


def solos():
    titulo('SOLOS')
    import tables
    titulo('Lista com tipos de solo')
    n = 0
    for i in tables.dados_Solo:
        print(f'{i[0]:30}{n}')
        n += 1
    titulo('Dados do solo')
    solo = []
    for i in range(len(prof)):
        s = int(input(f'Qual o tipo de solo á {i+1} m: '))
        solo.append(tables.dados_Solo[s])