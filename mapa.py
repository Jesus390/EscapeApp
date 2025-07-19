import random

class Mapa:
    def __init__(self, alto, ancho, edificio, bloqueos, porcentaje):
        self.alto = alto
        self.ancho = ancho
        self.edificios = edificio
        self.bloqueos = bloqueos
        self.porcentaje = porcentaje
        self.matriz = [[0 for _ in range(alto)]for _ in range(ancho)]
        self.generar_tablero()

    def generar_tablero(self):
        for fila in range(0, self.dimension, 2):
            for columna in range(0, self.dimension, 2):
                self.tablero[fila][columna] = self.edificio

        for fila in range(self.dimension):
            for columna in range(self.dimension):
                if self.tablero[fila][columna] == 0:
                    if random.randint(0, 100) <= self.porcentaje:
                        self.tablero[fila][columna] = self.obstaculos

    def mostrar(self):
        for filas in self.matriz:
            print(" ".join(filas))

