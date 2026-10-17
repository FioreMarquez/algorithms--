#Las funciones son una herramienta fundamental para 
#estructurar programas

#Ejercicio 1
"""1.1 Definir una funcion que calcule el perim de 
un rectangulo siendo x el lado mas corto"""

#suponiendo una funcion general porque no tengo el 
#P1 a mano
def perimetro_rect(x,a):
    #x:lado (lado mas chico)
    #a: altura
    return 2*x + 2*a

print(perimetro_rect(2,6))

#Ejercicio 4
"""Definir una función area_circulo(r) que reciba el radio
y devuelva el área del círculo. Recordar A = phi. r^2"""

import math
def area_circulo(r):
    return math.pi * r**2

print(area_circulo(2))

#Ejericio 5 
# distancia entre dos puntos

def distancia(x1,y1,x2,y2):
    return math.sqrt((x1-y1)^2+(x2-y2)^2)

#Ejercicio 8
"""
1. definir una funcion es_positivo(x) que devuelva
- true si x es positivo
- false en caso contrario
"""
def es_positivo(x:int)->bool:
    if x > 0:
        return True
    else:
        return False

print(es_positivo(-5))

"""
2. Definir una funcion es_positivo2(x) que muestre en pantalla:
- 'es positivo!' so x es positivo
- 'es negativo!' en caso ontrario
"""
def es_positivo2(x:int)-> str:
    if x > 0:
        print("Es positivo!")
    else:
        print("Es negativo!")

es_positivo2(1)
#print(es_positivo2(1)) #wtf me tira none

#Ejercicio 9
""" 
definir una funcion que determina si un float se encuentra entre -5 y 5
devuelve un bool:
- true si es que esta dentro del intervalo
- false si es que no lo está
"""
def test9(n:float)->bool:
    if -5 <= n <= 5:
        return True
    else:
        return False

print(test9(-8))

#ejercicio 10

def test10(x)-> bool:
    if x % 2 == 0:
        return True
    else:
        return False

print(test10(5))

#ejercicio 11. 
'Aca metemos ciclos'

def suma_n(n):
    entero = 1
    suma = 0
    while entero <= n:
        suma = suma + entero
        entero = entero + 1
    return suma 

print(suma_n(3))

#ejercicio 12 
""" se introduce la notacion type hints.
ocurre que esta no se verifica automaticamente en la ejecion del programa
tenemos que verificar los argumentos de forma explicita
dentro de la fnción """

#ejercicio 13
"""se implementa la funcion que evalue 
f(x) = ax + b"""

def evaluar_lineal(a : float, b:float, x:float)-> float:
    isinstance(a,(float,int))
    isinstance(b, (float,int))
    isinstance(x,(float,int))
    return a * x + b

#ejercicio 14
# Codigo
def vertice_parabola(a :float, b:float, c:float) -> tuple:
   assert a > 0 or a < 0, 'a debe ser distinto de cero'
   xv = - b/(2*a)
   yv = a * xv ** 2  + b * xv + c

   return xv, yv



#ejercicio 28

x = 10 #variable global

def f():
    x = 5 #variable local que tapa la global mientras se ejecuta la funcion
    return x
resultado = f()

print("resultado:", resultado)
print("x global:", x)

"""aca la variable dentro de la funcion no modifica la global
porque"""



#ejercicio 29

def externa():
    x = 3

    def interna():
        return x*2
    return interna() #devuelve 6

''' externa es f(g(x)) siendo interna = g(x)
 x es variable local para externa = f(x)
 x es envolvente
 '''
#ahora se modifica para que devuelva x*y
def externa():
    x = 3
    def interna(y):
        return x * y
    return interna(2)

externa()   # 6