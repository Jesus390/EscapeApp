import random

class Mapa():
    def __init__(self, alto, ancho, pos):
        self.ancho = ancho
        self.alto = alto
        self.pos = pos
        self.grilla = [[0 for _ in range(ancho)] for _ in range(alto)]

        self.EDIFICIO = 1
        self.OBSTACULO = 2

        self.simbolos = {
            0: '.',
            1: 'E',
            2: 'X'
        }

    def es_valido(self, x, y):
        return 0 <= x < self.alto and 0 <= y < self.ancho

    def mostrar_tablero(self):
        for fila in self.grilla:
            print(" ".join(self.simbolos[celda] for celda in fila))

    def puede_colocar_cuadra(self, tablero, fila_inicio, col_inicio, ancho, alto):
        filas = len(tablero)
        columnas = len(tablero[0])

        # Verifica si se sale del mapa
        if fila_inicio + alto > filas or col_inicio + ancho > columnas:
            return False

        # Verifica que todas las celdas estén libres (0)
        for fila in range(fila_inicio, fila_inicio + alto):
            for col in range(col_inicio, col_inicio + ancho):
                if tablero[fila][col] == 1:
                    return False

        return True

    def colocar_cuadra(self, tablero, fila_inicio, col_inicio, ancho, alto):
        for fila in range(fila_inicio, fila_inicio + alto):
            for col in range(col_inicio, col_inicio + ancho):
                tablero[fila][col] = 1  # 1 = ocupado

    def generar_cuadras(self):
        filas = len(self.grilla)
        columnas = len(self.grilla[0])

        # Tamaños posibles de cuadras
        cuadras = [
            {'ancho': 3, 'alto': 3},
            {'ancho': 7, 'alto': 3},
            {'ancho': 3, 'alto': 7},
        ]

        # Cuadras principales
        for fila in range(0, filas, 4):
            for col in range(0, columnas, 4):
                tipos_aleatorios = random.sample(cuadras, len(cuadras))  # mezcla

                for tipo in tipos_aleatorios:
                    if self.puede_colocar_cuadra(self.grilla, fila, col, tipo['ancho'], tipo['alto']):
                        self.colocar_cuadra(self.grilla, fila, col, tipo['ancho'], tipo['alto'])
                        break

        # Rellenar bordes horizontales (últimas columnas)
        for fila in range(0, filas, 4):
            col_restante = columnas % 4
            col_inicio = columnas - col_restante

            if col_restante > 0:
                for alto in range(3, 0, -1):
                    cuadra = {'ancho': col_restante, 'alto': alto}
                    if self.puede_colocar_cuadra(self.grilla, fila, col_inicio, cuadra['ancho'], cuadra['alto']):
                        self.colocar_cuadra(self.grilla, fila, col_inicio, cuadra['ancho'], cuadra['alto'])
                        break

        # Rellenar bordes verticales (últimas filas)
        for col in range(0, columnas, 4):
            fila_restante = filas % 4
            fila_inicio = filas - fila_restante

            if fila_restante > 0:
                for ancho in range(3, 0, -1):
                    cuadra = {'ancho': ancho, 'alto': fila_restante}
                    if self.puede_colocar_cuadra(self.grilla, fila_inicio, col, cuadra['ancho'], cuadra['alto']):
                        self.colocar_cuadra(self.grilla, fila_inicio, col, cuadra['ancho'], cuadra['alto'])
                        break

    def colocar_obstaculo_aleatorio(self, cantidad):
        colocados = 0
        while colocados < cantidad:
            x = random.randint(0, self.alto - 1)
            y = random.randint(0, self.ancho - 1)
            if self.grilla[x][y] == 0:
                self.grilla[x][y] = self.OBSTACULO
                colocados += 1
