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