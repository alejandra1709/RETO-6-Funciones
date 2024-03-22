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
    mult=(a*b*c*d*e)
    if mult <0:
        prom_mult=(-mult)**0.2*-1
    else:
        prom_mult=mult**0.2
    return prom_mult

def potencia(n1:float,n5:float) -> float:
    pot=n5**n1
    return pot

def raiz (n1:float) -> float:
    if n1<0:
        raiz_menor=(-n1)**(1/3)*-1
    else:
        raiz_menor=n1**(1/3)
    return raiz_menor