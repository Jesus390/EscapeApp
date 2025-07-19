from personajes import Heroe
from mapa import Mapa
from premiotrampa import Premio

class Jugar():

    def __init__(self, alto, ancho, pos_inicial):
        self.tablero = Mapa(alto, ancho, pos_inicial)
        self.personaje = Heroe(self.tablero)

    def jugar(self):
        turno = 0
        self.tablero.generar_cuadras()
        while turno <= 10:
            self.tablero.mostrar_tablero()

            direccion = input('Ingrese una direccion (w,a,s,d)')
            self.personaje.movimiento(direccion)
            
            turno += 1

pos_inicial = (0,0)
jugar = Jugar(40,40, pos_inicial)
jugar.jugar()
