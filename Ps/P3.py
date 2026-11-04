#P3- Parte 1:  Ciclos
'los codigos estan probados, todos andan.'
'esto es solo un registro'
#Ejercicio 1.
""" Pedir un numero n y mostrar su tabla de multiplicar
del 1 al 10"""

numero =  int(input('ingrese un numero entero'))
for i in range(1,numero+1):
    print(i * 10)

#Ejercicio 2
'recibe un entero n, cuenta cuantos pares hay entre 1 y n'
def pares(n):
    numeros_par = 0
    for i in range(1,n):
        if i % 2 == 0:
            numeros_par = numeros_par + 1
    return numeros_par

 #Ejercicio 3
def Suma_pares_impares(n:int):
    """recibe un entero pasitivo n y devuelve la
    suma de pares a impares """
    assert type(n)==int and n>0, 'debe ingresar un nro. positivo'
    pares= 0
    impares = 0
    for i in range(1,n+1):
        if i % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
    return pares, impares
#Ejercicio 4
def suma_multiplos(n:int):
    suma = 0
    for i in range(1,n+1):
        if i % 3 == 0:
            suma = suma + 1
    return suma

#Ejercicio 5
def suma_hasta(n:int):
    assert type(n) == int and n > 0, 'debe ingresar un entero positivo'
    suma = 0
    for i in range(1,n+1):
        suma = suma + i
    return suma

def sumatorio_2(n:int):
    assert type(n) == int and n > 0, 'debe ingresar un entero positivo'
    sumatorio = n*(n+1)//2
        
    return sumatorio


#P3- Parte 2: Cadenas
#Ejercicio 1.1
def analizar_cadena1(cadena:str):
    """recibe un string y devuelve la cantidad de caracteres, letras y números"""
    caracteres= 0
    digitos = 0
    letras = 0
    for i in cadena:
        if i.isalpha():
            letras = letras + 1
        if i.isdigit():
            digitos = digitos + 1
        if i.isalnum():
            caracteres = caracteres + 1
    return letras, digitos, caracteres

# Ejercicio 1.3
def analizar_cadena3(cadena:str):
    """ recibe una cadena y devuelve la cantidad de espacios"""
    espacios = 0
    for i in cadena:
        if i == " ":
            espacios = espacios + 1
    return espacios

#ejercicio 2
def invertir_cadena(cadena:str):
    cadena_invertida = ""
    for i in cadena:
        cadena_invertida = i + cadena_invertida
    return cadena_invertida