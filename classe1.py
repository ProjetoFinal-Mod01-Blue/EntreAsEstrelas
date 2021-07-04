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

    def incrementaAno(self):
        self.anoAtual += 1

    def chamaMenu(self):
        print("Para qual planeta você deseja ir? ")
        if self.galaxia == "Nova" and self.planetaChegada == "":
            print("""
            1 - Biós
            2 - Agnostos
            3 - Matér        
            """)
        elif self.galaxia == "Nova" and self.planetaChegada == "Biós":
            print("""
            2 - Agnostos
            3 - Matér        
            """)
        elif self.galaxia == "Nova" and self.planetaChegada == "Agnostos":
            print("""
            1 - Biós
            3 - Matér        
            """)
        elif self.galaxia == "Nova" and self.planetaChegada == "Matér":
            print("""
            1 - Biós
            2 - Agnostos       
            """)

    def viajarEntrePlanetas(self, destino):
        if destino == 1:
            self.viajaPlanetaBios()
        elif destino == 2:
            self.viajaPlanetaAgnostos()
        elif destino == 3:
            self.viajaPlanetaMater()

    def efeitoRandom(self):
        resultado = randint(1,5)
        if resultado == 1:
            print("Pane elétrica! Você perdeu 2 anos terrestres enquanto reparava a nave.")
            self.anoAtual += 2
        if resultado == 2:
            print("Traje especial despressurizado! Você perdeu 1 ano terrestre aguardando a pressurização.")
            self.anoAtual += 2

    def mudaGalaxia(self):
        if self.galaxia == "Via Láctea":
            self.galaxia = "Nova"
        elif self.galaxia == "Nova":
            self.galaxia = "Via Láctea"
        self.planetaPartida == ""
        self.planetaChegada = ""

    def viajaPlanetaBios(self):
        self.planetaChegada = "Biós"
        self.combustivel -= 10
        self.anoAtual += 2

    def viajaPlanetaAgnostos(self):
        self.planetaChegada = "Agnostos"
        self.combustivel -= 70
        self.anoAtual += 3

    def viajaPlanetaMater(self):
        self.planetaChegada = "Matér"
        self.combustivel -= 20
        self.anoAtual += 14
        self.comunicacao = "Instável"