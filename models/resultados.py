class Resultados:
    def __init__(self, mesa, numeroCandidato, partido, votos):
        self.mesa = mesa
        self.numeroCandidato = numeroCandidato
        self.partido = partido
        self.votos = votos
    
    def toDBCollection(self):
        return {
            "mesa": self.mesa,
            "numeroCandidato": self.numeroCandidato,
            "partido": self.partido,
            "votos": self.votos
        }