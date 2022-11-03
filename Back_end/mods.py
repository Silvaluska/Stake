# Funções do programa


from pickle import GLOBAL


def titulo(nome):
    print('+','-'*40,'+', sep='')
    print('|',f'{nome:^40}','|', sep='')
    print('+','-'*40,'+', sep='')


def menu_item(nome, item):
    print('|',f'{nome:39}{item}','|', sep='')


def menu():
    titulo('STAKE PROGRAM')
    menu_item('SPT', 1)
    menu_item('DIÂMETRO DA ESTACA', 2)
    menu_item('SOLOS', 3)
    menu_item('ESTACA', 4)
    menu_item('CALCULO', 5)
    menu_item('FECHAR PROGRAMA', 6)
    print('+','-'*40,'+', sep='')
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
    global d, p, a
    d = int(input('Qual Diamêtro da estaca (cm): '))
    p = pi*d/100
    a = pi*((d/100)**2)/4


def solos():
    titulo('SOLOS')
    import tables
    titulo('Lista com tipos de solo')
    n = 0
    for i in tables.dados_Solo:
        print('|',f'{i[0]:38}{n:>2}','|',sep='')
        n += 1
    titulo('Dados do solo')
    global solo
    solo = []
    for i in range(len(prof)):
        s = int(input(f'Qual o tipo de solo á {i+1} m: '))
        solo.append(tables.dados_Solo[s])


def tipo():
    titulo('Tipo de Estaca')
    estacas = [['Franki', 2.5, 5], ['Metálica', 1.75, 3.5], ['Pré-moldada', 1+d/(0.8*100), 2*(1+d/(0.8*100))], ['Escavada', 3, 6], ['Raiz, Helíce Continua e Ômega', 2, 4]]
    n = 0
    for i in estacas:
        print('|',f'{i[0]:39}{n}','|',sep='')
        n += 1
    print('+','-'*40,'+',sep='')
    global tipo_estaca
    tipo_estaca = estacas[int(input('Qual estaca você deseja usar? '))]
    return tipo_estaca


def calculo():
    r_Lateral = 0
    for i in range(len(prof)):
        alpha = solo[i][2]
        k = solo[i][1]
        spt = prof[i]
        deltaL = 1
        u = p
        f2 = tipo_estaca[2]
        r_Lateral += (alpha*k*spt*deltaL*u*10)/f2
    r_ponta = solo[-1][1] * 1000 * prof[-1] * a / tipo_estaca[1]
    r_total = r_Lateral + r_ponta
    print(f'Resistência da estaca: {r_total:.2f} kN')

