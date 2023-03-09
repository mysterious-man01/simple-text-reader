from os import listdir
import asets
from time import sleep

docname = ''
while True:
    # Menu principal
    shell = asets.menu(['Ver documento', 'Editar documento', 'Sair do programa'])
    sleep(0.3)

    # Opção 2: sair do programa
    if shell == 2: break

    # Opção 0: ler arquivos no diretório do programa
    elif shell == 0:
        diretorio = listdir()
        arq = asets.docfreq(diretorio)
        if len(arq) >= 1:
            arq.append('Voltar')
            posi = asets.menu(arq, 'Escolha uma opção:')
            docname = arq[posi]
            sleep(0.3)
        if docname in diretorio:
            doc = open(docname, 'rt')
            asets.color(doc.read(), background='white')
            doc.close()
            input('Aperte ENTER para continuar...')

    # Opção 1: Abrir arquivo para adicionar conteudo
    elif shell == 1:
        diretorio = listdir()
        arq = asets.docfreq(diretorio)
        if len(arq) >= 1:
            arq.append('Não usar documento existente')
            posi = asets.menu(arq, 'Escolha uma opção:')
            docname = arq[posi]
            sleep(0.3)
        if docname in diretorio:
            doc = open(docname, 'a')
            text = input('>')
            doc.write(f'{text}\n')
            doc.close()
            asets.color('Documento atualizado com sucesso', 'green')
            sleep(0.2)
        else:
            asets.color('O arquivo de cadastro não foi encontrado...', 'yellow')
            while True:
                shell = input('Deseja criar o arquivo de cadastro?(s/n):\n>').strip().lower()[0]
                if shell == 'n': break
                elif shell == 's':
                    arqname = input('Nome do arquivo: ')
                    if arqname not in diretorio:
                        while True:
                            asets.color('Um arquivo de mesmo nome foi encontrado.\ndeseja substituir?(s/n):')
                            shell = input('>').strip().lower()[0]
                            if shell == 'n': break
                            if shell == 's':
                                asets.docgenerete(arqname)
                            asets.color('Comando inválido...', 'red')
                    else: asets.docgenerete(arqname)
                    sleep(0.2)
                    break
                asets.color('Comando inválido...', 'red')
