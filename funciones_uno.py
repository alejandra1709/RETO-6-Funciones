import math 
pi=math.pi
def volumen (radio_esfera:float,radio_cono:float,altura_cono:float) -> float :
    volumen_esfera=4/3*pi*radio_esfera**3
    volumen_cono=(pi*radio_cono**2*altura_cono)/3
    volumen_total=volumen_cono+volumen_esfera
    return volumen_total

def area (radio_esfera:float,radio_cono:float,altura_cono:float) -> float :
    area_esfera=4*pi*radio_esfera**2
    altura_inclinacion=(radio_cono**2+altura_cono**2)**0.5
    area_cono=(pi*altura_inclinacion*radio_cono)+(pi*radio_cono**2)
    area_total=area_cono+area_esfera
    return area_total

if __name__ == "__main__":
    radio_esfera: float = float (input("Ingrese el radio de la esfera en centímetros: "))
    radio_cono: float = float (input("Ingrese el radio del cono en centímetros: "))
    altura_cono: float = float (input("Ingrese la altura del cono en centímetros: "))
    area_superficial=area(radio_esfera,radio_cono,altura_cono)
    volumen_final=volumen(radio_esfera,radio_cono,altura_cono)
    print("El área superficial de la figura es de",area_superficial,"centímetros cuadrados")
    print("El volúmen de la figura es",volumen_final,"centímetros cúbicos")
    