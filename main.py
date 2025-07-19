from personajes import Heroe
from Mapa import Mapa
from premiotrampa import Premio

class Jugar():

    def __init__(self, alto, ancho):
        self.tablero = Mapa(alto, ancho, 0, 0, (0,0))
        self.personaje = Heroe(self.tablero, 0, 0)

    def jugar(self):
        turno = 0
        while turno <= 50:
            self.tablero.mostrar_tablero()
            direccion = input('Ingrese una direccion (w,a,s,d)')
            
            self.personaje.movimiento(direccion)
            
            turno += 1


jugar = Jugar(10,10)
jugar.jugar()
