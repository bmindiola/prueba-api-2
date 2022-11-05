class Partidos:
    def __init__(self, nombrePartido, lema):
        self.nombrePartido = nombrePartido
        self.lema = lema
    
    def toDBCollection(self):
        return {
            "nombrePartido": self.nombrePartido,
            "lema": self.lema
        }