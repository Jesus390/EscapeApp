from personajes import Personajes
from mapa import Mapa
from premiotrampa import Trampa, Premio

class jugar():

    def __init__(self):
        self.tablero = Mapa()
        self.personaje = Personajes()
        self.trampas = Trampa()
        self.premios = Premio()

    def jugar(self):
        turno = 0
        while turno <= 50:
            
            turno += 1
