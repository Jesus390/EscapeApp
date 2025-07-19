
#clase para los tipos de poderes(speed,saltar muros,teleport,escudo Antivillano(Exclusivo para el personaje))
class Premio(Entidad):
  
    def __init__(self, x, y, tipo, exclusivo_jugador=False):
        
        super().__init__(x, y)

       
        self.tipo = tipo

        # si es un premio exclusivo del jugador, como el escudo
        self.exclusivo_jugador = exclusivo_jugador

        tipos_a_valores = {
            "speed": 5,     # avanza dos casillas con doble tecla
            "saltar": 6,    # permite saltar muros o enemigos
            "teleport": 7,  # puede moverse hasta 5 casillas
            "escudo": 8     # si el villano llega, lo empuja dos casillas atras
        }

        self.valor = tipos_a_valores[tipo]

    
    def get_valor(self):
        return self.valor
   
 #aplico los poderes
    def usar_poder(self, quien_usa):
        if self.tipo == "speed":
            quien_usa.poderes["speed"] = True
        elif self.tipo == "saltar":
            quien_usa.poderes["saltar"] = True
        elif self.tipo == "teleport":
            quien_usa.poderes["teleport"] = True
        elif self.tipo == "escudo":
            if self.exclusivo_jugador and quien_usa.es_jugador:
                quien_usa.poderes["escudo"] = True
    
    