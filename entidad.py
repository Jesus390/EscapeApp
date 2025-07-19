class Entidad:
    def __init__(self, entidad):
        self.entidad = entidad
        self.pos_x = entidad[0]
        self.pos_y = entidad[1]
        self.pos_x_anterior = entidad[0]
        self.pos_y_anterior = entidad[1]
