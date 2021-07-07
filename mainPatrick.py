from ast import increment_lineno
from time import sleep
from os import system
from classe1 import Nave
# import pygame
import os   

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

# system("cls")

# print("Durante um período de escassez de alimentos")
# sleep(2)
# print("cientistas descobrem que a Terra tem uma data concreta para acabar...")
# sleep(2)
# print("20 anos!!!")
# sleep(3)

# system("cls")

# print("Um piloto decide deixar sua filha de apenas 10 anos")
# sleep(2)
# print("para se arriscar em uma viagem através do universo")
# sleep(2)
# print("juntamente com 3 cientistas para identificar um planeta similar à Terra.")
# sleep(2)

# system("cls")
print('''
----------------------------------------------------------------------------
           ____ ___  ____ ____ ____    _  _ _ ____ ____ _ ____ _  _ 
           [__  |__] |__| |    |___    |\/| | [__  [__  | |  | |\ | 
           ___] |    |  | |___ |___    |  | | ___] ___] | |__| | \|
----------------------------------------------------------------------------                             
''')
while True:
    play = input("                   Vamos salvar a humanindade!?!? [Sim/Não]").strip().upper()[0]
    while play not in "SN":
        play = input("                   Vamos salvar a humanindade!?!? [Sim/Não]").strip().upper()[0]

    if play == "S":
        print("---"*25)
        nomePiloto = str(input("Digite seu nome: ")).title()
        print(f'''
        Em um futuro desconhecido.
        Durante um periodo de escasses de alimentos em nosso planeta,
        a humanidade esta proxima do fim.

        {nomePiloto}, vocês é o nosso melhor piloto
        deseja se arriscar em uma viagem para guiar 
        3 cientistas para identificar um planeta habitavel?.

''')
        sleep(8)
        system("cls")
        print('''
----------------------------------------------------------------------------
           ____ ___  ____ ____ ____    _  _ _ ____ ____ _ ____ _  _ 
           [__  |__] |__| |    |___    |\/| | [__  [__  | |  | |\ | 
           ___] |    |  | |___ |___    |  | | ___] ___] | |__| | \|
----------------------------------------------------------------------------                             
''')
        print("Sua viagem só é possível através de um BURACO DE MINHOCA!")
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
        print("Essa viagem durará 1 ano e nessa nova galáxia você terá 3 planetas promissores.")
        sleep(2)
        print("Na nave teremos 4 tripulantes. Você e 3 cientistas.")
        sleep(5)
        system("cls")
        print('''
----------------------------------------------------------------------------
           ____ ___  ____ ____ ____    _  _ _ ____ ____ _ ____ _  _ 
           [__  |__] |__| |    |___    |\/| | [__  [__  | |  | |\ | 
           ___] |    |  | |___ |___    |  | | ___] ___] | |__| | \|
----------------------------------------------------------------------------                             
''')

        nave = Nave(2021, 100, "Terra", "", "Via Láctea", "Estável")
        lancarNave = str(input(f"\nVamos lançar nossa nave Capitão, {nomePiloto}? [S/N]: ")).upper().strip()[0]

        if lancarNave == "S":
            print("Lançamento em: ")
            sleep(1)
            print("3")
            sleep(1)
            print("2")
            sleep(1)
            print("1")
            sleep(1)
            print("\nVocê está no espaço! Se dirigindo ao buraco de minhoca!")
            sleep(2)
            print(f"\nO ano atual é 2021 e sua nave está transportando embriões \nhumanos para caso a volta não seja possível.")
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

            sleep(3)

            print(nave)
            print('''
----------------------------------------------------------------------------
           ____ ___  ____ ____ ____    _  _ _ ____ ____ _ ____ _  _ 
           [__  |__] |__| |    |___    |\/| | [__  [__  | |  | |\ | 
           ___] |    |  | |___ |___    |  | | ___] ___] | |__| | \|
----------------------------------------------------------------------------                             
''')
            sleep(2)

            print("Você atravessou o buraco de minhoca!")

            nave.incrementaAno()
            nave.mudaGalaxia()
            print(nave)
            sleep(2)

            nave.chamaMenu()
            escolhaPlaneta = int(input("Digite sua opção: "))
            nave.viajarEntrePlanetas(escolhaPlaneta)
            nave.efeitoRandom()
            print(nave)
            sleep(2)

            nave.chamaMenu()
            escolhaPlaneta = int(input("Digite sua opção: "))
            nave.viajarEntrePlanetas(escolhaPlaneta)
            nave.efeitoRandom()
            print(nave)
            sleep(2)

            nave.chamaMenu()
            escolhaPlaneta = int(input("Digite sua opção: "))
            nave.viajarEntrePlanetas(escolhaPlaneta)
            nave.efeitoRandom()
            print(nave)
            sleep(2)
    else:
        pass
    if play == "N":
        print('''
----------------------------------------------------------------------------
                  ____ ____ _  _ ____    ____ _  _ ____ ____ 
                  | __ |__| |\/| |___    |  | |  | |___ |__/ 
                  |__] |  | |  | |___    |__|  \/  |___ |  \ 
----------------------------------------------------------------------------                          
''')
        break