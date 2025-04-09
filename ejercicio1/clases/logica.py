class MovimientoCaballo:
    def __init__(self):
        self.movimientos = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }

    def movimientos_validos(self, pasos):
        dp = [[0] * 10 for _ in range(pasos + 1)]
        for i in range(10):
            dp[0][i] = 1

        for p in range(1, pasos + 1):
            for i in range(10):
                dp[p][i] = sum(dp[p - 1][j] for j in self.movimientos[i])

        return sum(dp[pasos])