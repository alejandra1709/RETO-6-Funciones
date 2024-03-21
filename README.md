# RETO-6-Funciones
>***1. Dado la figura de la imagen, desarrolle:***
>
>* Una función matemática para calcular el volumen y el área superficial.
>
>* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r1, r2 y h.
>
>* Revise como utilizar el valor de pi usando import math y math.pi
<div align="center">
  <img src="https://i.postimg.cc/kg7bRdXK/68747470733a2f2f692e706f7374696d672e63632f465276436d7078782f696d6167652e706e67.png">
</div>

```python
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
```
>***2. Dado la figura de la imagen, desarrolle:***
>
>* Una función matemática para calcular el área y el perimetro.
>
>* Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado r, a y b.
>
>* Revise como utilizar el valor de pi usando import math y math.pi
<div align="center">
  <img src="https://i.postimg.cc/bJz4SrSk/68747470733a2f2f692e706f7374696d672e63632f3174344d727a734c2f696d6167652e706e67.png">
</div>

```python
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
```
>***3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.***
```python
def cantidad_carne(gallinas:int,gallos:int,pollitos:int) -> int:
    carne=gallinas*6+gallos*7+pollitos*1
    return carne
if __name__ == "__main__":
    gallinas: int = int(input("Ingrese el número de gallinas: "))
    gallos: int = int(input("Ingrese el número de gallos: "))
    pollitos: int = int(input("Ingrese el número de pollitos: "))
    kilos_carne=cantidad_carne(gallinas,gallos,pollitos)
    print("La cantidad de carne de aves es de",kilos_carne,"kilogramos")
```
>***4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.***
```python
def compra(panes:int,leches:int,huevos:int,dinero:int) -> int:
    total=300*panes+3300*leches+350*huevos
    vueltas=dinero-total
    return vueltas

if __name__ == "__main__":
    panes: int = int(input("¿Cuántos panes te mandó a comprar tú mamá? "))
    leches: int = int(input("¿Cuántas bolsas de leche te mandó a comprar tú mamá? "))
    huevos: int = int(input("¿Cuántos huevos te mandó a comprar tú mamá? "))
    dinero: int = int(input("¿De cuánto es el billete que te dio tú mamá? "))
    sobra=compra(panes,leches,huevos,dinero)
    if sobra >=0:
        print("Las vueltas que te deben dar son de:",sobra,"pesos")
    else:
        print("Te faltan",-(sobra),"para comprar todas las cosas")
```
>***5. Haga un programa que utilice una función para calcular el valor de un préstamo C usando interés compuesto del i por n meses.***
```python
def valor_prestamo (dinero_prestado:float,interes:float,meses:int) -> float:
    valor_final_prestamo=dinero_prestado*(1+(interes/100))**meses
    return valor_final_prestamo


if __name__ == "__main__":
    dinero_prestado: float = float(input("Ingrese la cantidad de dinero que se le fue prestado: "))
    interes: float = float(input("Ingrese la tasa de interés mensual (%): "))
    meses: int = int(input("Ingrese el tiempo del préstamo en meses: "))
    prestamo=valor_prestamo(dinero_prestado,interes,meses)
    print("El valor del préstamo es de",prestamo)
```
>***6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen D días a partir de hoy, si el número de contagiados actuales es C.***
```python
def contagiados(contagiados_actuales:int,dias:int) -> int:
    contagiados_futuros=contagiados_actuales*2**dias
    return contagiados_futuros
if __name__ == "__main__":
    contagiados_actuales: int = int(input("Ingrese el número de contagiados actuales: "))
    dias: int = int(input("Ingrese el número de días que pasarán desde hoy hasta el día en el que quiere conocer el número de contagiados: "))
    contagiados_solicitados=contagiados(contagiados_actuales,dias)
    print("Cuando pasen",dias,"dias, se van a haber contagiado",contagiados_solicitados,"personas")
```
>***7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:***
>* El promedio
>
>* La mediana
>
>* El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
>
>* Ordenar los números de forma ascendente
>
>* Ordenar los números de forma descendente
>
>* La potencia del mayor número elevado al menor número
>
>* La raíz cúbica del menor número
```python
import operaciones
if __name__ == "__main__":
    a: float = float(input("Escriba el primer número real: "))
    b: float = float(input("Escriba el segundo número real: "))
    c: float = float(input("Escriba el tercer número real: "))
    d: float = float(input("Escriba el cuarto número real: "))
    e: float = float(input("Escriba el quinto número real: "))
    n1: float = operaciones.orden(a,b,c,d,e)[0]
    n2: float = operaciones.orden(a,b,c,d,e)[1]
    n3: float = operaciones.orden(a,b,c,d,e)[2]
    n4: float = operaciones.orden(a,b,c,d,e)[3]
    n5: float = operaciones.orden(a,b,c,d,e)[4]
    print ("Los valores ingresados son: " , a , "," , b , "," , c , "," , d , "y" , e)
    print ("Su promedio es: " , operaciones.promedio(a,b,c,d,e))
    print("Su mediana es: " , n3)
    print("Su promedio multiplicativo es: " , operaciones.promedio_multiplicativo(a,b,c,d,e))
    print("Los números ordenados de forma ascendente: ",n1,",",n2,",",n3,",",n4,",",n5)
    print("Los números ordenados de forma descendente: ",n5,",",n4,",",n3,",",n2,",",n1)
    print("La potencia del mayor número elevado al menor número es: " , operaciones.potencia(n1,n5))
    print("La raíz cúbica del menor número es: " , operaciones.raiz(n1))
```
>***8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.***

operaciones.py:
```python
def promedio (a:float,b:float,c:float,d:float,e:float) -> float:
    prom= (a+b+c+d+e)/5
    return prom

def orden (a:float,b:float,c:float,d:float,e:float) -> float:
    if a<=b and a<=c and a<=d and a<=e :
        n1=a
        if b<=c and b<=d and b<=e :
            n2=b
            if c<=d and c<=e :
                n3=c
                if d<=e :
                    n4=d
                    n5=e
                else:
                    n4=e
                    n5=d
            elif d<=c and d<=e :
                n3=d
                if c<=e :
                    n4=c
                    n5=e
                else:
                    n4=e
                    n5=c
            elif e<=c and e<=d :
                n3=e
                if c<=d :
                    n4=c
                    n5=d
                else:
                    n4=d
                    n5=c
        elif c<=b and c<=d and c<=e :
            n2=c
            if b<=d and b<=e :
                n3=b
                if d<=e :
                    n4=d
                    n5=e
                else:
                    n4=e
                    n5=d
            elif d<=b and d<=e :
                n3=d
                if b<=e :
                    n4=b
                    n5=e
                else:
                    n4=e
                    n5=b
            elif e<=b and e<=d :
                n3=e
                if b<=d :
                    n4=b
                    n5=d
                else:
                    n4=d
                    n5=b
        elif d<=b and d<=c and d<=e :
            n2=d
            if b<=c and b<=e :
                n3=b
                if c<=e :
                    n4=c
                    n5=e
                else:
                    n4=e
                    n5=c
            elif c<=b and c<=e :
                n3=c
                if b<=e :
                    n4=b
                    n5=e
                else:
                    n4=e
                    n5=b
            elif e<=b and e<=c :
                n3=e
                if b<=c :
                    n4=b
                    n5=c
                else:
                    n4=c
                    n5=b
        elif e<=b and e<=c and e<=d :
            n2=e
            if b<=c and b<=d :
                n3=b
                if c<=d :
                    n4=c
                    n5=d
                else:
                    n4=d
                    n5=c
            elif c<=b and c<=d :
                n3=c
                if b<=d :
                    n4=b
                    n5=d
                else:
                    n4=d
                    n5=b
            elif d<=b and d<=c :
                n3=d
                if b<=c :
                    n4=b
                    n5=c
                else:
                    n4=c
                    n5=b
    elif b<=a and b<=c and b<=d and b<=e :
        n1=b
        if a<=c and a<=d and a<=e :
            n2=a
            if c<=d and c<=e :
                n3=c
                if d<=e :
                    n4=d
                    n5=e
                else:
                    n4=e
                    n5=d
            elif d<=c and d<=e :
                n3=d
                if c<=e :
                    n4=c
                    n5=e
                else:
                    n4=e
                    n5=c
            elif e<=c and e<=d :
                n3=e
                if c<=d :
                    n4=c
                    n5=d
                else:
                    n4=d
                    n5=c
        elif c<=a and c<=d and c<=e :
            n2=c
            if a<=d and a<=e :
                n3=a
                if d<=e :
                    n4=d
                    n5=e
                else:
                    n4=e
                    n5=d
            elif d<=a and d<=e :
                n3=d
                if a<=e :
                    n4=a
                    n5=e
                else:
                    n4=e
                    n5=a
            elif e<=a and e<=d :
                n3=e
                if a<=d :
                    n4=a
                    n5=d
                else:
                    n4=d
                    n5=a
        elif d<=a and d<=c and d<=e :
            n2=d
            if a<=c and a<=e :
                n3=a
                if c<=e :
                    n4=c
                    n5=e
                else:
                    n4=e
                    n5=c
            elif c<=a and c<=e :
                n3=c
                if a<=e :
                    n4=a
                    n5=e
                else:
                    n4=e
                    n5=a
            elif e<=a and e<=c :
                n3=e
                if a<=c :
                    n4=a
                    n5=c
                else:
                    n4=c
                    n5=a
        elif e<=a and e<=c and e<=d :
            n2=e
            if a<=c and a<=d :
                n3=a
                if c<=d :
                    n4=c
                    n5=d
                else:
                    n4=d
                    n5=c
            elif c<=a and c<=d :
                n3=c
                if a<=d :
                    n4=a
                    n5=d
                else:
                    n4=d
                    n5=a
            elif d<=a and d<=c :
                n3=d
                if a<=c :
                    n4=a
                    n5=c
                else:
                    n4=c
                    n5=a
    elif c<=a and c<=b and c<=d and c<=e :
        n1=c
        if a<=b and a<=d and a<=e :
            n2=a
            if b<=d and b<=e :
                n3=b
                if d<=e :
                    n4=d
                    n5=e
                else:
                    n4=e
                    n5=d
            elif d<=b and d<=e :
                n3=d
                if b<=e :
                    n4=b
                    n5=e
                else:
                    n4=e
                    n5=b
            elif e<=b and e<=d :
                n3=e
                if b<=d :
                    n4=b
                    n5=d
                else:
                    n4=d
                    n5=b
        elif b<=a and b<=d and b<=e :
            n2=b
            if a<=d and a<=e :
                n3=a
                if d<=e :
                    n4=d
                    n5=e
                else:
                    n4=e
                    n5=d
            elif d<=a and d<=e :
                n3=d
                if a<=e :
                    n4=a
                    n5=e
                else:
                    n4=e
                    n5=a
            elif e<=a and e<=d :
                n3=e
                if a<=d :
                    n4=a
                    n5=d
                else:
                    n4=d
                    n5=a
        elif d<=a and d<=b and d<=e :
            n2=d
            if a<=b and a<=e :
                n3=a
                if b<=e :
                    n4=b
                    n5=e
                else:
                    n4=e
                    n5=b
            elif b<=a and b<=e :
                n3=b
                if a<=e :
                    n4=a
                    n5=e
                else:
                    n4=e
                    n5=a
            elif e<=a and e<=b :
                n3=e
                if a<=b :
                    n4=a
                    n5=b
                else:
                    n4=b
                    n5=a
        elif e<=a and e<=b and e<=d :
            n2=e
            if a<=b and a<=d :
                n3=a
                if b<=d :
                    n4=b
                    n5=d
                else:
                    n4=d
                    n5=b
            elif b<=a and b<=d :
                n3=b
                if a<=d :
                    n4=a
                    n5=d
                else:
                    n4=d
                    n5=a
            elif d<=a and d<=b :
                n3=d
                if a<=b :
                    n4=a
                    n5=b
                else:
                    n4=b
                    n5=a
    elif d<=a and d<=b and d<=c and d<=e :
        n1=d
        if a<=b and a<=c and a<=e :
            n2=a
            if b<=c and b<=e :
                n3=b
                if c<=e :
                    n4=c
                    n5=e
                else:
                    n4=e
                    n5=c
            elif c<=b and c<=e :
                n3=c
                if b<=e :
                    n4=b
                    n5=e
                else:
                    n4=e
                    n5=b
            elif e<=b and e<=c :
                n3=e
                if b<=c :
                    n4=b
                    n5=c
                else:
                    n4=c
                    n5=b
        elif b<=a and b<=c and b<=e :
            n2=b
            if a<=c and a<=e :
                n3=a
                if c<=e :
                    n4=c
                    n5=e
                else:
                    n4=e
                    n5=c
            elif c<=a and c<=e :
                n3=c
                if a<=e :
                    n4=a
                    n5=e
                else:
                    n4=e
                    n5=a
            elif e<=a and e<=c :
                n3=e
                if a<=c :
                    n4=a
                    n5=c
                else:
                    n4=c
                    n5=a
        elif c<=a and c<=b and c<=e :
            n2=c
            if a<=b and a<=e :
                n3=a
                if b<=e :
                    n4=b
                    n5=e
                else:
                    n4=e
                    n5=b
            elif b<=a and b<=e :
                n3=b
                if a<=e :
                    n4=a
                    n5=e
                else:
                    n4=e
                    n5=a
            elif e<=a and e<=b :
                n3=e
                if a<=b :
                    n4=a
                    n5=b
                else:
                    n4=b
                    n5=a
        elif e<=a and e<=b and e<=c :
            n2=e
            if a<=b and a<=c :
                n3=a
                if b<=c :
                    n4=b
                    n5=c
                else:
                    n4=c
                    n5=b
            elif b<=a and b<=c :
                n3=b
                if a<=c :
                    n4=a
                    n5=c
                else:
                    n4=c
                    n5=a
            elif c<=a and c<=b :
                n3=c
                if a<=b :
                    n4=a
                    n5=b
                else:
                    n4=b
                    n5=a
    elif e<=a and e<=b and e<=c and e<=d :
        n1=e
        if a<=b and a<=c and a<=d :
            n2=a
            if b<=c and b<=d :
                n3=b
                if c<=d :
                    n4=c
                    n5=d
                else:
                    n4=d
                    n5=c
            elif c<=b and c<=d :
                n3=c
                if b<=d :
                    n4=b
                    n5=d
                else:
                    n4=d
                    n5=b
            elif d<=b and d<=c :
                n3=d
                if b<=c :
                    n4=b
                    n5=c
                else:
                    n4=c
                    n5=b
        elif b<=a and b<=c and b<=d :
            n2=b
            if a<=c and a<=d :
                n3=a
                if c<=d :
                    n4=c
                    n5=d
                else:
                    n4=d
                    n5=c
            elif c<=a and c<=d :
                n3=c
                if a<=d :
                    n4=a
                    n5=d
                else:
                    n4=d
                    n5=a
            elif d<=a and d<=c :
                n3=d
                if a<=c :
                    n4=a
                    n5=c
                else:
                    n4=c
                    n5=a
        elif c<=a and c<=b and c<=d :
            n2=c
            if a<=b and a<=d :
                n3=a
                if b<=d :
                    n4=b
                    n5=d
                else:
                    n4=d
                    n5=b
            elif b<=a and b<=d :
                n3=b
                if a<=d :
                    n4=a
                    n5=d
                else:
                    n4=d
                    n5=a
            elif d<=a and d<=b :
                n3=d
                if a<=b :
                    n4=a
                    n5=b
                else:
                    n4=b
                    n5=a
        elif d<=a and d<=b and d<=c :
            n2=d
            if a<=b and a<=c :
                n3=a
                if b<=c :
                    n4=b
                    n5=c
                else:
                    n4=c
                    n5=b
            elif b<=a and b<=c :
                n3=b
                if a<=c :
                    n4=a
                    n5=c
                else:
                    n4=c
                    n5=a
            elif c<=a and c<=b :
                n3=c
                if a<=b :
                    n4=a
                    n5=b
                else:
                    n4=b
                    n5=a
    return[n1,n2,n3,n4,n5]    

def promedio_multiplicativo(a:float,b:float,c:float,d:float,e:float) -> float:
    prom_mult=(a*b*c*d*e)**0.2
    return prom_mult

def potencia(n1:float,n5:float) -> float:
    pot=n5**n1
    return pot

def raiz (n1:float) -> float:
    raiz_menor=n1**(1/3)
    return raiz_menor
```
>***9. Consultar qué es y cómo funciona pip en python.***

>***10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.***

