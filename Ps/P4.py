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

