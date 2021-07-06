from ast import increment_lineno
from time import sleep
from os import system
from classe1 import Nave
import pygame
import os

fimDeJogo = 0

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

system("cls")

print("Você agora é esse piloto e deve escolher as ações corretas para SALVAR A HUMANIDADE!")
sleep(2)
nomePiloto = str(input("Digite seu nome: "))

# system("cls")

# print("Sua viagem só é possível através de um BURACO DE MINHOCA!")
# sleep(2)
# print("Essa viagem durará 1 ano e nessa nova galáxia você terá 3 planetas promissores.")
# sleep(2)
# print("Na nave teremos 4 tripulantes. Você e 3 cientistas.")
# sleep(2)

nave = Nave(2021, 100, "Terra", "", "Via Láctea", "Estável")
lancarNave = str(input(f"\nVamos lançar nossa nave, {nomePiloto}? [S/N]: ")).upper().strip()[0]

if lancarNave == "S":
#     print("Lançamento em: ")
#     sleep(1)
#     print("3")
#     sleep(1)
#     print("2")
#     sleep(1)
#     print("1")
#     sleep(1)
#     print("\nVocê está no espaço! Se dirigindo ao buraco de minhoca!")
#     sleep(2)
#     print(f"\nO ano atual é 2021 e sua nave está transportando embriões \
# humanos para caso a volta não seja possível.")
#     sleep(3)

    print(nave)
    sleep(2)

    print("Você atravessou o buraco de minhoca!")
    nave.mudaGalaxia()
    print(nave)
    sleep(2)

while fimDeJogo != 1:

    nave.chamaMenu()
    escolhaPlaneta = int(input("Digite sua opção: "))
    nave.efeitoRandom()
    nave.viajarEntrePlanetas(escolhaPlaneta)
    print(nave)
    sleep(2)

else:
    print("Lançamento cancelado! Você desistiu e será o FIM DA HUMANIDADE!")

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