class Mesas:
    def __init__(self, mesa, cedulas_inscritas):
        self.mesa = mesa
        self.cedulas_inscritas = cedulas_inscritas
    
    def toDBCollection(self):
        return {
            "mesa": self.mesa,
            "cedulas_inscritas": self.cedulas_inscritas
        }
        