# Funções do programa
from cmath import pi


def titulo(nome):
    print('-='*20)
    print(f'{nome:^40}')
    print('-='*20)


# Dados do solo
dados_Solo = [['Areia', 1, 1.4], ['Areia Siltosa', 0.8, 2], ['Areia Siltoargilosa', 0.7, 2.4], ['Areia Argilosa', 0.6, 3], ['Areia Argilosiltosa', 0.5, 2.8], ['Silte', 0.4, 3], ['Silte Arenoso', 0.55, 2.2], ['Silte Arenoargiloso', 0.45, 2.8], ['Silte Argiloso', 0.23, 3.4], ['Silte Argiloarenoso', 0.25, 3], ['Argila', 0.2, 6], ['Argila Arenosa', 0.35, 2.4], ['Argila Arenossiltosa', 0.3, 2.8], ['Argila Siltosa', 0.22, 4], ['Argila Siltoarenosa', 0.33, 3]]

# Inicio do programa
titulo('Stake')

# Pedindo para o Usuário Inserir os valores de SPT
prof = []
n = 1
while True:
    spt = float(input(f'Digite o SPT á {n} m: '))
    if spt == 999:
        break
    prof.append(spt)
    n += 1
print('Dados do SPT Salvos!')

# Pedindo para o Usuário inserir o diametro da estaca
titulo('Tipo de estaca')
d = int(input('Qual Diamêtro da estaca (cm): '))
p = pi*d/100
print(p)

tipo = [['Franki', 2.5, 5], ['Metálica', 1.75, 3.5], ['Pré-moldada', 1+d/(0.8*100), 2*1+d/(0.8*100)], ['Escavada', 3, 6], ['Raiz, Helíce Continua e Ômega', 2, 4]]

# Pedindo para o usuário inserir os tipos de solo em cada profundidade
titulo('Lista com tipos de solo')
n = 0
for i in dados_Solo:
    print(f'{i[0]:30}{n}')
    n += 1

titulo('Dados do solo')
solo = []
for i in range(len(prof)):
    s = int(input(f'Qual o tipo de solo á {i+1} m: '))
    solo.append(dados_Solo[s])


r_Ponta = r_Lateral = 0
r_Total = r_Lateral + r_Ponta