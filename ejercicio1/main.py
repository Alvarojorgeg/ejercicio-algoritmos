from clases.logica import MovimientoCaballo

if __name__ == "__main__":
    movimientos = 2 
    caballo = MovimientoCaballo()
    total = caballo.movimientos_validos(movimientos)
    print(f"Movimientos válidos para {movimientos} movimientos: {total}")