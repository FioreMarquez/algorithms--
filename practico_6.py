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
import math
class Empleado:
    def __init__(self, nombre, sueldo_base):
      assert type(nombre) == str, ' debe ingresar una cadena de caracteres (nombre)'
      assert type(sueldo_base)== int or type(sueldo_base)== float and sueldo_base >=0, ' debe ingresar un numero entero positivo(sueldo)'
      self.nombre= nombre
      self._sueldo_base= sueldo_base #protegido
      self.__bonificaciones = [] #privado

    def get_suelto_total(self)-> float:
      return self._sueldo_base + sum(self.__bonificaciones)

    def get_bonificacion_maxima(self):
        assert len(self.__bonificaciones)> 0, ' no hay bonificaciones registradas'
        return max(self.__bonificaciones)

    def get_bonificacion_minima(self)-> float:
      assert len(self.__bonificaciones)>0, ' debe ingresar una lista de bonificaciones que al menos contenga un monto'
      return min(self.__bonificaciones)
    
    def get_tiene_bonificaciones(self) -> bool:
      return len(self.__bonificaciones)>0
      
    def ver_bonificaciones(self) ->list:
        return self.__bonificaciones.copy()
    
    def agregar_bonificacion(self, monto):
        assert type(monto) == int or type(monto) == float
        assert monto > 0
        self.__bonificaciones.append(monto)

#hay que agregar la lista de empleados como ejemplo.

#Ejercicio 4
class Libro:
    def __init__(self, titulo, autor, anio):
        assert type(anio)== int and anio >0, ' debe ingresar un numero positivo como año'
        assert type(autor)== str and type(titulo)== str, 'autor y titulo deben ser una cadena de caracteres'
        
        self.titulo = titulo
        self.autor= autor
        self.anio= anio
        self._disponible = True
    def estar_disponible(self)->bool:
        return self._disponible
    def prestar(self):
        assert self._disponible == True, 'el libro no esta disponible'
        self._disponible = False
    def devolver(self):
        assert self._disponible != True, 'el libro ya esta disponible'
        self._disponible = True
    def __str__(self):
        return f'Titulo:{self.titulo}| Autor: {self.autor}| Disponible: {self._disponible} '

""""
AGREGAR LOS EJEMPLOS Y/O TESTS
"""

#Ejercicio 5
""""
nota personal: en este caso no se habla de una herencia
estamos en el caso de una composición; una clase tiene objetos de otra
Biblioteca administra los libros una vez que ya existen
"""""
class Biblioteca:
    def __init__(self):
        self._libros = []
    def agregar_libro(self, libro):
        assert isinstance(libro, Libro), 'el objeto debe ser un Libro'
        for l in self._libros:
            if l.titulo == libro.titulo and l.autor == libro.autor:
                raise ValueError ('el libro ya existe en la biblioteca')
        self._libros.append(libro)
    def prestar_libro(self,titulo):
        for l in self._libros:
            if l.titulo == titulo:
                l.prestar()
                return
            raise ValueError ('el libro no existe en la biblioteca')
        
    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        libro.devolver()

    def libros_disponibles(self):
        disponibles = []
        for l in self._libros:
            if l.estar_disponible():
                disponibles.append(l)
        return disponibles

    def cantidad_libros(self):
        return len(self._libros)

    def __str__(self): #se debe ver como el print que le pido
        total = self.cantidad_libros()
        disponibles = len(self.libros_disponibles())
        return f'Biblioteca con {total} libros ({disponibles} disponibles)'
            






    
