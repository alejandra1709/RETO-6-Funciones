import math 
pi=math.pi
def perimetro (base_rectangulo:float,altura_rectangulo:float,radio_circulos:float) -> float:
    perimetro_rectangulo=2*base_rectangulo+2*altura_rectangulo
    perimetro_circulo=2*pi*radio_circulos
    perimetro_total=perimetro_rectangulo+2*perimetro_circulo
    return perimetro_total

def area (base_rectangulo:float,altura_rectangulo:float,radio_circulos:float) -> float:
    area_rectangulo=base_rectangulo*altura_rectangulo
    area_circulos=2*pi*radio_circulos**2
    area_total=area_circulos+area_rectangulo
    return area_total

if __name__ == "__main__":
    base_rectangulo: float = float (input("Ingrese la medida de la base del rectángulo en centímetros: "))
    altura_rectangulo: float = float (input("Ingrese la altura del rectángulo en centímetros: "))
    radio_circulos: float = float (input("Ingrese el radio de los círculos en centímetros: "))
    area_final=area(base_rectangulo,altura_rectangulo,radio_circulos)
    perimetro_final=perimetro(base_rectangulo,altura_rectangulo,radio_circulos)
    print("El área de la figura es de",area_final,"centímetros cuadrados")
    print("El perímetro de la figura es",perimetro_final,"centímetros")