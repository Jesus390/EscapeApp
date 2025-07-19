from personajes import Heroe
from mapa import Mapa
from premiotrampa import Premio

class Jugar():

    def __init__(self, alto, ancho, pos_inicial):
        self.tablero = Mapa(alto, ancho, pos_inicial)
        self.heroe = Heroe(pos_inicial, self.tablero)

    def jugar(self):
        turno = 0
        self.tablero.generar_cuadras()

        self.tablero.colocar_entrada_salida(pos_inicial, (27,47))
        while turno <= 10:
            self.tablero.mostrar_tablero()

            direccion = input('Ingrese una direccion (w,a,s,d)')
            self.heroe.movimiento(direccion)
            
            turno += 1

pos_inicial = (3,3)
jugar = Jugar(30,50, pos_inicial)
jugar.jugar()
