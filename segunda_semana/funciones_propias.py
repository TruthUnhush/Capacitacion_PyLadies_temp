def saludo(nombre, edad):
    print(f"Hola {nombre}!")
    print(f"Tienes {edad} años.")
    print("Que gusto de conocerte!")

def quitar_vida():
    global vida
    vida -= 1

def sumar_dos_numeros(a, b):
    return a + b


vida = 3

print(vida)
saludo("Maria", 22)
quitar_vida()
print(vida)


frutas = ["Manzana", "Chirimoya", "Papaya", "Chirimoya", "Uvas", "Chirimoya", "Pera"]
texto = "Hola a todos"
texto = "Adios a todos"

print(frutas)
frutas[0] = "Naranjas"
print(frutas)

print(texto[8:12])

otra_lista = frutas[:3]
mismas_frutas = frutas[:]

print(otra_lista)
print(frutas)
print()

frutas.append("Melon")

print(frutas)
print(mismas_frutas)
print()

print(frutas[::-1])
print(frutas)

frutas.pop()

print(frutas)

print()

a = 10
b = 5
c = 12


resultado = sumar_dos_numeros(a, b)

print(resultado + c) 