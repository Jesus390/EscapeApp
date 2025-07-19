class Mapa():
    def __init__(self,alto,ancho,edificio,obstaculo):
        self.ancho=ancho
        self.alto=alto
        self.edificio=edificio
        self.obstaculo=obstaculo
        self.grilla = [['0' for _ in range(ancho)] for _ in range(alto)]

