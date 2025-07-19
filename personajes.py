from entidad import Entidad


class Personajes(Entidad):
    def mover(self, direccion):
        if direccion == w:
            self.y -= 1
        elif direccion == s:
            self.y += 1
