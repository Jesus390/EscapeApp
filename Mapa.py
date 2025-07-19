class Mapa():
    def __init__(self,alto,ancho,edificio,obstaculo,pos):
        self.ancho=ancho
        self.alto=alto
        self.edificio=edificio
        self.obstaculo=obstaculo
        self.pos=pos
        self.grilla = [['0' for _ in range(ancho)] for _ in range(alto)]

    def es_valido(self):
        x,y=self.pos
        return 0<=x<self.alto and 0<=y<self.ancho
