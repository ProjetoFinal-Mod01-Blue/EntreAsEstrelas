from random import randint

class Nave:
    def __init__(self, anoAtual, combustivel, planetaPartida, planetaChegada, galaxia, comunicacao):
        self.anoAtual = anoAtual
        self.combustivel = combustivel
        self.planetaPartida = planetaPartida
        self.planetaChegada = planetaChegada
        self.galaxia = galaxia
        self.comunicacao = comunicacao

    def __str__(self):
        return f"""
    Ano Atual: {self.anoAtual}
    Combustível restante: {self.combustivel}%
    Planeta de partida: {self.planetaPartida}
    Planeta de chegada: {self.planetaChegada}
    Galáxia Atual: {self.galaxia}   
    Comunicação: {self.comunicacao}   
    """

    def verificaCombustivel(self):
        if self.combustivel <= 0:
            return "Você ficou sem combustível."

    def chamaMenu(self):
        print("Para qual planeta você deseja ir? ")
        if self.galaxia == "Nova" and self.planetaChegada == "":
            print("""
            1 - Biós (Mais promissor)
            2 - Agnostos (Planeta similar à Terra)
            3 - Matér (Pode não ser habitável)        
            """)
        elif self.galaxia == "Nova" and self.planetaChegada == "Biós":
            print("""
            Vamos tentar outro planeta? 

            2 - Agnostos (Planeta similar à Terra)
            3 - Matér (Pode não ser habitável)
            0 - Voltar para Terra       
            """)
        elif self.galaxia == "Nova" and self.planetaChegada == "Agnostos":
            print("""
            3 - Matér (Pode não ser habitável)
            0 - Voltar para Terra           
            """)
        elif self.galaxia == "Nova" and self.planetaChegada == "Matér":
            print("""
            0 - Voltar para Terra         
            """)

    def viajarEntrePlanetas(self, destino):
        if destino == 1:
            self.viajaPlanetaBios()
        elif destino == 2:
            self.viajaPlanetaAgnostos()
        elif destino == 3:
            self.viajaPlanetaMater()
        elif self.planetaChegada == "Biós" and destino == 0:
            while destino == 0:
                print("Coragem!! A humanidade depende de você, por favor não desista.")
                destino = int(input("Digite sua opção: "))
        elif self.planetaChegada == "Agnostos" and destino == 0:
            resposta = str(input("Você quer desistir de voltar para a Terra e iniciar uma nova humanidade neste planeta? [S/N]: "))
            if resposta == "S":
                print("Parabéns pela decisão, mas tente ensinar mais amor e menos ódio para esta nova geração.")
            else:
                print("Você voltou para a Terra e encontrou sua filha pela última vez.")
        elif self.planetaChegada == "Matér" and destino == 0:
            print("Você está voltando para a Terra")


    def efeitoRandom(self):
        resultado = randint(1,5)
        if resultado == 1:
            print("Pane elétrica! Você perdeu 2 anos terrestres enquanto reparava a nave.")
            self.anoAtual += 2
        if resultado == 2:
            print("Traje especial despressurizado! Você perdeu 1 ano terrestre aguardando a pressurização.")
            self.anoAtual += 1

    def mudaGalaxia(self):
        if self.galaxia == "Via Láctea":
            self.galaxia = "Nova"
        elif self.galaxia == "Nova":
            self.galaxia = "Via Láctea"
        self.planetaPartida = ""
        self.planetaChegada = ""
        self.anoAtual += 1

    def viajaPlanetaBios(self):
        self.planetaChegada = "Biós"
        self.combustivel -= 10
        self.anoAtual += 2
        print('''
        PLANETA BIÓS:
        As informações não estão corretas, o planeta não é habitável, 
        sem oxigênio. É todo coberto por gelo.
        -10% de combustível
        Se passaram 2 anos terrestres.
        ''')

    def viajaPlanetaAgnostos(self):
        self.planetaChegada = "Agnostos"
        self.combustivel -= 70
        self.anoAtual += 3
        print('''
        PLANETA AGNOSTOS:
        O planeta é todo coberto por água. Não habitável.
        -70% de combustível
        Se passaram 3 anos terrestres.
        ''')

    def viajaPlanetaMater(self):
        self.planetaChegada = "Matér"
        self.combustivel -= 20
        self.anoAtual += 14
        self.comunicacao = "Instável"
        print('''
        PLANETA MATÉR:
        Planeta muito parecido com a Terra. Habitável.
        O sistema de comunicação foi comprometido na entrada da atmosfera.
        -20% de combustível
        Se passaram 14 anos terrestres.
        ''')