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
    t = 'ESTACA'
    print(f'{t:39}4')
    c = 'CALCULO'
    print(f'{c:39}5')
    f = 'FECHAR PROGRAMA'
    print(f'{f:39}6')
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
    global d, p
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
    global solo
    solo = []
    for i in range(len(prof)):
        s = int(input(f'Qual o tipo de solo á {i+1} m: '))
        solo.append(tables.dados_Solo[s])


def tipo():
    titulo('Tipo de Estaca')
    estacas = [['Franki', 2.5, 5], ['Metálica', 1.75, 3.5], ['Pré-moldada', 1+d/(0.8*100), 2*1+d/(0.8*100)], ['Escavada', 3, 6], ['Raiz, Helíce Continua e Ômega', 2, 4]]
    n = 0
    for i in estacas:
        print(f'{i[0]:39}{n}')
        n += 1
    print('-='*20)
    global tipo_estaca
    tipo_estaca = estacas[int(input('Qual estaca você deseja usar? '))]
    return tipo_estaca


def calculo():
    print(f'Lista de SPT {prof}')
    print(f'Diâmetro da estaca {d} e perimetro da estaca {p}')
    print(f'Lista de solos {solo}')
    print(f'Tipo de estaca {tipo_estaca}')
    