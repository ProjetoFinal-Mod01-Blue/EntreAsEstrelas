# -------------------------------- Libs -------------------------------------
from ast import increment_lineno
from time import sleep #Biblioteca para efeitos de transição
from tqdm import tqdm # Biblioteca para barra de progresso
from os import system
import pygame # Biblioteca para uso de efeitos sonoros
import os
#---------------------------------- Funções ----------------------------------
from function import leiaint #Função para ler apenas números inteiros
from function import encerrar #Função para encerrar o jogo
# pygame.mixer.init() #Funçao pra iniciar efeitos sonoros
#----------------------------------- Classes -----------------------------------
from classe1 import Nave

fimDeJogo = 0

# system("cls")
# ------------------------------- Programa Principal -------------------------
if(__name__ == "__main__"):
    system("cls")
    print('''
        --------------------------------------------------------------------------------------------------
                            ____ ___  ____ ____ ____    _  _ _ ____ ____ _ ____ _  _ 
                            [__  |__] |__| |    |___    |\/| | [__  [__  | |  | |\ | 
                            ___] |    |  | |___ |___    |  | | ___] ___] | |__| | \|
        ---------------------------------------------------------------------------------------------------                            
''')
    # print('''
    # 1 - Start
    # ''')
    # play = leiaint('Aperte 1 para começar: ')
    # # if play == 2:
    # #     quit()
    # if play == 1:
    for p in tqdm(range(100)):
        sleep(0.001)
    sleep(4)
    system("cls")
    hist1 =['Durante um período de escassez de alimentos', 'cientistas descobrem que a Terra tem uma data concreta para acabar em...', '20 anos!!!']
    for c in hist1:
        print(c)
        sleep(3)

    system("cls")

    hist2 = ['Um piloto decide deixar sua filha de apenas 10 anos', 'para se arriscar em uma viagem através do universo','juntamente com 3 cientistas para identificar um planeta similar à Terra.']
    for c in hist2:
        print(c)    
        sleep(3)

    system("cls")

    hist3 = ['Sua viagem só é possível através de um BURACO DE MINHOCA !','O percurso durará 1 ano e nessa nova galáxia você encontrará 3 planetas promissores.','Na nave teremos 4 tripulantes. Você e 3 cientistas.']
    for c in hist3:
        print(c)
        sleep(3)

    system("cls")
    hist4 = ['Você terá que decidir entre seguir o Plano A : Encotrar um planeta colonizável e buscar os sobreviventes na Terra.', 'Ou Plano B: Caso algo dê errado e seu retorno não seja possível, sua nave está transportando embriões humanos para a criação de uma nova sociedade.']
    for c in hist4:
        print(c)
        sleep(3)

    print("Você agora é este piloto e deve escolher as ações corretas para SALVAR A HUMANIDADE !")
    sleep(2)
    piloto = str(input("Digite seu nome para continuar: ")).title()

    system("cls")

    nave = Nave(2021, 100, "Terra", "", "Via Láctea", "Estável")
    lancarNave = str(input(f"\nVamos lançar nossa nave, {piloto}? [S/N]: ")).upper().strip()[0]

    if lancarNave == "S":
        print("Lançamento em: ")
        for c in range(5 , 0, -1):
            print(c)
            sleep(1)
        print('''
                    .   
                   .'.
                   |o|
                  .'o'.
                  |.-.|
                  '   '
                   ( )
                    )
                   ( )

               ____
          .-'""p 8o""`-.
       .-'8888P'Y.`Y[ ' `-.
     ,']88888b.J8oo_      '`.
   ,' ,88888888888["        Y`.
  /   8888888888P            Y8'
 /    Y8888888P'             ]88'
:     `Y88'   P              `888:
:       Y8.oP '- >            Y88:
|          `Yb  __             `'|
:            `'d8888bo.          :
:             d88888888ooo.      ;
 \            Y88888888888P     /
  \            `Y88888888P     /
   `.            d88888P'    ,'
     `.          888PP'    ,'
       `-.      d8P'    ,-'   
          `-.,,_'__,,.-'


''')
        sleep(6)
        system("cls")
        print("\nVocê está no espaço! Se dirigindo ao buraco de minhoca!")

        print('''
________________________________         
     /                                "-_          
    /      .  |  .                       \          
   /      : \ | / :                       \         
  /        '-___-'                         \      
 /_________________________________________ \      
     _______| |________________________--""-L 
    /       F J                              \ 
   /       F   J                              L
  /      :'     ':                            F
 /        '-___-'                            / 
/_________________________________________--"        
        ''')
        

        sleep(10)
    
        print("Você atravessou o buraco de minhoca!")
        sleep(2)
        system("cls")
    #     print(f"\nO ano atual é 2021 e sua nave está transportando embriões \
    # humanos para caso a volta não seja possível.")
    #     sleep(3)

        print(nave)
        sleep(2)

        
        nave.mudaGalaxia()
        print(nave)
        sleep(2)

    # nave.chamaMenu()
    # escolhaPlaneta = int(input("Digite sua opção: "))

    while fimDeJogo != 1:

        nave.chamaMenu()
        escolhaPlaneta = leiaint('Digite a opção: ')
        nave.efeitoRandom()
        nave.viajarEntrePlanetas(escolhaPlaneta)
        print(nave)
        sleep(2)

    else:
        print("Você agiu conforme seu coração mandou e desistiu de sua missão.Lançamento cancelado! E você viverá o resto de seus dias ao lado de sua família até que chegue o FIM DA HUMANIDADE !")

    # pygame.init()
    # if os.path.exists('David_Bowie_-_Starman-192k.mp3'):
    #   pygame.mixer.music.load('David_Bowie_-_Starman-192k.mp3')
    #   pygame.mixer.music.play()
    #   pygame.mixer.music.set_volume(1)

    #   clock = pygame.time.Clock()
    #   clock.tick(10)

        #   while pygame.mixer.music.get_busy():
        #      pygame.event.poll()
        #      clock.tick(10)
        # else:
        #   print('O arquivo musica.mp3 não está no diretório do script Python')