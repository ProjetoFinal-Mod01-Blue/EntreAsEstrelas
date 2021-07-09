# Função que será usada em casos de escolhas executadas com valores numéricos

def leiaint(msg):
    valida = False
    valor = 0
    while True:
        escolha = str(input(msg))
        if escolha.isnumeric():
            valor = int(escolha)
            valida = True
        else:
            print('Opção inválida !')
        if valida :
            break
        return valor

# Funcão que será usada todas as vezes que questionar o jogador se ele quer ou não encerrar o jogo.

def encerrar():
    resp = ''
    while True:
        print('''
        0 - Continuar
        1 - Voltar para a Terra
        2 - Construir uma nova civilização
        ''')
        resp = leiaint('Você deseja desistir e voltar para Terra ou tentar reconstruir uma civilização neste planeta ?: ')
        if resp >= 0 or resp <=2:
            break
        print('Digite apenas 1 ou 2.')
    if resp == 2:
        print('Parabés pela sua decisão ! Foi preciso o uso de muita astúcia. Mas tente ensinar mais amor e menos ódio para esta nova geração. ')
        quit()
    elif resp == 1:
        print('Você voltou para a Terra e conseguiu ver sua filha pela última vez.')
    else:
        pass
    return resp


            # while True:
            #     resposta = str(input("Você quer desistir de voltar para a Terra e iniciar uma nova humanidade neste planeta? [S/N]: ")).upper().strip()[0]
            #     if resposta == "S":
            #         print("Parabéns pela decisão,ela foi de muita astúcia. Mas tente ensinar mais amor e menos ódio para esta nova geração.")
            #         break
            #     elif resposta == "N":
            #         print("Você voltou para a Terra e encontrou sua filha pela última vez.")
            #         break
            #     else:
            #         continue