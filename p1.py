#Ex 1
a = 5
b = 3.2
c = 1 + 3j
d = "hola"
e = True
f = False

print(type(5))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

""" que ocurre cuando se convierte un número distinto de cero a bool?"""
print(bool(a))
""" que ocurre cuando se convierte un número cero a bool?"""
print(bool(0))
""" se puede convertir una cadena 5 a número?, a qué tipo de número?"""
print(int(5))
print(float(5))#si tiene caracteres falla
""" se puede convertir una cadena 5.9 a número? a qué tipo de nuúmero?"""
print(int(5.9))
print(float(5.9))
""" qué ocurre al convertir b a entero?"""
print(int(b))

"""se pueba lo siguiente, por consigna"""
print(a+b)
print(a+c)
print(b*2)

#punto 4. Se ejecuta lo siguiente:
print(0.1+0.2) # no da 0.3 exácto, por error de redondeo

"""
Escribir un programa que:

1.pida dos números al usuario llamados 'a' y 'b'

2. lo convierta a número real (float)

3. Realice las siguientes  operaciones 

```
- (a>0) and (b>0)
- (a>0) or (b>0)
- not (a>0)
```
4. ¿Qué hace cada operacion?
"""
def comparacion(a,b):
    a = input('ingrese un numero entero')
    b = input('ingrese otro numero entero')

    c=float(a)
    d=float(b)

    op1= print((c < 0)and (d > 0))
    op2= print((c>0)or(d>0))
    return op1, op2

print(comparacion(2,3))

