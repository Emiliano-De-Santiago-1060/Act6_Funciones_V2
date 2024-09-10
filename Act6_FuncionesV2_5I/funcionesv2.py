print("Más sobre funciones")
# Aquí se escriben las funciones
def suma_ab(a ,b):
    s = a+b
    return s 

def resta_ab(c, d):
    o = c-d
    return o

def multi_ab(e ,f):
    p = e*f
    return p

def div_ab(g ,h):
    q = g/h
    return q

# Llamadas a funciones
print("Calculando suma")
n1=int(input("Ingresa el primer numero "))
n2=int(input("Ingresa el segundo numero "))
suma=suma_ab(n1, n2)
print(f"La suma de {n1} + {n2} es igual a: {suma}")
print(" ")

print("Calculando resta")
n3=int(input("Ingresa el primer numero "))
n4=int(input("Ingresa el segundo numero "))
resta=resta_ab(n3, n4)
print(f"La resta de {n3} - {n4} es igual a: {resta}")
print(" ")

print("Calculando multiplicacion")
n5=int(input("Ingresa el primer numero "))
n6=int(input("Ingresa el segundo numero "))
multi=multi_ab(n5, n6)
print(f"La resta de {n5} x {n6} es igual a: {multi}")
print(" ")

print("Calculando division")
n7=int(input("Ingresa el primer numero "))
n8=int(input("Ingresa el segundo numero "))
div=div_ab(n7, n8)
print(f"La resta de {n7} entre {n8} es igual a: {div}")