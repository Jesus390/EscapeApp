from entidad import Entidad


class Heroe(Entidad):
    def __init__(self, mapa, posicion):
        super().__init__(posicion)
        self.mapa = mapa
        self.poderes = {
            "speed": False,
            "salto": False,
            "teleport": False,
            "escudo": False,
        }

    def movimiento(self, direccion):
        if direccion == "w":
            if self.mapa.es_valido(self.pos_x, self.pos_y - 1):
                self.mapa.grilla[self.pos_x][self.pos_y] = 0
                self.pos_x -= 1
                self.mapa.grilla[self.pos_x][self.pos_y] = 3

        elif direccion == "s":
            if self.mapa.es_valido(self.pos_x, self.pos_y + 1):
                self.mapa.grilla[self.pos_x][self.pos_y] = 0
                self.pos_x += 1
                self.mapa.grilla[self.pos_x][self.pos_y] = 3

        elif direccion == "a":
            if self.mapa.es_valido(self.pos_x, self.pos_y):
                self.mapa.grilla[self.pos_x][self.pos_y] = 0
                self.pos_y -= 1
                self.mapa.grilla[self.pos_x][self.pos_y] = 3

        elif direccion == "d":
            if self.mapa.es_valido(self.pos_x, self.pos_y):
                self.mapa.grilla[self.pos_x][self.pos_y] = 0
                self.pos_y += 1
                self.mapa.grilla[self.pos_x][self.pos_y] = 3

    def agregar_al_mapa(self):
        if self.mapa.es_valido(self.pos_x, self.pos_y):
            self.mapa.grilla[self.pos_x][self.pos_y] = 3


class Villanos(Entidad):
    def __init__(self, mapa, posicion):
        super().__init__(posicion)
        self.mapa = mapa
        self.poderes = {
            "speed": False,
            "salto": False,
            "teleport": False,
            "escudo": False,
        }

    def movimiento(self):
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def agregar_al_mapa(self):
        if self.mapa.es_valido(self.pos_x, self.pos_y):
            self.mapa.grilla[self.pos_x][self.pos_y] = 9
