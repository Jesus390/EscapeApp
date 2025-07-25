from entidad import Entidad
import random 
#clase para los tipos de poderes(speed,saltar muros,teleport,escudo Antivillano(Exclusivo para el personaje))
class Premio(Entidad):
  
    def __init__(self, pos, tipo, mapa, exclusivo_jugador=False):

        self.mapa = mapa
        super().__init__(pos)

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

#clase para posicionar los premios/poderes en el mapa 


class PosicionarPoderes:
    def __init__(self, mapa):
        self.mapa = mapa
        self.premios = []

    def posicion_valida(self, x, y):
        if self.mapa[y][x] == 0:
            return True
        else:
            return False

    def generar_poder(self, cantidad):
        tipos = ["speed", "saltar", "teleport", "escudo"]
        filas = len(self.mapa)
        columnas = len(self.mapa[0])

        for _ in range(cantidad):
            tipo = random.choice(tipos)

            while True:
                x = random.randint(0, columnas - 1)
                y = random.randint(0, filas - 1)

                if self.posicion_valida(x, y):
                    break

            poder = Premio((x, y), tipo, self.mapa, True)
            self.mapa[y][x] = poder.get_valor()
            self.premios.append(poder)

            
            




    
    
