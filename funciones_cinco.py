def valor_prestamo (dinero_prestado:float,interes:float,meses:int) -> float:
    valor_final_prestamo=dinero_prestado*(1+(interes/100))**meses
    return valor_final_prestamo


if __name__ == "__main__":
    dinero_prestado: float = float(input("Ingrese la cantidad de dinero que se le fue prestado: "))
    interes: float = float(input("Ingrese la tasa de interés mensual (%): "))
    meses: int = int(input("Ingrese el tiempo del préstamo en meses: "))
    prestamo=valor_prestamo(dinero_prestado,interes,meses)
    print("El valor del préstamo es de",prestamo)

    
