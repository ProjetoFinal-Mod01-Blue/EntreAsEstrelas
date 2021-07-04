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

    def consomeCombustivel(self):
        pass

    def incrementaAno(self):
        self.anoAtual += 1

    def mudaGalaxiaNova(self):
        self.galaxia = "Nova"

    def mudaGalaxiaNova(self):
        self.galaxia = "Via Láctea"

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