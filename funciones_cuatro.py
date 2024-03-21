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