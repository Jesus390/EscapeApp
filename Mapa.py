import random

class Mapa():
    def __init__(self, alto, ancho, pos):
        self.ancho = ancho
        self.alto = alto
        self.pos = pos
        self.grilla = [[0 for _ in range(ancho)] for _ in range(alto)]

        self.EDIFICIO = 1
        self.OBSTACULO = 2

        self.simbolos = {
            0: '.',
            1: 'E',
            2: 'X'
        }

    def es_valido(self):
        x, y = self.pos
        return 0 <= x < self.alto and 0 <= y < self.ancho

    def mostrar_tablero(self):
        for fila in self.grilla:
            print(" ".join(self.simbolos[celda] for celda in fila))

    def colocar_edificio_aleatorio(self, cantidad):
        colocados = 0
        while colocados < cantidad:
            x = random.randint(0, self.alto - 1)
            y = random.randint(0, self.ancho - 1)
            if self.grilla[x][y] == 0:
                self.grilla[x][y] = self.EDIFICIO
                colocados += 1

    def colocar_obstaculo_aleatorio(self, cantidad):
        colocados = 0
        while colocados < cantidad:
            x = random.randint(0, self.alto - 1)
            y = random.randint(0, self.ancho - 1)
            if self.grilla[x][y] == 0:
                self.grilla[x][y] = self.OBSTACULO
                colocados += 1
