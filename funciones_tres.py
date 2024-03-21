def cantidad_carne(gallinas:int,gallos:int,pollitos:int) -> int:
    carne=gallinas*6+gallos*7+pollitos*1
    return carne
if __name__ == "__main__":
    gallinas: int = int(input("Ingrese el número de gallinas: "))
    gallos: int = int(input("Ingrese el número de gallos: "))
    pollitos: int = int(input("Ingrese el número de pollitos: "))
    kilos_carne=cantidad_carne(gallinas,gallos,pollitos)
    print("La cantidad de carne de aves es de",kilos_carne,"kilogramos")