class Nave:
    def __init__(self, anoAtual, combustivel, planetaPartida, planetaChegada, galaxia):
        self.anoAtual = anoAtual
        self.combustivel = combustivel
        self.planetaPartida = planetaPartida
        self.planetaChegada = planetaChegada
        self.galaxia = galaxia

    def __str__(self):
        return f"""
    Ano Atual: {self.anoAtual}
    Combustível restante: {self.combustivel}%
    Planeta de partida: {self.planetaPartida}
    Planeta de chegada: {self.planetaChegada}
    Galáxia Atual: {self.galaxia}      
        """

    def consomeCombustivel(self):
        pass

    def incrementaAno(self):
        self.anoAtual += 1

    def mudaGalaxia(self):
        self.galaxia = "Nova"