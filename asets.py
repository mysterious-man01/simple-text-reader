def color(msg, color='preset', background='preset', end='\n'):
    colors = {'preset': '', 'red': '31', 'green': '32',
              'yellow': '33', 'blue': '34', 'purple': '35',
              'whiteblue': '36', 'grey': '37'}

    background_color = {'preset': '', 'red': '41', 'green': '42',
                        'yellow': '43', 'blue': '44', 'purple': '45',
                        'whiteblue': '46', 'grey': '47', 'white': '40'}
    c = ''
    i = 0
    if color != 'preset' and background != 'preset': c = ';'
    if background == 'white': i = 7

    if color not in colors:
        print(f'\033[31mErro: {color} não existe\033[m')
    elif background not in background_color:
        print(f'\033[31mErro: {background} não existe\033[m')
    else:
        print(f'\033[{i};{colors[color]}{c}{background_color[background]}m', end='')
        print(f'{msg}\033[m', end=end)


def menu(lista, msg='Opções'):
    print('*' * 30)
    print(f'{msg:^30}')
    print('*' * 30)
    for item in enumerate(lista):
        color(f'{item[0]} -- ', 'yellow', end=''), color(f'{item[1]}', 'blue')
    print('*' * 30)
    while True:
        try:
            shell = int(input('>'))
        except (Exception, TypeError, ValueError) as erro:
            color(f'Tipo de erro: {erro.__class__}', 'red')
            color(f'ERRO: O valor informado não é um número', 'red')
        else:
            if 0 <= shell < len(lista): return shell
            color(f'"{shell}" não é uma opção válida...', 'red')


def docgenerete(name='.'):
    try:
        doc = open(f'{name}.txt', 'wt+')
        doc.close()
    except:
        color('Ouve um erro durante a criação do arquivo', 'red')
    else: color('Arquivo criado com sucesso', 'green')


def docfreq(lista, ex='.txt'):
    arqs = list()
    for item in lista:
        if ex in item:
            arqs.append(item)
    return arqs
