a = 5

b = 2

if b > a :
    print("Esto es verdadero")
else:
    print("Esto no es verdad")


edad = input("¿Cuál es tu edad?: ")

edad = int(edad)


if edad < 3:
    print("Eres un bebé")
elif 2 < edad < 11:
    print("Eres un niño o niña")
elif edad < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")

