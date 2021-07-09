# -------------------------------- Libs -------------------------------------
from time import sleep #Biblioteca para efeitos de transição
from tqdm import tqdm # Biblioteca para barra de progresso
from os import system # Biblioteca para utilizar o cls (limpar a tela)
import pygame # Biblioteca para uso de efeitos sonoros
import os # Para verificar o caminho da música
from classe1 import Nave # Importando a classe Nave do arquivo classe1.py
from functions import cabecalho, galaxiaAtual, galaxiaNova # Importando a função que exibe o cabeçalho
from functions import fimgame # Importando a função que exibe o Game Over

# ------------------------- Variáveis inicializadas --------------------------
piloto = "John Doe"
fimDeJogo = 0

# ------------------------------- Programa Principal -------------------------
if(__name__ == "__main__"): # Só executa o código abaixo se ele estiver no arquivo de nome __main__

    system("cls")      # Limpa o a tela do terminal
    cabecalho()        # Exibe o cabeçalho

    for p in tqdm(range(100), ncols=85):          # Barra de carregamento da biblioteca tqdm
        sleep(0.001)
    sleep(4)

    system("cls")
    cabecalho()

    # Listas com texto introdutório
    hist1 =['Durante um período de escassez de alimentos\n', 'cientistas descobrem que a Terra tem uma data concreta para acabar em...\n', '20 anos!!!']
    for c in hist1:       # imprime cada item da lista
        print(f'{c: ^90}')
        sleep(5)        

    system("cls")
    cabecalho()

    hist2 = ['Um piloto decide deixar sua filha de apenas 10 anos\n', 'para se arriscar em uma viagem através do universo\n','juntamente com 3 cientistas para identificar um planeta similar à Terra.']
    for c in hist2:
        print(f'{c: ^90}')    
        sleep(5)

    system("cls")
    cabecalho()

    hist3 = ['Sua viagem só é possível através de um BURACO DE MINHOCA !\n','O percurso durará 1 ano e nessa nova galáxia você encontrará 3 planetas promissores.\n','Na nave teremos 4 tripulantes. Você e 3 cientistas.\n']
    for c in hist3:
        print(f'{c: ^90}')
        sleep(5)

    system("cls")
    cabecalho()

    hist4 = ['Você terá que decidir entre seguir o\n', 'Plano A: Encontrar um planeta colonizável e buscar os sobreviventes\n', 'na Terra.\n', 'Ou Plano B: Caso algo dê errado e seu retorno não seja possível\n', 'Sua nave está transportando embriões humanos para a criação de\n','uma nova sociedade.\n']
    for c in hist4:
        print(f'{c: ^90}')
        sleep(5)

    # Nome do piloto-comandante
    print("Você agora é este piloto e deve escolher as ações corretas para SALVAR A HUMANIDADE !\n")
    sleep(3)
    piloto = str(input("                     Digite seu nome, Comandante:   ")).title()

    system("cls")
    cabecalho()

    nave = Nave(2021, 100, "Terra", "Via Láctea", "Estável", 1) # Instanciando nave na classe Nave

    # Pergunta se o usuário quer lançar a nave
    lancarNave = str(input(f"                 Vamos lançar nossa nave, {piloto}? [S/N]: ")).upper().strip()[0]

    # Enquanto a resposta de lancarNave for diferente de S ou N continua perguntando
    while lancarNave not in 'SN':
        lancarNave = str(input(f"                 Vamos lançar nossa nave, {piloto}? [S/N]: ")).upper().strip()[0]
    
    # Se lancarNave for igual a S, executa:
    if lancarNave == "S":
        print(f"{'Lançamento em: ': ^90}")       # Contagem regressiva de 5 até 1
        for c in range(5 , 0, -1):
            print(f'{c: ^90}')
            sleep(1)

        system("cls")
        galaxiaAtual() # Exibe a imagem do foguete saindo da Terra e indo em direção ao buraco de minhoca
        sleep(3)
        
        print(f"{'Se dirigindo ao buraco de minhoca!': ^90}")
        sleep(5)
        system("cls")
        print(nave) # Exibe as informações sobre a nave
        sleep(3)
        print(f"\nO ano atual é 2021 e sua nave está transportando embriões \
humanos para caso a volta não seja possível.")
        sleep(4)
        print("Você atravessou o buraco de minhoca!")
        galaxiaNova() # Exibe a imagem da nova galáxia
        sleep(4)
        system("cls")
        cabecalho()
        sleep(3)

        nave.mudaGalaxia() # Chama o método que muda de galáxia
        print(nave)
        sleep(4)


        # Enquanto fimDeJogo for diferente do valor nave.fimJogo executa o código abaixo
        while fimDeJogo != nave.fimJogo: 
            system("cls")
            cabecalho()
            nave.chamaMenu() # Método que exibe o menu dependendo do galáxia ou planeta que o usuário se encontra e recebe a informação do usuário do planeta que se deseja ir
            nave.efeitoRandom() # Efeito randômico que pode gerar conflitos e adicionar anos extras durante os acontecimentos
            nave.viajarEntrePlanetas(nave.escolha) # Método que altera os valores da nave (exemplo: combustível, anos terrestres, etc.) de acordo com a escolha do usuário
            print(nave)
            sleep(8)
    
    # Caso o lancarNave seja N exibe:

    else:
        print("\nVocê agiu conforme seu coração mandou e desistiu de sua missão. Lançamento cancelado! \nVocê viverá o resto de seus dias ao lado de sua família até que chegue o FIM DA HUMANIDADE!")
        sleep(5)
    print(fimgame())

    # Executa o som mp3 no final do código

    pygame.init()
    if os.path.exists('David_Bowie_-_Starman-192k.mp3'):
      pygame.mixer.music.load('David_Bowie_-_Starman-192k.mp3')
      pygame.mixer.music.play()
      pygame.mixer.music.set_volume(1)

      clock = pygame.time.Clock()
      clock.tick(10)

    while pygame.mixer.music.get_busy():
        pygame.event.poll()
        clock.tick(10)
    else:
          print('O arquivo musica.mp3 não está no diretório do script Python')