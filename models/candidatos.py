class Candidatos:
    def __init__(self, numero, cedula, nombre, apellido, partido):
        self.numero = numero
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.partido = partido
    
    def toDBCollection(self):
        return {
            "numero": self.numero,
            "cedula": self.cedula,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "partido": self.partido
        }