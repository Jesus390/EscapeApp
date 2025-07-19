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
                self.pos_x_anterior = self.pos_x
                self.mapa.grilla[self.pos_x_anterior][self.pos_y_anterior] = 0
                self.pos_x -= 1
        elif direccion == "s":
            if self.mapa.es_valido(self.pos_x, self.pos_y + 1):
                self.mapa.grilla[self.pos_x_anterior][self.pos_y_anterior] = 0
                self.pos_x += 1
        elif direccion == "a":
            if self.mapa.es_valido(self.pos_x, self.pos_y):
                self.pos_y_anterior = self.pos_y
                self.mapa.grilla[self.pos_x_anterior][self.pos_y_anterior] = 0
                self.pos_y -= 1
        elif direccion == "d":
            if self.mapa.es_valido(self.pos_x, self.pos_y):
                self.pos_y_anterior = self.pos_y
                self.mapa.grilla[self.pos_x_anterior][self.pos_y_anterior] = 0
                self.pos_y += 1

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
        self.ultimos_movimientos = []

    def movimientos_validos(self, pos=None):
        if pos is None:
            pos = (self.pos_x, self.pos_y)
        x, y = pos
        posibles = [(x + dx, y + dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        return [m for m in posibles if self.es_valido(m)]

    def es_valido(self, pos):
        x, y = pos
        return (0 <= y < len(self.mapa.matriz)) and (0 <= x < len(self.mapa.matriz[0])) and self.mapa.matriz[y][x] != 1

    def movimiento_AI(self, player_pos, max_turno):
        mejor_mov = self.get_best_move(player_pos, max_turno)
        if mejor_mov:
            self.pos_x, self.pos_y = mejor_mov
            self.ultimos_movimientos.append(mejor_mov)
            if len(self.ultimos_movimientos) > 4:
                self.ultimos_movimientos.pop(0)

    def get_best_move(self, player_pos, max_turno):
        mejor_score = float("-inf")
        mejor_mov = None
        actual_pos = (self.pos_x, self.pos_y)

        for move in self.movimientos_validos():
            self.pos_x, self.pos_y = move
            score = self.minimax(0, True, move, player_pos, 0, max_turno)

            if move in self.ultimos_movimientos:
                score -= 5

            if score > mejor_score:
                mejor_score = score
                mejor_mov = move

        self.pos_x, self.pos_y = actual_pos
        return mejor_mov

    def evaluar_estado(self, villano_pos, player_pos, turno, max_turno):
        if villano_pos == player_pos:
            return 100
        if turno >= max_turno:
            return -100

        dx = abs(player_pos[0] - villano_pos[0])
        dy = abs(player_pos[1] - villano_pos[1])
        return -(3 * dx + 2 * dy + turno)

    def minimax(self, profundidad, es_max, villano_pos, player_pos, turno, max_turno):
        if profundidad == 4 or villano_pos == player_pos or turno >= max_turno:
            return self.evaluar_estado(villano_pos, player_pos, turno, max_turno)

        if es_max:
            max_eval = float("-inf")
            for move in self.movimientos_validos(villano_pos):
                eval = self.minimax(profundidad + 1, False, move, player_pos, turno, max_turno)
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for move in self.movimientos_validos(player_pos):
                eval = self.minimax(profundidad + 1, True, villano_pos, move, turno + 1, max_turno)
                min_eval = min(min_eval, eval)
            return min_eval

