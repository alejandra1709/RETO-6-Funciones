def contagiados(contagiados_actuales:int,dias:int) -> int:
    contagiados_futuros=contagiados_actuales*2**dias
    return contagiados_futuros
if __name__ == "__main__":
    contagiados_actuales: int = int(input("Ingrese el número de contagiados actuales: "))
    dias: int = int(input("Ingrese el número de días que pasarán desde hoy hasta el día en el que quiere conocer el número de contagiados: "))
    contagiados_solicitados=contagiados(contagiados_actuales,dias)
    print("Cuando pasen",dias,"dias, se van a haber contagiado",contagiados_solicitados,"personas")
    
