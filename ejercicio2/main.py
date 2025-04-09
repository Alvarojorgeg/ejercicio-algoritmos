from clases.logica import NReinas

if __name__ == "__main__":
    n = 8 
    reinas = NReinas()
    soluciones = reinas.resolver(n)
    print(f"Cantidad de soluciones para {n} reinas: {len(soluciones)}")
    if soluciones:
        print("Esta es la solución:", soluciones[0])