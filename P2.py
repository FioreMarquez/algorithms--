#Las funciones son una herramienta fundamental para 
#estructurar programas

#Ejercicio 1
"""1.1 Definir una funcion que calcule el perim de 
un rectangulo siendo x el lado mas corto"""

def perimetro_rect(x,a):
    #x:lado (lado mas chico)
    #a: altura
    return 2*x + 2*a

print(perimetro_rect(2,6))