from personajes import Heroe, Villanos
from mapa import Mapa
from premiotrampa import PosicionarPoderes

class Jugar():

    def __init__(self, alto, ancho, pos_inicial):
        self.tablero = Mapa(alto, ancho, pos_inicial)
        self.heroe = Heroe(self.tablero, pos_inicial)

        ubi_malo = self.tablero.buscar_ubicacion_libre()
        self.villano = Villanos(self.tablero, ubi_malo)

    def jugar(self):
        turno = 0
        self.tablero.generar_cuadras()

        self.tablero.colocar_entrada_salida(pos_inicial, (27,47))
    
        posicionador = PosicionarPoderes(self.tablero.grilla)
        posicionador.generar_poder(5)

        while turno <= 50:
            self.tablero.mostrar_tablero()

            direccion = input('Ingrese una direccion (w,a,s,d)')
            self.heroe.movimiento(direccion)
            self.heroe.agregar_al_mapa()

            self.villano.movimiento_AI((self.heroe.pos_x, self.heroe.pos_y), turno)
            
            turno += 1

pos_inicial = (3,3)
jugar = Jugar(30,50, pos_inicial)
jugar.jugar()
