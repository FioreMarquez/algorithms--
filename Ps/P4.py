#Diccionarios
"solo codigos, sin tests. Ya estan probados y andan. Es solo registro"

#Ejercicio 1

def contar_letras(cadena: str)-> dict:
    'funcion que toma un str y devuelve un dict con claves y valores'
    'ignorando los espacios'
    assert type(cadena) == str, 'debe ingresar una cadena de caracteres'
    lista ={}
    for i in cadena:
        if i != " ":
          lista[i]= lista.get(i,0) + 1
    return lista

#ejercicio 2

# codigo
def frecuencia_palabras(texto:str):
    assert type(texto)== str, ' debe ingresar una cadena de caracteres'
    palabras = {}
    for i in texto.split():
        palabras[i] = palabras.get(i,0) + 1
    return palabras

print(frecuencia_palabras("hola a todos"))

#Ejercicio 3

def filtrar_por_valor(d:dict, umbral:int) -> dict:
    """ funcion que toma un diccionario con valores numéricos y devuelve
    un nuevo diccionario que contenga unicamente los pares key,value tales que 
    valor > umbral """
    isinstance(d,dict), ' debe ingresar una cadena con valores numericos'
    diccionario = {}
    for k,v in d.items():
        if v > umbral:
            diccionario[k] = v
    return diccionario

#ejercicio 4

