from entidad import Entidad


class Heroe(Entidad):
    def __init__(self, posicion, mapa):
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
                self.pos_y -= 1
            else:
                print('mov no valido')
        elif direccion == "s":
            if self.mapa.es_valido(self.pos_x, self.pos_y + 1):
                self.pos_y += 1
        elif direccion == "a":
            if self.mapa.es_valido(self.pos_x, self.pos_y - 1):
                self.pos_x -= 1
        elif direccion == "d":
            if self.mapa.es_valido(self.pos_x, self.pos_y + 1):
                self.pos_x += 1


class Villanos(Entidad):
    def __init__(self, mapa):
        self.mapa = mapa
        self.poderes = {
            "speed": False,
            "salto": False,
            "teleport": False,
            "escudo": False,
        }

    def movimiento(self):
        movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]
