## Ejercicio 1

#En este ejercicio vas a implementar una clase que represente un personaje de un videojuego.

#1. Definir una clase `Personaje` con los siguientes atributos:

#- Atributos (públicos)
"""
    - `nombre`: nombre del personaje (`str`)
    - `salud`: cantidad de vida del personaje (`int`)
    - `nivel`: nivel del personaje (`int`)

- Constructor: Implementar el método `__init__` que:

    - reciba `nombre`, `salud` y `nivel`
    - inicialice los atributos correspondientes
    - valide:
        - que `nombre` sea un `str`
        - que `salud` sea un entero mayor o igual a 0
        - que `nivel` sea un entero mayor o igual a 1

- Implementar los siguientes métodos:

    - `subir_nivel() -> None`  Incrementa el nivel del personaje en 1.

    - `recibir_danio(danio: int) -> None` Reduce la salud del personaje en la cantidad indicada.

    - Requisitos:
        - validar que `danio` sea un entero positivo
        - si la salud resultante es menor o igual a 0:
            - establecer la salud en 0
            - imprimir: `"El personaje ha sido derrotado"`

- Método especial

    - `__str__() -> str`  
  Debe devolver un string con el estado del personaje en el siguiente formato:

```python
"Nombre: Link | Salud: 80 | Nivel: 5"
``` 
Restricciones
- Usar assert para validar entradas
- No permitir valores inválidos (salud negativa, nivel menor a 1, etc.)
- Escribir código claro y legible
"""
#Codigo


#Ejercicio 1
# codigo
class Personaje:
    def __init__(self, nombre, salud, nivel):
        self.nombre = nombre
        self.salud = salud
        self.nivel = nivel
        assert type(nombre)== str, ' debe ingresar una cadena de caracteres'
        assert type(salud)== int and salud >=0 , ' debe ingresar un entero mayor a 0'
        assert type (nivel)== int and nivel >1, ' debe ingresar un entero mayor a 1'
    def get_nombre(self):
        return self.nombre
    def get_salud(self):
        return self.salud
    def get_nivel(self):
        return self.nivel 
    def subir_nivel(self):
        self.nivel = self.nivel + 1
    def recibir_danio(self, danio:int):
        assert type(danio) == int and danio >0, ' debe ingresar un entero positivo'
        self.salud = self.salud - danio 
        if self.salud <= 0:
            self.salud = 0
            print('el personaje ha sido derrotado')
    def __str__(self):
        return f"nombre: {self.nombre} | Salud: {self.salud}| nivel : {self.nivel}"

#Ejercicio 2
#codigo
class Punto:
    def __init__(self, x, y):
        assert isinstance(x,(int,float))
        assert isinstance(y,(int,float))
        self.x = x
        self.y = y
    def __str__(self):
        return f"x: {self.x}| y:{self.y}"
    def distancia_al_origen(self):
        return ((self.x - 0 )**2 + (self.y - 0)**2)**0.5
    

#ejercicio 3
#codigo

    
