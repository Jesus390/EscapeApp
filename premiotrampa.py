from entidad import Entidad
#clase para los tipos de poderes(speed,saltar muros,teleport,escudo Antivillano(Exclusivo para el personaje))
class Premio(Entidad):
    def __init__(self, x, y, tipo, exclusivo_jugador=False):
        self.x = x
        self.y = y
        self.tipo = tipo
        