# importação das bibliotecas

from random import randint    # biblioteca para gerar numeros aleatórios 
from time import sleep       # biblioteca para usar pausas entre linhas de codigo


# Criação da classe Nave
class Nave:
    def __init__(self, anoAtual, combustivel, planetaChegada, galaxia, comunicacao, fimJogo, escolha=0):
        self.__anoAtual = anoAtual
        self.__combustivel = combustivel
        self.__planetaChegada = planetaChegada
        self.__galaxia = galaxia
        self.__comunicacao = comunicacao
        self.__fimJogo = fimJogo
        self.__escolha = escolha

# getter: valor do argumento fimJogo
    @property
    def fimJogo(self):
        return self.__fimJogo

# getter: escolha do planeta pelo usuário
    @property
    def escolha(self):
        return self.__escolha

# método para exibir os valores atribuídos a cada atributo

    def __str__(self):
        return f"""
                        Ano Atual: {self.__anoAtual}
             Combustível restante: {self.__combustivel}%
               Planeta de chegada: {self.__planetaChegada}
                    Galáxia Atual: {self.__galaxia}   
                      Comunicação: {self.__comunicacao}   
    """

# método para finalizar o jogo
    def gameOver(self):
        self.__fimJogo = 0

# método para chamar o menu, exibí-lo e requisitar uma informação do usuário para poder viajar entre planetas
    def chamaMenu(self):
        print("Para qual planeta você deseja ir? ")
        # se a galáxia for Nova e o planeta de chegada não for nenhum dos possíveis executa:
        if self.__galaxia == "Nova" and self.__planetaChegada == "":
            print("""
                   1 - Biós (Mais promissor)
                   2 - Agnostos (Planeta similar à Terra)
                   3 - Matér (Pode não ser habitável)        
                """)
            # enquanto o valor não for nenhum dos possíveis continua solicitando a informação e exibindo opção inválida
            while True:
                self.__escolha = int(input("Digite a escolha: "))
                if self.__escolha == 1 or self.__escolha == 2 or self.__escolha == 3:
                    break
                else:
                    print("Opção inválida.")
        # se a galáxia for Nova e o planeta de chegada for Biós:
        elif self.__galaxia == "Nova" and self.__planetaChegada == "Biós":
            print("""
            Vamos tentar outro planeta? 

                   2 - Agnostos (Planeta similar à Terra)
                   3 - Matér (Pode não ser habitável)
                   0 - Voltar para Terra
                """)
            # enquanto o valor não for nenhum dos possíveis continua solicitando a informação e exibindo opção inválida
            while True:
                self.__escolha = int(input("Digite a escolha: "))
                if self.__escolha == 0 or self.__escolha == 2 or self.__escolha == 3:
                    break
                else:
                    print("Opção inválida.")
        # se a galáxia for Nova e o planeta de chegada for Agnostos:
        elif self.__galaxia == "Nova" and self.__planetaChegada == "Agnostos":
            print("""
                   3 - Matér (Pode não ser habitável)
                   0 - Voltar para Terra           
                """)
            # enquanto o valor não for nenhum dos possíveis continua solicitando a informação e exibindo opção inválida
            while True:
                self.__escolha = int(input("Digite a escolha: "))
                if self.__escolha == 0 or self.__escolha == 3:
                    break
                else:
                    print("Opção inválida.")
        # se a galáxia for Nova e o planeta de chegada for Matér:
        elif self.__galaxia == "Nova" and self.__planetaChegada == "Matér":
            print("""
                   4 - Construir civilização no planeta usando os embriões
                   0 - Voltar para Terra         
                """)
            # enquanto o valor não for nenhum dos possíveis continua solicitando a informação e exibindo opção inválida
            while True:
                self.__escolha = int(input("Digite a escolha: "))
                if self.__escolha == 0 or self.__escolha == 4:
                    break
                else:
                    print("Opção inválida.")

# método para viajar entre os planetas de acordo com o destino escolhido pelo usuário
    def viajarEntrePlanetas(self, destino):
        if destino == 1:
            self.viajaPlanetaBios()
        elif destino == 2:
            self.viajaPlanetaAgnostos()
        elif destino == 3:
            self.viajaPlanetaMater()

        elif self.__planetaChegada == "Biós" and destino == 0:
            while destino == 0:
                print('Coragem!! A humanidade depende de você, por favor não desista.')
                destino = 1
        
        elif self.__planetaChegada == "Agnostos" and destino == 0:  
                    print("Você voltou para a Terra e encontrou sua filha pela última vez.")
                    self.__galaxia = "Via Láctea"
                    self.__planetaChegada = "Terra"
                    self.gameOver()
        
        elif self.__planetaChegada == "Matér" and destino == 0:
            self.__galaxia = "Via Láctea"
            self.__planetaChegada = "Terra"
            hist5 = ['Seu combustível acabou. É o fim da humanidade...','Espera! Surgiram seres da 5ª dimensão e resolveram nos ajudar para termos outra chance. Você aprendeu VIAGEM NO TEMPO!', ' Você conseguiu ver sua filha e salvar a humanidade!']
            for c in hist5:
                print(c)
                sleep(4)
            self.gameOver()

        elif self.__planetaChegada == "Matér" and destino == 4:
            hist6 = ['Você iniciou uma nova humanidade!' , 'Faça amor não faça guerra!']
            for c in hist6:
                print(c)
                sleep(3)
            self.gameOver()

# método para criar efeito randômico que aumenta o ano terrestre
    def efeitoRandom(self):
        resultado = randint(1,10)
        if resultado == 1:
            print("Pane elétrica! Você perdeu 2 anos terrestres enquanto reparava a nave.")
            self.__anoAtual += 2
        if resultado == 2:
            print("Traje especial despressurizado! Você perdeu 1 ano terrestre aguardando a pressurização.")
            self.__anoAtual += 1

# método para alterar entre as galáxias Via Láctea e Nova adicionando um ano terrestre quando muda entre elas
    def mudaGalaxia(self):
        if self.__galaxia == "Via Láctea":
            self.__galaxia = "Nova"
            self.__planetaChegada = ""
        elif self.__galaxia == "Nova":
            self.__galaxia = "Via Láctea"
            self.__planetaChegada = "Terra"
        
        self.__anoAtual += 1

# método para alterar os parâmetros se o usuario escolhe Biós como destino:
    def viajaPlanetaBios(self):
        self.__planetaChegada = "Biós"
        self.__combustivel -= 10
        self.__anoAtual += 2
        print('''
        PLANETA BIÓS:
        As informações não estão corretas, o planeta não é habitável, 
        sem oxigênio. É todo coberto por gelo.
        -10% de combustível
        Se passaram 2 anos terrestres.
        ''')
        sleep(5)

# método para alterar os parâmetros se o usuario escolhe Agnostos como destino:
    def viajaPlanetaAgnostos(self):
        self.__planetaChegada = "Agnostos"
        self.__combustivel -= 70
        self.__anoAtual += 3
        print('''
        PLANETA AGNOSTOS:
        O planeta é todo coberto por água. Não habitável.
        -70% de combustível
        Se passaram 3 anos terrestres.
        ''')
        sleep(5)

# método para alterar os parâmetros se o usuario escolhe Matér como destino:
    def viajaPlanetaMater(self):
        self.__planetaChegada = "Matér"
        self.__combustivel -= 20
        self.__anoAtual += 14
        self.__comunicacao = "Instável"
        print('''
        PLANETA MATÉR:
        Planeta muito parecido com a Terra. Habitável.
        O sistema de comunicação foi comprometido na entrada da atmosfera.
        -20% de combustível
        Se passaram 14 anos terrestres.
        ''')
        sleep(5)