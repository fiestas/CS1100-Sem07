''' 
def escribe_media(x,y):
    resultado = (x + y) / 2
    print("La media de %f y %f es: %f"%(x,y,resultado))
    return resultado

def main():
    a = 3
    b = 5
    escribe_media(a,b)
    escribe_media(1, 4)
    escribe_media(10, 18)
    print("Programa terminado")

# Llamada a la funcion Principal que tiene por nombre main()
if (__name__== "__main__"):
    main()
'''

def calcula_media(*args):
    total = 0
    for i in args:
        total += i
    resultado = total / len(args)
    return resultado

def main():
    a, b, c, d = 3, 5, 10, 21
    media = calcula_media (a, b, c, d)
    print("La media de %f, %f, %f y %f es: %f" % (a, b,c,d, media))
    print("Programa terminado")

if __name__== "__main__":
    main()

