frutas = ["Manzana", "Chirimoya", "Papaya", "Chirimoya", "Uvas", "Chirimoya", "Pera"]

for fruta in frutas:
    print(f"Tu fruta es: {fruta}")

for i in range(5):
    print(f"Iteración: {i} Hola a todos")

n_chirimoyas = 0

for fruta in frutas:

    print(f"Fruta actual {fruta}")
    if fruta == "Chirimoya":
        n_chirimoyas += 1

    if n_chirimoyas == 2:
        break

i = 0

print(n_chirimoyas)

n_chirimoyas = 0

while n_chirimoyas < 3:

    elemento = frutas[i]

    print(f"La fruta en el ciclo while es {elemento}")

    if elemento == "Chirimoya":
        n_chirimoyas += 1

    i += 1

comando = input("Dame un comado: ")

while comando != "exit":

    print("Hola")
    comando = input("Si quieres salir, introduce exit: ")