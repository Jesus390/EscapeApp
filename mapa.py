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
        for fila in range(0, self.ancho, 2):
            for columna in range(0, self.alto, 2):
                self.matriz[fila][columna] = self.edificio

        for fila in range(self.ancho):
            for columna in range(self.alto):
                if self.matriz[fila][columna] == 0:
                    if random.randint(0, 100) <= self.porcentaje:
                        self.matriz[fila][columna] = self.bloqueos

    def validacion_entrada_salidar(self, entrada, salida):
        if 0 <= entrada[0] < self.ancho and 0 <= entrada[1] < self.alto:
            if self.matriz[entrada[0]][entrada[1]] != self.edificio and self.matriz[entrada[0]][entrada[1]] != self.bloqueos:
                self.matriz[entrada[0]][entrada[1]] = 4

        if 0 <= salida[0] < self.ancho and 0 <= salida[1] < self.alto:
            if self.matriz[salida[0]][salida[1]] != self.edificio and self.matriz[salida[0]][salida[1]] != self.bloqueos:
                if salida != entrada:
                    self.matriz[salida[0]][salida[1]] = 5

    #prueba de envio
