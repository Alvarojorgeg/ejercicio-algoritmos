from clases.logica import NReinas

if __name__ == "__main__":
    n = 8  # Cambia el valor para otras cantidades
    reinas = NReinas()
    soluciones = reinas.resolver(n)
    print(f"Cantidad de soluciones para {n} reinas: {len(soluciones)}")
    if soluciones:
        print("Ejemplo de solución:", soluciones[0])