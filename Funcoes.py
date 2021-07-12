# ---------------------------------- Libs  ------------------------------------------
from time import sleep


# ---------------------------------- Funções -----------------------------------------
# Função para o programa aceitar apenas números inteiros 
def leiaint(msg):
    valido = False
    valor = 0
    while True:
        escolha = str(input(msg))
        if escolha.isnumeric():
            valor = int(escolha)
            valido = True
        else:
            print('ERRO! Digite apenas números.')
        if valido:
            break
    return valor

# Função para encerrar o programa
def encerrar():
    resp = ''
    while True:
        resp = str(input('Deseja encerrar o jogo ? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
    if resp == 'S':
        quit()
    else:
        pass
    return resp

# Função de eventos aleatórios
def aleatorio():
    import random
    # declarando variável vida que tem haver com o tanto de vida terrestre
    vida = 20 # Utilizar a class Tempo, foi dado um valor fixo para teste
    case1 = 'Pane elétrica. Nave fica à deriva e consome 2 anos de vida terrestre.'
    case2 = 'Seu traje espacial foi despressurizado. Você não pode desembarcar da aeronave e consome 1 ano de vida terrestre.'

    cases = [case1,case2]
    sorteio = random.choice(cases)

    # Para o cálculo de perda de anos funcione corretamente, é necessário que a função tenha um laço, caso contrário não ocorre subtração de tempo de vida na terra. 
    if sorteio == case1:
        vida -= 2
    elif sorteio == case2:
        vida -= 1

    print()
    sleep(1)
    print(sorteio)
    print()
    sleep(1)
    print(f'Agora você possui {vida} anos de vida terrestre. Use-os com sabedoria para conseguir salvar a humanidade.')

# Função com informações dos planetas, esta função deve ser chamada dentro do menu do jogo
def informacao():
    while True:
        print('Selecione o número indicado para ver as informações de cada planeta.')
        sleep(1)
        print('''
        1 - Biós
        2 - Agnostos 
        3 - Matér
        0 - Voltar ao Menu
        ''')
        sleep(1)
        escolha = leiaint('Digite a opção desejada: ')
        if escolha < 0  or escolha > 3: # Prevenção de erro
            print('Opção inválida !')
            informacao()
        elif escolha == 1:
            print('''
            Nome: Biós
            Nível de Oxigênio : 0
            Estado: Desconhecido
            Condições de vida : Não habitável
            Combustivel: -10%
            Percurso: -2 anos de vida terrestre.
            ''')
            sleep(5)
        elif escolha == 2:
            print('''
            Nome: Agnostos
            Nível de Oxigênio : 0
            Estado: Coberto por água.
            Condições de vida : Não habitável
            Combustivel: -70%
            Percurso: -3 anos de vida terrestre.
            ''')
            sleep(5)
        elif escolha == 3:
            print('''
            Nome: Matér
            Nível de Oxigênio : 21%
            Estado: Planeta  similar a Terra
            Condições de vida : Habitável
            Combustivel: -20%
            Percurso: -14 anos de vida terrestre.
            ''')
            sleep(5)
        elif escolha == 0:
            menu()
            break
# Função menu
def menu():
    print('''
    O que vamos fazer agora ?
    1 - Decolar 
    2 - Informações de Planetas
    3 - Explorar novos Planetas
    ''')


# Função de escolha de planetas.
# def escolhePlaneta():

# --------------------------------- Programa Principal(Para teste) ---------------------------------------
for c in range(1):
    print('*** Seja bem-vindo(a) ao Interestelar ***')
    sleep(1)
    print()
    nome = str(input('Digite seu nome para continuar: ')).title()
    print(f'Olá comadante {nome} !')
    sleep(1)
    print()
    print('Me chamo Tars, e vou guiá-lo nesta jornada para salvar o planeta Terra !')
    sleep(1)
    print()
    encerrar()
    print('Cheguei aqui')
    informacao()
# aleatorio()

