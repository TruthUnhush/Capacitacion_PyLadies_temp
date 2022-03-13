
# llave1 = valor1

persona1 = {
    "nombre": "Pepito", 
    "apellido": "Gonzales",
    "tiene_empleo": True, 
    "proyectos completados": 5
}

# print(persona1)

mi_diccionario = dict()

print(mi_diccionario)


# Añadir un elemento

mi_diccionario["numero de personas"] = 12
print(mi_diccionario)

# Acceder a un element

print(mi_diccionario["numero de personas"])

# Modificar un elemento

mi_diccionario["tipo de clase"] = "Programación"
print(mi_diccionario)
mi_diccionario["numero de personas"] = 15
print(mi_diccionario)
mi_diccionario["numero de personas"] += 1
print(mi_diccionario)

# Eliminar un elemento

mi_diccionario["profesor a cargo"] = "Pepito"
print(mi_diccionario)
mi_diccionario.pop("profesor a cargo")
print(mi_diccionario)

