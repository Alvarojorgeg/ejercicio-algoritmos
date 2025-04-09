class NReinas:
    def resolver(self, n):
        soluciones = []
        self.colocar([], 0, n, soluciones)
        return soluciones

    def colocar(self, actual, fila, n, soluciones):
        if fila == n:
            soluciones.append(actual[:])
            return
        for col in range(n):
            if self.es_valido(actual, fila, col):
                actual.append(col)
                self.colocar(actual, fila + 1, n, soluciones)
                actual.pop()

    def es_valido(self, actual, fila, col):
        for f, c in enumerate(actual):
            if c == col or abs(f - fila) == abs(c - col):
                return False
        return True
