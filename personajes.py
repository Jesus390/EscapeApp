from entidad import Entidad


class Heroe(Entidad):
    def __init__(self, mapa):
        self.mapa = mapa

    def movimiento(self, direccion):
        if direccion == "w":
            self.y -= 1
        elif direccion == "s":
            self.y += 1
        elif direccion == "a":
            self.x -= 1
        elif direccion == "d":
            self.x += 1


class Villanos(Entidad):
    def __init__(self, mapa):
        self.mapa = mapa

    def movimiento(self, direccion):
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
